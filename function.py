def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b


# def addition(): <---------------followind Declaration also correct...
#     print("Additon -=",a+b)
# addition()


a=int(input("Enter Num1:-"))
b=int(input("Enter Num2:-"))

print("Addition-:",add(a,b))
print("Subtraction-:",sub(a,b))
print("Multification-:",mul(a,b))
print("Division-:",div(a,b))
print("Modular Division-:",mod(a,b))