from tabulate import tabulate
class Converter:
    def c_to_f(self,c): return c*9/5+32
c=25
print(tabulate([['Celsius',c],['Fahrenheit',Converter().c_to_f(c)]],headers=['Type','Value']))
