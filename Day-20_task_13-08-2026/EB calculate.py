def unit_100(a=100):
  return(a*2)
def unit_200(a=100):
  return(a*3)
def unit_400(a=200):
  return(a*5)
def unit_max(a):
  return(a*7)
unit=int(input('enter a unit: '))
if unit<=100:
  price=unit_100(unit)
elif unit>100 and unit<=200:
  price=unit_100()+unit_200(unit-100)
elif unit>200 and unit<=400:
  price=unit_100()+unit_200()+unit_400(unit-200)
elif unit>400:
  price=unit_100()+unit_200()+unit_400()+unit_max(unit-400)
print("the unit is '",unit,"' the price:",price)
