from utils import calculate_tax

def process_order(price):
    tax = calculate_tax(price)
    total = price + tax
    return total

def get_discounted_price(price, discount):
    return price * (1 - discount)
