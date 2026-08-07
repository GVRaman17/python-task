li=['David','Alice','Emma','Bob','John']
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)
    
