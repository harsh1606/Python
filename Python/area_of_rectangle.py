#python program for find area of a rectangle

def area(a,b):
	return a*b

if __name__=='__main__':
	l=float(input("Enter length of rectangle"))
	b=float(input("Enter breadth of rectangle"))
	print("Area of rectangle is",area(l,b))

	