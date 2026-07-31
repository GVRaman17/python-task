sum=0
while(True):
  a=int(input('enter a no.:'))
  if not(-1<a and a<7):
    print("enter in range 0-6")
    continue
  elif a==0:
    break;
  else:
    sum+=a
print(sum)
