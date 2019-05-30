#python program for find the solution of quadratic equation ax**2+bx+c=0

import cmath
def qu_eq(a,b,c):
	d=(b**2)-(4*a*c)   #calculate the discriminant
	sol1=(-b-cmath.sqrt(d))/(2*a)
	sol2=(-b+cmath.sqrt(d))/(2*a)
	return sol1,sol2


if __name__ == '__main__':
	a=float(input("Enter the cofficient of x**2 "))
	b=float(input("Enter the cofficient of x "))
	c=float(input("Enter the constant term "))
	sol1,sol2=qu_eq(a,b,c)
	print(f"solution of quadic eq is {sol1} and {sol2}")

	