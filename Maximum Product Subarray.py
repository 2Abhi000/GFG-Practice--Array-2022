#Maximum Product Subarray
a=[2, 3, 4, 5, -1, 0]
k=[]


for i in range(len(a)):
    p=1
    for j in range(i,len(a)):
        p=p*a[j]
        k.append(p)
print(max(k))
