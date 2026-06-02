def greet():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty")
    else:
        print(f"Hello, {name}!")

greet()
