def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

val = "Welcome to python"
print("10th fibonacci number: %i" %fib(10))
ivalue = int(raw_input("Please enter a number"))
print [fib(i) for i in range(ivalue)]
for i in range(ivalue):
   print fib(i)