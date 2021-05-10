#ATM
#People -names
#Pins
#Credit Card or ID
#Money - withdraw/dep


peopleID = [1234, 5678, 9812 ]
pinsID = [1111, 2222, 3333]
names = ["Michael", "Ivan", "Jessica"]
money = [10, 50, -10]

cardInfo ={
    peopleID[0]: {'pin': pinsID[0], 'money': money[0], 'name':names[0]},
    peopleID[1]: {'pin': pinsID[1], 'money':money[1], 'name':names[1]},
    peopleID[2]:{'pin': pinsID[2], 'money':money[2], 'name':names[2]},
    #for homework try using a for loop instead
    #for sdhkajsdhakj in range(something) range(0,3)
    #optinal
}

print("Welcome to Aiden's Bank ")
while True:
 inputedID = int(input("\n Please put in your ID: "))

#if the person put in the id of 1234 i want the program to ask them to put in their id and only let them in if the pin is 1111
 i = 1
 for x in cardInfo: #later change the  x to ID
   i = i + 1 #note to yaron we need this for the end line 64 in yarons code
   if  inputedID == x:
       inputedPin = int(input("Please provide pin: "))

       if inputedPin ==  cardInfo[inputedID]['pin']:
           print("Welcome " +  cardInfo[inputedID]['name'])
           print("Balance: $" + str(cardInfo[inputedID]['money']))
           inputAction = input("Do you want to withdraw (w) or deposit (d): ")
           inputAction = inputAction.lower()

           if inputAction == "withdraw" or inputAction =="w":
               moneyOut = int(input("How much money would you like to withdraw?: $"))
               if moneyOut < 0:
                   print("Not valid amount of money.")
                   break
               if moneyOut > cardInfo[inputedID]["money"]:
                   print("You dont have enough money in your account")
               else:
                   cardInfo[inputedID]["money"] = cardInfo[inputedID]["money"] - moneyOut
                   print("you currently have $" + str(cardInfo[inputedID]["money"]))
                   break

           elif inputAction == "deposit" or inputAction=="d":
               moneyIn = int(input("How much money would you like to deposit?: $"))
               if moneyIn < 0:
                   print("Not valid amount of money.")
                   break
               cardInfo[inputedID]["money"] = cardInfo[inputedID]["money"] + moneyIn
               print("you currently have $" + str(cardInfo[inputedID]["money"]))
               break

           else:
               print("You either don't know it or might need to check your spelling")

       else:
           print("It's either that you put in the wrong pin or that your a scammer, if so shame on you.")

   elif i > (len(peopleID)):
       print("This number doesnt work. ")
       i = 1



#Review review review , at least 5 times







