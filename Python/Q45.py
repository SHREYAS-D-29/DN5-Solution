import csv,datetime
current=datetime.datetime.now().month
tot={}
with open('expenses.csv') as f:
    for r in csv.DictReader(f):
        d=datetime.datetime.strptime(r['date'],'%Y-%m-%d')
        if d.month==current:
            tot[r['category']]=tot.get(r['category'],0)+float(r['amount'])
print(tot)
