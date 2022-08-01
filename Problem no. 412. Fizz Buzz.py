# Problem no. 412. Fizz Buzz
n=15
a=[]
for i in range(1,n+1):
    if(i%3==0):
        a.append("Fizz")
    if(i%5==0):
        a.append("Buzz")
    if(i%3 == 0 and i%5==0):
        a.append("FizzBuzz")
    else:
        a.append(str(i))
#a.sort()
print(a)
