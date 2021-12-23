def fact():
    f=1
    n = input("Enter N = ")
    try:
        n = int(n)
    except ValueError:
        return fail()
    n = int(n)
    if n<0:
        return fail()
    elif n==0 or n==1:
        return f 
    else:
        for i in range(1,n+1):
            f=f*i
        return f'The factorial of your number is {f}'
def fail():
    print("Check: FAILURE")
    return("No issue") 
