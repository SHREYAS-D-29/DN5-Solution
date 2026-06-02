def kg_to_lbs(kg):
    if kg <= 0:
        return "Invalid weight"
    return kg * 2.20462

kg = 70.5
print(f"Weight in pounds: {kg_to_lbs(kg):.2f}")
