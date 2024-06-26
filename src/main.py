import asyncio
import signal
import random
from typing import Optional, Tuple
import aiohttp
import json
from loguru import logger
from config import config
from warp import RegisterData, clone_key, GetInfoData
from utilities import key_dispatcher, proxy_dispatcher

class SignalHandler:
    KEEP_PROCESSING: bool = True

    def __init__(self) -> None:
        signal.signal(signalnum=signal.SIGINT, handler=self.exit_gracefully)
        signal.signal(signalnum=signal.SIGTERM, handler=self.exit_gracefully)

    def exit_gracefully(self, signum, frame) -> None:
        logger.info("Received signal {}, stopping all threads...".format(signum))
        self.KEEP_PROCESSING = False

signal_handler = SignalHandler()

async def custom_clone_key(key_to_clone: str, retry_count: int = 0) -> Optional[Tuple[GetInfoData, RegisterData, Optional[str]]]:
    if retry_count > config.RETRY_COUNT or not signal_handler.KEEP_PROCESSING:
        return None

    try:
        key, register_data, private_key = await clone_key(
            key=key_to_clone,
            proxy_url=proxy_dispatcher.get_proxy(),
            device_model=len(config.DEVICE_MODELS) > 0 and random.choice(config.DEVICE_MODELS) or None,
        )

        key_dispatcher.add_key(key["license"])

        return key, register_data, private_key
    except Exception as e:
        logger.error("{} (key: {}, retry count: {})".format(
            e,
            key_to_clone,
            retry_count
        ))

        if config.DELAY > 0 and signal_handler.KEEP_PROCESSING:
            sleep_time = config.DELAY

            while sleep_time > 0 and signal_handler.KEEP_PROCESSING:
                await asyncio.sleep(delay=1)
                sleep_time -= 1

        return await custom_clone_key(key_to_clone=key_to_clone, retry_count=retry_count + 1)

async def worker(id: int, session: aiohttp.ClientSession, urls: list, index: int) -> None:
    logger.debug("Worker {} started".format(id))

    while signal_handler.KEEP_PROCESSING:
        response = await custom_clone_key(
            key_to_clone=key_dispatcher.get_key(),
        )

        if response is not None:
            key, register_data, private_key = response

            output = {
                "key": key["license"],
                "referral_count": f"{key['referral_count']} GB",
                "private_key": config.SAVE_WIREGUARD_VARIABLES and private_key or "",
                "peer_endpoint": config.SAVE_WIREGUARD_VARIABLES and register_data["config"]["peers"][0]["endpoint"]["host"] or "",
                "peer_public_key": config.SAVE_WIREGUARD_VARIABLES and register_data["config"]["peers"][0]["public_key"] or "",
                "interface_addresses": config.SAVE_WIREGUARD_VARIABLES and (register_data["config"]["interface"]["addresses"]["v4"] + "/32, " + register_data["config"]["interface"]["addresses"]["v6"] + "/128") or ""
            }

            #logger.success(json.dumps(output))

            post_url = urls[index % len(urls)]
            async with session.post(post_url, json=output) as resp:
                if resp.status == 200:
                    logger.info(f"Successfully posted data for key: {key['license']} to {post_url}")
                else:
                    logger.error(f"Failed to post data for key: {key['license']} to {post_url}, status code: {resp.status}")

            index += 1  # Update the index for the next URL

        if signal_handler.KEEP_PROCESSING and config.DELAY > 0:
            sleep_time = config.DELAY

            while sleep_time > 0 and signal_handler.KEEP_PROCESSING:
                await asyncio.sleep(delay=1)
                sleep_time -= 1

async def main() -> None:
    tasks = []
    urls = [
        "https://warp1.242024.xyz/api/warp/savekey",
        "https://warp2.242024.xyz/api/warp/savekey",
        "https://warp3.242024.xyz/api/warp/savekey",
        "https://warp4.242024.xyz/api/warp/savekey",
        "https://warp5.242024.xyz/api/warp/savekey",
        "https://warp6.242024.xyz/api/warp/savekey",
        "https://warp7.242024.xyz/api/warp/savekey",
        "https://warp8.242024.xyz/api/warp/savekey",
        "https://warp9.242024.xyz/api/warp/savekey",
        "https://warp10.242024.xyz/api/warp/savekey"
    ]

    async with aiohttp.ClientSession() as session:
        for i in range(config.THREADS_COUNT):
            tasks.append(
                asyncio.create_task(worker(i + 1, session, urls, i))
            )

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
