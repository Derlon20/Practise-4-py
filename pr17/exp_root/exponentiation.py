def exp2():
    n = input("Enter N = ")
    try:
        n = float(n)
    except ValueError:
        return fail()
    n = float(n)
    return f"The square of your number is {round(n**2,3)}"

def exp3():
    n = input("Enter N = ")
    try:
        n = float(n)
    except ValueError:
        return fail()
    n = float(n)
    return f"The cube of your number is {round(n**3,3)}"

def fail():
    print("Check: FAILURE")
    return("No issue") 