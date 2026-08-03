li=[20,10,30,15,30,40]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)
