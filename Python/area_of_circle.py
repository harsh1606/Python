#Python program for find area of a circle

def area(r):
	return 3.14*(r*r)

if __name__=="__main__":
	r=float(input("Enter Radius"))
	print("area of circle is",area(r))