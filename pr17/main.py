from factorial import fact
from exp_root import root, exponentiation
from logarithm import log

print("First you begin, you should know how to call on math func you need\nEnter:\n     fact - if you want to calculate factorial\n     exp2 - if you want to calculate square of the number\n     exp3 - if you want to calculate cube of the number\n     root2 - if you want to calculate square root\n     root3 - if you want to calculate cube root\n     log - if you want to calculate logarithm\n     ln - if you want to calculate natural logarithm\n     lg - if you want to calculate decimal logarithm\n     end - if you want to end work of this programm")

def main():
    print("- "*12, "</||\>", " -"*12)
    name=str(input("Enter what you want to find: "))
    while name != "fact" and name != "root2" and name != "root3" and name != "exp2" and name != "exp3" and name != "log" and name != "ln" and name != "lg" and name != "end":
        name = input("ERROR.  Enter what you need to find again: ")
    if name=="fact":
        dist="fact"
    elif name=="root2" or name=="root3":
        dist="root"
    elif name=="exp2" or name=="exp3":
        dist="exponentiation"
    elif name=="log" or name=="ln" or name=="lg":
        dist="log"
    elif name=="end":
        print("Sayoonara, Bentley-san")
        raise SystemExit
    print(eval(f"{dist}.{name}")())
    main()

if __name__ == '__main__':
    main()
