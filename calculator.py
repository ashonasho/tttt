def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def mod(x,y):
    return(x%y)

def select_choice(choice):
    if(choice=="+"):
        print(add(x,y))
    elif(choice=="-"):
        print(sub(x,y))
    elif(choice=="*"):
        print(multiply(x,y))
    elif(choice=="/"):
        print(div(x,y))
    elif(choice=="%"):
        print(mod(x,y))
    else:
        print("Invalid option")


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    choice=input("please enter your arithmetic operator : ")
    if(choice=="#"):
       break
    elif(choice=="$"):
        continue
    else:
        x=int(input("please enter number 1 : "))
        y=int(input("please enter number 2 : "))
        select_choice(choice)