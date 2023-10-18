import calculatorModel as mapp

def eventAdd(a,b):
    addition=mapp.addition(a,b)
    return addition
     

def eventSubst(a,b):
    substraction=mapp.substraction(a,b)
    return substraction

def eventMultiply(a,b):
    product=mapp.product(a,b)
    return product
    

def eventDivide(a,b):
    division=mapp.division(a,b)
    return division
    
def eventModule(a,b):
    module=mapp.module(a,b)
    return module

