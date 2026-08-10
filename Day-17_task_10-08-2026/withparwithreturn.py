def odev(a):
  print('with par with return')
  if a%2==0:
    return('even')
  else:
    return('odd')
a=int(input('val='))
c=odev(a)
print(c,":",a)
