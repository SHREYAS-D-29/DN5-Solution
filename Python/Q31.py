def create_cart():
    cart = [100, 250, 75]

    if not all(isinstance(item, (int, float)) for item in cart):
        print("Invalid cart items")
        return

    print("Cart Contents:", cart)

create_cart()
