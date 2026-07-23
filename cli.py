import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from dotenv import load_dotenv

from bot.orders import place_market_order, place_limit_order, place_stop_market_order
from bot.validators import validate_symbol, validate_side, validate_positive_number

load_dotenv()

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")
console = Console()

def display_response(title: str, response: dict):
    table = Table(title=title)
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="magenta")

    keys_to_display = ["orderId", "symbol", "status", "type", "side", "origQty", "executedQty", "avgPrice", "price", "stopPrice"]
    for key in keys_to_display:
        if key in response:
            table.add_row(key, str(response[key]))

    console.print(table)
    rprint("[bold green]Success: Order placed successfully.[/bold green]")

@app.command()
def market(symbol: str, side: str, quantity: float):
    """Place a MARKET order."""
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_positive_number(quantity, "quantity")
        
        console.print(f"[bold yellow]Requesting MARKET {side} for {quantity} {symbol}[/bold yellow]")
        response = place_market_order(symbol, side, quantity)
        display_response("MARKET Order Details", response)
    except Exception as e:
        rprint(f"[bold red]Failed to place MARKET order:[/bold red] {e}")

@app.command()
def limit(symbol: str, side: str, quantity: float, price: float):
    """Place a LIMIT order."""
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_positive_number(quantity, "quantity")
        price = validate_positive_number(price, "price")

        console.print(f"[bold yellow]Requesting LIMIT {side} for {quantity} {symbol} at {price}[/bold yellow]")
        response = place_limit_order(symbol, side, quantity, price)
        display_response("LIMIT Order Details", response)
    except Exception as e:
        rprint(f"[bold red]Failed to place LIMIT order:[/bold red] {e}")

@app.command()
def stop(symbol: str, side: str, quantity: float, stop_price: float):
    """Place a STOP_MARKET order."""
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_positive_number(quantity, "quantity")
        stop_price = validate_positive_number(stop_price, "stop_price")

        console.print(f"[bold yellow]Requesting STOP_MARKET {side} for {quantity} {symbol} with stop price {stop_price}[/bold yellow]")
        response = place_stop_market_order(symbol, side, quantity, stop_price)
        display_response("STOP_MARKET Order Details", response)
    except Exception as e:
        rprint(f"[bold red]Failed to place STOP_MARKET order:[/bold red] {e}")

if __name__ == "__main__":
    app()
