import json
class Employee:
    def __init__(self,id,name): self.id=id; self.name=name
    def __str__(self): return f'{self.id} - {self.name}'
emps={'E101':'John','E102':'Mary'}
with open('emps.json','w') as f: json.dump(emps,f)
with open('emps.json') as f: data=json.load(f)
for k,v in data.items(): print(Employee(k,v))
