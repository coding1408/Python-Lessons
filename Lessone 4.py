currentNumber=1
while currentNumber <= 10:
    print (currentNumber)
    currentNumber+=1

prompt="\n please enter the name of a city"
prompt+="\n (enter ' quit ' when you are finished)"
while True:
    city=input(prompt)
    if city == 'quit':
        break
    else:
        print ("wow i love "+ city.title()+"!")


currentNumber = 0
while currentNumber <= 10:

    currentNumber +=1
    if currentNumber % 2 == 1: #if there is a reminder of 1
        continue
    print(currentNumber

