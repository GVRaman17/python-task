x=int(input('enter a number :'))
temp=x
rev=0
while temp>0:
    y=temp%10
    rev=rev*10+y
    temp=temp//10
if rev==x:
    print('palindrom')
else:
    print('not palindrom')
