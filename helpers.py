import os

from loguru import logger
from dotenv import load_dotenv

README_URL = "https://github.com/nir007/uniswap_v2/blob/main/README.md"

def is_number(val: str) -> bool:
    return val.replace(".", "").isdigit()


def get_start_up_settings():
    load_dotenv()

    try:
        proxy = os.getenv("PROXY")
        private = os.getenv("PRIVATE")
        agg_base_url = os.getenv("AGGREGATOR_API_BASE_URL")
        open_api_base_url = os.getenv("OPEN_API_BASE_URL")

        if not private:
            raise RuntimeError(f"Setup your private key in .env file please. \nSee {README_URL}")

        if not agg_base_url:
            raise RuntimeError(f"Setup XY Finance agg api base url in .env file please. \nSee {README_URL}")

        if not open_api_base_url:
            raise RuntimeError(f"Setup XY Finance open api base url in .env file please. \nSee {README_URL}")

        return proxy, private, agg_base_url, open_api_base_url

    except Exception as e:
        logger.error(f"Invalid startup data: {e}")
