n=7
a=n//2
b=n//2
flag=0
for i in range(n):
  for j in range(n):
    if(j==a or j==b):
      print('*',end=' ')
    else:
      print(' ',end=' ')
    if(a==0 and b==6):
      flag=1
  if(flag== 0):
    a-=1
    b+=1
  else:
    a+=1
    b-=1
  print()
