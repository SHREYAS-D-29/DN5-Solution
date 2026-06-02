def even_odd(num):
    if not isinstance(num, int):
        return "Invalid input"
    return "Even" if num % 2 == 0 else "Odd"

num = 8
print(even_odd(num))
