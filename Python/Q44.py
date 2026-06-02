import csv
rows=[]
with open('employees.csv') as f:
    rows=list(csv.DictReader(f))
high=[r for r in rows if int(r['salary'])>50000]
print('High Salary Employees:',len(high))
print('Average Salary:',sum(int(r['salary']) for r in rows)/len(rows))
