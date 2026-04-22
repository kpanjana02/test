num1=int(input())
num2=int(input())
print("Enter 1 for addition\n Enter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division")
choice=int(input())
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invalid")