def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper()
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with 'USDT' (e.g., BTCUSDT)")
    return symbol

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be 'BUY' or 'SELL'")
    return side

def validate_positive_number(value: float, field_name: str) -> float:
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than 0")
    return value
