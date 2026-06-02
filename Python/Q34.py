def get_salary(data, department, employee):
    if department not in data:
        print("Department not found")
        return

    if employee not in data[department]:
        print("Employee not found")
        return

    print("Salary:", data[department][employee])

employees = {
    "IT": {"John": 60000, "Mary": 75000},
    "HR": {"David": 50000}
}

get_salary(employees, "IT", "Mary")
