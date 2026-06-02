def assign_grade(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

score = 88
print("Grade:", assign_grade(score))
