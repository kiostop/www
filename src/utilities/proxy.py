from itertools import cycle
import os
from loguru import logger
from config import config


class ProxyDispatcher:
    proxies: list[str] | None = None

    def __init__(self, proxy_file: str | None) -> None:
        if proxy_file is None or proxy_file == '':
            return

        self.proxy_file = proxy_file
        with open(proxy_file, 'r') as file:
            self.proxies = file.read().splitlines()

        self.proxy_cycle = cycle(self.proxies)

    def get_proxy(self) -> str | None:
        if self.proxies is None or len(self.proxies) == 0:
            return None

        proxy = next(self.proxy_cycle)
        return proxy

    def remove_proxy_from_file(self, proxy: str) -> None:
        if self.proxies is None or len(self.proxies) == 0:
            return

        try:
            self.proxies.remove(proxy)
            with open(self.proxy_file, 'w') as file:
                file.write("\n".join(self.proxies) + "\n")
        except ValueError:
            pass  # Proxy not found, or already removed

proxy_dispatcher = ProxyDispatcher(config.PROXY_FILE)


async def custom_clone_key(key_to_clone: str, retry_count: int = 0) -> tuple:
    if retry_count > config.RETRY_COUNT or not signal_handler.KEEP_PROCESSING:
        return None

    proxy = proxy_dispatcher.get_proxy()
    try:
        key, register_data, private_key = await clone_key(
            key=key_to_clone,
            proxy_url=proxy,
            device_model=len(config.DEVICE_MODELS) > 0 and random.choice(config.DEVICE_MODELS) or None,
        )

        key_dispatcher.add_key(key["license"])

        return key, register_data, private_key
    except Exception as e:
        logger.error("{} (key: {}, retry count: {}, proxy: {})".format(
            e,
            key_to_clone,
            retry_count,
            proxy
        ))

        # Remove the failed proxy from the pool and file
        if proxy:
            proxy_dispatcher.remove_proxy_from_file(proxy)

        if config.DELAY > 0 and signal_handler.KEEP_PROCESSING:
            sleep_time = config.DELAY

            while sleep_time > 0 and signal_handler.KEEP_PROCESSING:
                await asyncio.sleep(delay=1)
                sleep_time -= 1

        return await custom_clone_key(key_to_clone=key_to_clone, retry_count=retry_count + 1)
