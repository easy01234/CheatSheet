def is_fibonacci(n):
    a,b=0,1
    while b<=n:
        a,b=b,a+b
        if a==n:
            return True 
    return False
n=int(input("Enter a number: "))
if is_fibonacci(n):
    print(n, "is a fibonacci number: ")
else:
    [print(n, "is not a fibonacci number.")]
    