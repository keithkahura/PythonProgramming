
import operators
import others
import trigonometry
operator=input("enter an operator:")
if operator=="cube":
    num=eval(input("enter number:"))
    x = others.cube(num)
    print(x)
elif operator=="square":
    num=eval(input("enter number:"))
    x=others.square(num)
    print(x)
elif operator=="sine":
    angle=eval(input("enter angle:"))
    x= trigonometry.get_sine(angle)
    print(x)
elif operator=="tan":
    angle=eval(input("enter angle:"))
    x=trigonometry.get_tan(angle)
    print(x)
else:
    num1=eval(input("enter number 1:"))
    num2=eval(input("enter number 2:"))
if operator=="+":
    v=operators.addition(num1,num2)
    print(v)
elif operator=="-":
    v=operators.minus(num1,num2)
    print(v)
elif operator=="/":
    v=operators.divide(num1,num2)
    print(v)
elif operator=="*":
    v=operators.multiply(num1,num2)
    print(v)
elif operator =="X" or operator == "x" or operator =="*" :
    v=operators.multiply(num1,num2)
    print(v)
else:
    print("welcome!!!!")
