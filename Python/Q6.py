def even_odd(number):
    if not isinstance(number, int):
        return "Invalid input"
    return "Even" if number % 2 == 0 else "Odd"

number = 17
print(even_odd(number))
