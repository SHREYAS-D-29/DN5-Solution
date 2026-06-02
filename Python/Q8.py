def salary_stats(salaries):
    if not salaries:
        return "Invalid list"
    print("Lowest Salary:", min(salaries))
    print("Highest Salary:", max(salaries))

salary_list = [50000, 75000, 62000, 95000]
salary_stats(salary_list)
