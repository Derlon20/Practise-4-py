import math

def log():
    a,b=geta(),getb()
    if a==0 or b==0:
        return fail()
    return f"The logarithm of your numbers is {round(math.log(a,b),3)}"

def lg():
    b=getb()
    if b==0:
        return fail()
    return f"The decimal logarithm of your number is {round(math.log(10,b),3)}"

def ln():
    b=getb()
    if b==0:
        return fail()
    return f"The decimal logarithm of your number is {round(math.log(b),3)}"

def fail():
    print("Check: FAILURE")
    return("No issue") 

def geta():
    a = input("Enter A = ")
    try:
        a = float(a)
    except ValueError:
        a=0
        return a 
    a = float(a)
    if a<=0 or a==1:
        a=0
    return a

def getb():
    b = input("Enter B = ")
    try:
        b = float(b)
    except ValueError:
        b=0
        return b 
    b = float(b)
    if b<=0:
        b=0
    return b