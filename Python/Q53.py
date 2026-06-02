from datetime import datetime
tasks=[{'name':'Task1','due':'2026-01-01'}]
tasks.sort(key=lambda x: datetime.strptime(x['due'],'%Y-%m-%d'))
print(tasks)
