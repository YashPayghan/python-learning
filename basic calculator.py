def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def main():
    n1=float(input("what's the first number?\n "))
    b="""
    +
    -
    *
    /
    """
    print(b)
    c=input("pick an operetor :")

    n2=float(input("what's the second number?\n "))

    if c=="+":
        print(n1,c,n2,"=",add(n1,n2))
    elif c=="-":
        print(n1,c,n2,"=",subtract(n1,n2))
    elif c=="*":
        print(n1,c,n2,"=",multiply(n1,n2))
    elif c=="/":
        print(n1,c,n2,"=",divide(n1,n2))
    else:
        print("enter a valid operetor")
main()
d=input("do you want to continue calculating(YES/NO)?\n").lower()
while d=="yes":
    main()