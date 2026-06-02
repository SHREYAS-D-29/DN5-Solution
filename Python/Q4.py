def net_salary(salary, tax_rate):
    if salary < 0 or not (0 <= tax_rate <= 1):
        return "Invalid input"
    return salary * (1 - tax_rate)

salary = 75000.5
tax_rate = 0.18
print(f"Net Salary: {net_salary(salary, tax_rate):.2f}")
