a=int(input("Enter Number 1:-"))
b=int(input("Enter Number 2:-"))
print("-----------------------------------------OPTIONS--------------------------------------------")
print("1.Addition \t 2.Subtraction \t 3.Multification \t 4.Division \t 5.Modular Division")
print("--------------------------------------------------------------------------------------------")
choice=input(" 1 For Addition \n 2 For Subtraction \n 3 For Multification \n 4 For Division \n 5 For Modular Division------>")

if(choice=="1"):
    print("Addition of",a,"And",b,"=",a+b)
elif(choice=="2"):
    print("Subtraction of",a,"And",b,"=",a-b)
elif(choice=="3"):
    print("Multification of",a,"And",b,"=",a*b)
elif(choice=="4"):
    print("Division of",a,"And",b,"=",a/b)#int value automatically convert into Float value
elif(choice=="5"):
    print("Modular Division of",a,"And",b,"=",a%b)
else:
    print("Invalid Input.")