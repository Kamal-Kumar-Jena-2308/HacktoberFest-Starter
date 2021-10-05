import time
while True:        
    k=[]
    a=int(input("Enter Your First Number\n=>"))
    b=int(input("Enter Your Second Number\n=>"))
    k.append(a)
    k.append(b)
    operator=int(input("To Add - Enter 1\nTo Subtract - Enter 2\nTo Multiply - Enter 3\nTo Divide - Enter 4\nENTER - "))
    c=int(k[0])
    d=int(k[1])
    if operator <= 0:
        if operator >= 5:
            print("Enter a valid operator")
            quit()
    else:
        if operator == 1:
            print("===================================\n===================================")
            print(f"The sum of {c} and {d} is", c+d)
        elif operator == 2:
            print("===================================\n===================================")
            print(f"The difference of {c} and {d} is", c-d)
        elif operator == 3:
            print("===================================\n===================================")
            print(f"The product of {c} and {d} is", c*d)
        elif operator == 4:
            print("===================================\n===================================")
            print(f"The quotient of {c} and {d} is", c/d)
    again=input("Enter 'y' to use again\nEnter 'n' to exit :- ")
    if again == 'y':
        continue
    else:
        print("Thanks For Using our Calculator\n|       |\n    |    \n \_____/  ")
        exit()