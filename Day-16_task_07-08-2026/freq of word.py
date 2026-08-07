st='python is easy python is fun'
temp=''
lis=[]
dic={}
for i in st:
    if i!=' ':
        temp+=i
    else:
        lis.append(temp)
        temp=''
    if i==st[len(st)-1]:
        lis.append(temp)
for i in lis:
    dic[i]=dic.get(i,0)+1
print(dic)
