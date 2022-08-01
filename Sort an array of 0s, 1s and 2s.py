#Sort an array of 0s, 1s and 2s 

n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    a.append(int(input("Enter the element: ")))
a.sort()
print("Array is: ",a)
