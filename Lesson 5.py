codingGlossary = {
    'append' : 'add to the end of the list',
    'sort': 'sorts in alph. order',
    'range': 'lets you pick a range of numbers',
    'for': ' a loop that repeats an action',
    'print': 'shows on screen'
}

print(codingGlossary)
print(codingGlossary['append'] +"\n")

for key in codingGlossary:
    # print #prints the key only
    # print(codingGlossary[key]) #prints the value of the key
    print(key+ ": " + codingGlossary[key] )
print("\n")

cities = {
    'New York': {'country': "USA", 'population': 5000000, 'fact':"its also known as the big apple"},
    "Los Angeles": {'country': "USA", 'population': 5600000, 'fact':"it is a cool place"},
    "Texas": {'country': "USA", 'population': 7000000, 'fact':"people think cowboys are there"},
}
print (cities)
print (cities['New York'])
print (cities['Los Angeles']['population'] )
print("\n")
print("........................")
for city in cities:
    print(city)
    if city == "New York":
        print("The country is: " +cities[city]['country'])
        print("The population is: " + str(cities[city]['population']))
        print("Here is a fun fact: "+ cities[city]['fact'] + "\n" + "........................")
    elif city == "Los Angeles":
        print("The country is: " + cities[city]['country'])
        print("The population is: " + str(cities[city]['population']))
        print("Here is a fun fact: " + cities[city]['fact'] + "\n" + "........................")

    elif city == "Texas":
        print("The country is: " + cities[city]['country'])
        print("The population is: " + str(cities[city]['population']))
        print("Here is a fun fact: " + cities[city]['fact'] + "\n" + "........................")
        # howwork do the rest (texas)
         #we do not need if statments look at lesson 5b


