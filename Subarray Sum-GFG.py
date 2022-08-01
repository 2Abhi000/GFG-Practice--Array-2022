# Subarray Sum-GFG
n=int(input('Enter the size of array: '))
ar=[]
d={}
for i in range(n):
    ar.append(int(input('Enter the elements in array: ')))
s=int(input("Enter the sum: "))
a=[]
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        o=ar[i]+ar[j]
        d[o]=(i,j)
for i in d:
    if(s==i):
        print(d[s])
