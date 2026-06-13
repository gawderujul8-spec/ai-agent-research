from core import process_order
from utils import format_currency

def checkout(cart):
    total = 0
    for item in cart:
        total += process_order(item['price'])

    print(f"Checkout total: {format_currency(total)}")
