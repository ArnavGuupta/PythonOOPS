class manufacture:
    def add_info(self):
        self.brand = input("Enter brand:")
        self.name  = input("Enter name:")
        self.price = float(input("Enter price"))
class stock(manufacture):
    def stock_price(self):
        global mbrand,mprice
        mb = []
        mp = []
        for i in range(3):
         b = input("Enter brand")
         p = float(input("Enter price"))
         p = p + (10/100*p)
         mb.append(b)
         mp.append(p)
         mbrand = mb
         mprice = mp
class sales(stock):
   def show(self):
      print("Brand \t \t price")
      for i in range(3):
         print(mbrand[i],'\t\t',mprice[i])

obj = sales()
obj.add_info()
obj.stock_price()
obj.show()