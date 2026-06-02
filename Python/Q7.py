def split_bill(total_bill, people):
    if total_bill <= 0 or people <= 0:
        return "Invalid input"
    return total_bill // people

total_bill = 1250
people = 4
print("Individual Share:", split_bill(total_bill, people))
