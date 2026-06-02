class CartItem:
    def __init__(self,n,p,q): self.n=n; self.p=p; self.q=q
class ShoppingCart:
    def __init__(self): self.items=[]
    def add_item(self,i): self.items.append(i)
    def total(self): return sum(x.p*x.q for x in self.items)
cart=ShoppingCart(); cart.add_item(CartItem('Pen',10,2))
subtotal=cart.total(); gst=subtotal*0.18
print('Total:',subtotal+gst)
