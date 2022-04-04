
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations={"+": add,
           "-": subtract,
           "*": multiply,
           "/": divide
           }

repeat=True
while repeat:
    for x in operations:
        print(x)

    op=input('enter your operation')
    num1=float(input('enter first number'))
    num2=float(input('enter second number'))

    function=operations[op]
    ans=function(num1,num2)

    print(f'{num1}  {op}  {num2} = {ans}')

    choice=input(f"do you want to continue yes\ no ")
    if choice== 'no':
        repeat=False

