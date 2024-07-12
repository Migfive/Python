def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    

factorial_5= print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

resultado = print(fibonacci(5))