import math

def addition(a,b):
    return a+b

def product(a,b):
    return a*b
    
def substraction(a,b):
    return a-b
    
def division(a,b):
    if b!=0:
        return a/b
    else:
        None
        
def module(a,b):
    m=math.sqrt(a**2+b**2)
    return m
       

if __name__=='__main__':
    a=3.0
    b=4.0
    print(addition(a,b))
    print(product(a,b))
    print(substraction(a,b))
    print(division(a,b))
    print(module(a,b))
