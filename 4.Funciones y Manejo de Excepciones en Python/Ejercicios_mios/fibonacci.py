def fibonacci(f):
    if f == 0:
        return [0]
    elif f == 1:
        return [0,1]
    else:
        serie = fibonacci(f-1)
        serie.append(serie[f-1] + serie[f-2])
        return serie
    
fibonacci_6 = print(fibonacci(8))
