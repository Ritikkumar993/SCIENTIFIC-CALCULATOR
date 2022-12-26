import  math
def add():
    num1=float(input("Enter the 1 number: "))
    num2=float(input("Enter the 2 number :"))
    print(num1+num2)
def sub():
    num1=float(input("Enter the 1 number: "))
    num2=float(input("Enter the 2 number :"))
    print(num1-num2)
def mul():
    num1=int(input("Enter the 1 number: "))
    num2=int(input("Enter the 2 number :"))
    print(num1*num2)
def mod():
    num1=int(input("Enter the 1 number: "))
    num2=int(input("Enter the 2 number :"))
    print(num1%num2)
def squar():
    num1 = int(input("Enter the 1 number: "))
    print(num1**(1/2))
def expo():
    num1=int(input("Enter the 1 number: "))
    num2=int(input("Enter the 2 number :"))
    print(num1**num2)
def sin():
    num1 = int(input("Enter the degre: "))
    print(math.sin(num1))
def cos():
    num1 = int(input("Enter the degre: "))
    print(math.cos(num1))
def tan():
    num1 = int(input("Enter the degre: "))
    print(math.tan(num1))
def rad_to_deg():
    num1 = float(input("Enter the rad: "))
    print(math.degrees(num1))
def deg_to_rad():
    num1 = float(input("Enter the deg:"))
    print(math.radians(num1))
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. MOD")
print("5. SQUARE ROOT")
print("6. EXPONENT")
print("7. SIN")
print("8. COS")
print("9. TAN")
print("10.RAD_TO_DEG")
print("11.DEG_TO_RAD")
print("12.EXIT")
while True:
    a=int(input("ENTER YOUR CHOISE:"))
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        mul()
    elif a==4:
        mod()
    elif a==5:
        squar()
    elif a==6:
        expo()
    elif a==7:
        sin()
    elif a==8:
        cos()
    elif a==9:
        tan()
    elif a==10:
        rad_to_deg()
    elif a==11:
        deg_to_rad()
    elif a==12:
        exit()
    else:
        print("YOU HAVE ENTER THE WRONG NUMBER")
        print("PLEASE TRY AGAIN")




