import math

def log():
    return f"The logarithm of your numbers is {round(math.log(geta(),getb()),3)}"

def lg():
    return f"The decimal logarithm of your number is {round(math.log(10,getb()),3)}"

def ln():
    return f"The decimal logarithm of your number is {round(math.log(getb()),3)}"

def fail():
    print("Check: FAILURE")
    return("No issue") 

def geta():
    a = input("Enter A = ")
    try:
        a = float(a)
    except ValueError:
        return fail()
    a = float(a)
    if a<=0 or a==1:
        return fail()
    else:
        return a

def getb():
    b = input("Enter B = ")
    try:
        b = float(b)
    except ValueError:
        return fail()
    b = int(b)
    if b<=0:
        return fail()
    else:
        return b