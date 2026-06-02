import json
grades={'John':[80,90]}
with open('grades.json','w') as f: json.dump(grades,f)
print('Class Average:',sum(grades['John'])/len(grades['John']))
