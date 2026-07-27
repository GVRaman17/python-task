a=1
b=1
flag=0
while(a<=5):
    if a==5 and flag==0:
        print(b,end=' ')
        a=1
        flag=1
    elif flag==0:
        print(b,end=' ')
        b+=1
        a+=1
    elif flag==1 and a!=5:
        print(b-a,end=' ')
        a+=1
    else:
        a+=1
