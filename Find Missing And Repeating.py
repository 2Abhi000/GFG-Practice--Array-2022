#Find Missing And Repeating
n=int(input("Enter the size of array1: "))
a=[]
t=[]
d={}
for i in range(n):
    a.append(int(input("Enter the value: ")))

for i in a:
    d[i]=a.count(i)
for i in d:
    if(d[i]>1):
        t.append(i)
for i in range(1,len(a)+1):
    if(i not in a):
        t.append(i)
for i in t:
    print(i,end=' ')
