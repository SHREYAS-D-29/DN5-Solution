def check_pass(marks):
    if not 0 <= marks <= 100:
        return "Invalid marks"
    return "Pass" if marks >= 40 else "Fail"

marks = 75
print(check_pass(marks))
