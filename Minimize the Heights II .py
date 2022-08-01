# Minimize the Heights II 
k=int(input("Enter the value of k: "))
n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    a.append(int(input("Enter the height of tower: ")))
print("Array is: ",a)
p=[]
for i in range(len(a)):
    if(a[i]<=k):
        p.append(a[i]+k)
    else:
        p.append(a[i]-k)
ans=max(p)-min(p)
print("The minimum possible difference the height of shortest and tallest tower is: ",ans)
