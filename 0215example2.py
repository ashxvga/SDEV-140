"""
#lambda function with multiple arguments

x = lambda a, b, c : a+b+c

print(x(5,10,15))
"""
def my_function(n):
    return lambda a: a * n

result = my_function(2) #gives a value to n
print(result(10)) #gives a value to a
