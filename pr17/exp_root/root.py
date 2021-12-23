def root2():
    n = input("Enter N = ")
    try:
        n = float(n)
    except ValueError:
        return fail()
    n = float(n)
    if n<0:
        return fail()
    else:
        return f"The square root of your number is {round(n**(1/2),3)}"

def root3():
    n = input("Enter N = ")
    try:
        n = float(n)
    except ValueError:
        return fail()
    n = float(n)
    if n>0:
        return f'The cube root of your number is {round(n**(1./3.),3)}'
    else:
        return f'The cube root of your number is {round(-(-n)**(1./3.),3)}'

def fail():
    print("Check: FAILURE")
    return("No issue") 
