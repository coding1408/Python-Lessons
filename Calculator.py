def addition(a, b):
    c = a + b
    return c

def subtration(a, b):
    c = a - b
    return c

def multiplication (a, b):
    c = a * b
    return c

def division (a, b):
    c = a / b
    return c

if __name__ == "__main__":
 print("Type quit at sign selection to quit")
 while True:
    number1 = int(input(" pick a number: "))

    number2 = int(input(" pick another number: "))
    
    sign = input("What sign (add, sub, div, mult): " )
    if sign == "quit":
        break
    if sign == "add" or sign=="+":
         answer = addition(number1, number2)
    elif sign == "sub" or sign =="-":
         answer = subtration(number1, number2)
    elif sign == "div" or sign == "/":
         answer = division(number1, number2)
    elif sign == "mult" or sign == "*":
         answer = multiplication(number1, number2)
    else:
         answer =  "Error, you either put a none int number or wrong spelling on sign"

    print(answer)

 print("you broke")

