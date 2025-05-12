#Fibonacci Number

n=int(input("Enter n to find nth fibonacci number : "))
if(n<=0):
    print("Enter a valid n value")
elif(n==1):
    print("1st fibonacci number is : 0")
else:
    a=0
    b=1
    for i in range (2,n):
        c=a+b
        a=b
        b=c
    print(f"{n}th fibonacci number is : {c}")