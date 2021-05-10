def cityInDictinary ( cities, city):
    print("The country is: " + cities[city]['country'])
    print("The population is: " + str(cities[city]['population']))
    print("Here is a fun fact: " + cities[city]['fact'] + "\n" + "........................")


cities = {
    'New York': {'country': "USA", 'population': 5000000, 'fact':"its also known as the big apple"},
    "Los Angeles": {'country': "USA", 'population': 5600000, 'fact':"it is a cool place"},
    "Texas": {'country': "USA", 'population': 7000000, 'fact':"people think cowboys are there"},
}
for city in cities:
    print(city)
    cityInDictinary(cities, city)



