def calculate(a,b,op):
    if op=='+': return a+b
    if op=='-': return a-b
    if op=='*': return a*b
    if op=='/': return a/b
try:
    a=float(input('A:')); b=float(input('B:')); op=input('Op:')
    print('Result:',calculate(a,b,op))
except Exception as e: print('Error:',e)
