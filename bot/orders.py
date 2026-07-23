from binance.exceptions import BinanceAPIException, BinanceRequestException
from .client import get_client
from .logging_config import logger

def place_market_order(symbol: str, side: str, quantity: float) -> dict:
    client = get_client()
    try:
        logger.info(f"Requesting MARKET order: {side} {quantity} {symbol}")
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"MARKET order response: {response}")
        return response
    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Binance Exception: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Exception: {e}")
        raise

def place_limit_order(symbol: str, side: str, quantity: float, price: float) -> dict:
    client = get_client()
    try:
        logger.info(f"Requesting LIMIT order: {side} {quantity} {symbol} at {price}")
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price
        )
        logger.info(f"LIMIT order response: {response}")
        return response
    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Binance Exception: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Exception: {e}")
        raise

def place_stop_market_order(symbol: str, side: str, quantity: float, stop_price: float) -> dict:
    client = get_client()
    try:
        logger.info(f"Requesting STOP_MARKET order: {side} {quantity} {symbol} with Stop Price {stop_price}")
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP_MARKET',
            quantity=quantity,
            stopPrice=stop_price
        )
        logger.info(f"STOP_MARKET order response: {response}")
        return response
    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Binance Exception: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Exception: {e}")
        raise
