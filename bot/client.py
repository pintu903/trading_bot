import os
from binance.client import Client
from .logging_config import logger

def get_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        logger.error("API keys not found in environment variables.")
        raise ValueError("BINANCE_API_KEY and BINANCE_SECRET_KEY must be set in .env")

    # Connect to Binance Futures Testnet
    client = Client(api_key, api_secret, testnet=True)
    return client
