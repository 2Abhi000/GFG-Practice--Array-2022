#Majority Element

n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    a.append(int(input("Enter the element: ")))
a.sort()
d={}
for i in a:
    d[a.count(i)]=i
m=max(d)
print("Majority Element is: ",d[m])
