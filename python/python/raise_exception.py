a=int(input("enter 1 number : "))
b=int(input("enter 2 number : "))

if(b==0):
    raise ZeroDivisionError("zero is not allow") #it will raise custom error and will crash program
else:
    print("division of a and b : ",a/b)

#any number can not be divide by zero