import unittest

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

def handler_name(event, context): 
    num = int(event["num"])
    if num < 0:
        raise ValueError("Number must be a positivie integer")
    return fibonacci(num)


