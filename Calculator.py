print("Calculator\nSelect Type of calculator")
cal=int(input("Press 1 for Arithmetic calculator\nPress 2 for Logical calculator\nPress 3 for Comparison Calculator"))
if cal==1:

    a=int(input("Enter 1st number "))
    b=int(input("Enter 2nd number "))
    
    op=int(input("Press 1 for addition \nPress 2 for subtraction \nPress 3 for Multiplication \nPress 4 for Divison "))

    if op==1:
        print("Addition of given number"+a+" "+b+"=",a+b)
    
    elif op==2:
        print("Subtraction of given number"+a+" "+b+"=",a-b)
    
    elif op==3:
        #c=a*b
        print("Multiplication result of given numbers",a*b)
        
    else:
        #d=int(a/b)
        print("Division of given numbers",a/b)

elif cal==3:
    
    a=int(input("Enter 1st number "))
    b=int(input("Enter 2nd number "))
    
    op1=int(input("Press 1 for checking if 1st no. greater than 2nd no. \nPress 2 for checking if 2nd no. greater than 1st no. \nPress 3 for equality of both input numbers \nPress 4 for non-equality of both input"))

    if  op1 ==1:
        print(a>b)

    elif op1==2:
        print(a<b)

    elif op1==3:
        print(a==b)

    else :
        print(a!=b)

        

        
                        
