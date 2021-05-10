lis =[ ]
for i in range(1, 26):
  lis.append(i)
  print (lis)
for i in range(1,25):
  del lis [len(lis) - 1]
  print (lis)

answer = int(input("whats 10 + 10? "))
if answer == 20:
    print( "You got it correct!")
elif answer == 100:
    print("you did muliplication instead of addition")
elif answer ==1:
    print("you did divsion instead of addition")
elif answer > 100 and answer < 150:
    print ("study harder")
else:
    print("you got it wrong")

print("-----------------------------------")

# ask the user their age
#if they are 4 or younger they get in for free
# if they are less than 12 thenthey get in for 6 dollars (you have to pay 6 dollars)
#if they are between 12 and 65 they have to pay 12
#if they are over 65 they have to pay 6
#if they are over 100 you give them a dollar

age = int(input("whats your age? "))
if age < 0 or age >=120:
    print("stop lying")
elif age <= 4:
    print ("you can get it for free but bring a parent next time")
elif age < 13:
    print ( "itll be six dollars")
elif age <= 65:
    print ("that'll be twelve dollars")
elif age <100:
    print ("that'll be six dollars")
else:
    print (" here, take a dollar ")
