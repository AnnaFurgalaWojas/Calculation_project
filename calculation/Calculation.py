def add_function(a,b):
    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        raise ValueError('NO NUMBERS, TRY AGAIN')
    return a+b

def divide_function(a,b):
    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        raise ValueError('NO NUMBERS, TRY AGAIN')
    if b==0:
        raise ValueError ("You Can not divide by 0")
    return a/b

def mean_function (numbers):
    if not numbers:
        raise ValueError('NO NUMBERS, TRY AGAIN')
    return sum(numbers)/len(numbers)