class supermarket:
  def __init__(self,name):
    self.S_name=name
  def customer(self,name,ph):
    self.name=name
    self.ph=ph
  def product(self,name,price):
    self.p_name=name
    self.price=price
  def display(self):
    print(f"{self.S_name} supermarket \n----------------------------\ncustomer name{self.name}\ncustomer ph{self.ph}\nproduct name{self.p_name}\nprice{self.price}")
s1=supermarket('more')
s1.customer('venkat',6383560226)
s1.product('sunflower oil',200)
s1.display()
