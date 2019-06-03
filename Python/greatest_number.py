#python program to find greater number between three number
def gre(a,b,c):
    if (a>b) and (a>c):
        print(f'{a} is greatest number')
    elif (b>c):
        print(f'{b} is greatest number')
    else:
        print(f'{c} is greatest number')


if __name__=='__main__':
    a=float(input("Enter first number "))
    b=float(input("Enter second number "))
    c=float(input("Enter third number "))
    gre(a,b,c)
    