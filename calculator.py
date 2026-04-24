#def calculator
def subtract(n,s):
    return n-s
def add(n,s):
    return n+s
def multiply(n,s):
    return n*s
def divide(n,s):
    if n==0:
        return "ERROR!division by 0"
    return n/s

#user input
number1=float(input("enter your first number:"))
number2=float(input("enter you second number"))
option=input("choose an option(+,-,*,/):")
    
#results
if option=="-":
    results=subtract(number1,number2)
    print (results)
elif option=="+":
    results=add(number1,number2)
    print(results)
elif option=="*":
    results=multiply(number1,number2)
    print(results) 
elif option=="/":
    results=divide(number1,number2)
    print(results)
else:
    results= ("invalid option ") 
    print("Results",results)         
