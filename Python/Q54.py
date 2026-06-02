class Product: pass
class Perishable(Product): pass
class Electronics(Product): pass
stock={'Laptop':5,'Milk':2}
alerts={k for k,v in stock.items() if v<3}
print('Low Stock:',alerts)
