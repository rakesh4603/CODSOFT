print("----------Simple Calculator----------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo")
choice=int(input("Enter your choice:"))
if choice>5:
    print("enter a valid choice")
else:
    first_value=int(input("Enter 1st value:"))
    second_value=int(input("Enter 2nd value:"))
    if choice==1:
        print("result is",first_value+second_value)
    elif choice==2:
        print("result is",first_value-second_value)
    elif choice==3:
        print("result is",first_value*second_value)
    elif choice==4:
        print("result is",first_value/second_value)
    elif choice==5:
        print("results is",first_value%second_value)
    