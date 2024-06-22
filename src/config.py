class Settings():
    BASE_KEYS: list[str] = [
            '9h5A32Gm-kc6H13D8-Y695a2RM',
            'Fl1Rk529-165ba0CQ-94h57zxL',
            '5802hSzp-a6n2l3H4-1dh502Li',
            'W8GR5r91-8Smk034x-pH230gL9',
            '8Mk46m5e-Gm7k214u-0nc798oK',
            'f61J50Yh-2W8g0v6y-43Fng05i',
            '598UHE3T-43fc08MH-36B5t2Or',
            '6jVD9b72-U10L7Gv8-RV5C814i',
            '7N3kUf92-6bKr201h-L402qkP5',
            'f724Wuk3-Tp5Mo937-05o3XDs7',
            '4OVo721Y-D062i1Zr-OW90VL23',
        ]
    THREADS_COUNT: int = 1
    PROXY_FILE: str | None = None
    DEVICE_MODELS: list[str] = []
    SAVE_WIREGUARD_VARIABLES: bool = True
    DELAY: int = 25
    OUTPUT_FILE: str = 'output.txt'
    OUTPUT_FORMAT: str = '{key} | {referral_count} GB | {private_key} | {peer_endpoint} | {peer_public_key} | {interface_addresses}'
    RETRY_COUNT: int = 1


config = Settings()
