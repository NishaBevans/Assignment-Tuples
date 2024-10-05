def display_orders(orders):
    for customer, product, quantity in orders:
        print(f"{customer} ordered {quantity} {product}(s).")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
]

display_orders(orders)