#fuction recursion - a function calling itself
#countdown recursion

def tri(k):
    print(k)
    if k > 0:
        tri(k-1)
#tri(0) #only prints 0
tri(12)