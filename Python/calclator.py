#for addition
def add(a,b):
	return a+b

# for subtraction
def sub(a,b):
	return a-b


#for multiplication
def mul(a,b):
	return a*b


#for division
def div(a,b):
	return a/b


if __name__=="__main__":
	print("select operation")
	print("1 : addition")
	print("2 : subtraction")
	print("3 : multiplication")
	print("4 : division")

	choice=int(input("Enter your choice"))

	n=int(input("Enter first number"))
	m=int(input("Enter second number"))
	if choice==1:
		print(n,"+",m,"=",add(n,m))

	elif choice==2:
		print(n,"-",m,"=",sub(n,m))

	elif choice==3:
		print(n,"*",m,"=",mul(n,m))

	elif choice==4:
		print(n,"/",m,"=",div(n,m))
	else:
		print("Invalid operation")

	
