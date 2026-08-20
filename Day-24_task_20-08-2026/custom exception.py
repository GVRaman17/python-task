class ZeroBalance(Exception):
  pass
balance=int(input("enter a balance:"))
try:
  if balance!=0:
    print("transaction succefully")
  else:
    raise ZeroBalance("zero balance exception")
except Exception as ex:
  print(ex)
