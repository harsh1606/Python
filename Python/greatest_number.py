#python program to find greater number between three number
def maximum(a, b, c): 
    list = [a, b, c] 
    return max(list) 
  
a=float(input("Enter first number "))
b=float(input("Enter second number "))
c=float(input("Enter third number "))
print(maximum(a, b, c)) 
    
