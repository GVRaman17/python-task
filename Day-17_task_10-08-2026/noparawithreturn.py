def odev():
  print('with par no return')
  a=int(input('val='))
  if a%2==0:
    return('even',a)
  else:
    return('odd',a)
c,a=odev()
print(c,":",a)
