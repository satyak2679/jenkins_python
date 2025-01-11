import math
from collections import Counter
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
def square(a):
    return a*a
def mean(data):
    return sum(data)/len(data)
def median(data):
    n = len(data)
    index = (n) // 2
    if n % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index - 1:index + 1]) / 2.0
def mode(data):
    c=Counter(data)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]