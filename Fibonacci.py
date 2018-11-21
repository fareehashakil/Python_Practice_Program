# Object:
#     To print fibonacci series.

# Source Code:
def fib(n):
    a = 0
    b = 1
    if n == 0:
        pass
    elif n == 1:
        print(a)
    elif n == 2:
        print(a , b)
    else:
        print(a , b , end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b , end = " ")

fib(int(input("Enter no: ")))
