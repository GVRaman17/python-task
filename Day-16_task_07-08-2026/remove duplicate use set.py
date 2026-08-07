n=int(input("enter the count of the list: "))
lis=[]
for i in range(n):
    temp=int(input("val:"))
    lis.append(temp)
lis=list(set(lis))
print("here the removed duplicate")
print(lis)
