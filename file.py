#Python program to add two numbers using function

def add_num(a,b):#function for addition
    sum=a+b;
    return sum; #return value

num1=int(input("Enter the number to add"))  #variable declaration
num2=int(input("Enter the number to add"))
print("The sum is",add_num(num1,num2))
