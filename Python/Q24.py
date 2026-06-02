from math import *

def demonstrate_math(value):
    if value < 0:
        print("Invalid input")
        return

    print(f"Square Root: {sqrt(value):.2f}")
    print(f"Power (value^2): {pow(value, 2):.2f}")
    print(f"Pi Value: {pi:.2f}")

demonstrate_math(9)
