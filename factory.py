enter = int(input("Enter a number for factorial: "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(enter))
