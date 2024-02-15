"""
#lambda function with multiple arguments

x = lambda a, b, c : a+b+c

print(x(5,10,15))
"""
def my_function(n):
    return lambda a: a * n

result = my_function(2) 
print(result(10))
