def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print(factorial(5))


def fibonacci(f):
    serie = []
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
       return fibonacci(f-1) + fibonacci (f-2)
    
fibonacci_6 = print(fibonacci(6))

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)
    
number = 5
print(suma_naturales(number))