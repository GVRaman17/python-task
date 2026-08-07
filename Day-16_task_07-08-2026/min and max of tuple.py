tu=(5,3,6,7,8,1,2,9)
max=tu[0]
min=tu[0]
for i in tu:
    if max<i:
        max=i
    if min>i:
        min=i
print('the max no:',max)
print('the min no:',min)
