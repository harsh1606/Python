#Swap two number without third variable

def swap(a,b):
	a=a+b
	b=a-b
	a=a-b
	return a,b
if __name__== '__main__':
	x=int(input("Enter your first number"))
	y=int(input("Enter your second number"))
	print("value of x is ",x," and y is ",y,"before swaping")
	x,y=swap(x,y)
	print("value of x is ",x," and y is ",y,"after swaping")

	
	