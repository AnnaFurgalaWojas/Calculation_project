def add_function(a,b):
    if not int(a) or not int(b):
        return ValueError('NO NUMBERS, TRY AGAIN')
    return a+b

def divide_function(a,b):
    if not int(a) or not int(b):
        return ValueError('NO NUMBERS, TRY AGAIN')
    return a/b

def mean_function (numbers):
    if not numbers:
        return ValueError('NO NUMBERS, TRY AGAIN')
    return sum(numbers)/len(numbers)