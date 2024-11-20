def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

operators={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}
def calculator():
    num1=float(input("Whats the first number?: "))
    for symbol in operators:
            print(symbol)
    should_continue=True
    while should_continue:
        operation=input("pick an operation from above:")#operation selected
        num2=float(input("What the next number?: "))

        calculation=operators[operation] #operation inside the operator is selected
        answer=calculation(num1,num2)#answer stored here
        print(f"{num1}{symbol}{num2} = {answer}") 

        if input("if you wish to continue the press 'y' to start new calculation press 'n' ")=="y":
            num1=answer #the new num1 is the answer we got from the operation before
        else:
            should_continue=False
            calculator()
calculator()

