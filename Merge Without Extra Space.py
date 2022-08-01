#Merge Without Extra Space
n=int(input("Enter the size of array1: "))
a=[]
b=[]
for i in range(n):
    a.append(int(input("Enter the value: ")))
m=int(input("Enter the size of array2: "))
for j in range(m):
    b.append(int(input("Enter the value: ")))

a=a+b
a.sort()
print(a)
