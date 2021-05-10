import matplotlib.pyplot as plt
import random

def randomGoalsPerGame(gamesPlayed):
    goalsList = []
    for i in range(gamesPlayed):
        goalsInOneGame = random.randint(0,4)
        goalsList.append(goalsInOneGame)
    return goalsList

def numberOfGamesArray(gamesPlayed):
    numberOfGames = []
    for i in range(gamesPlayed+1):
        if i > 0:
            numberOfGames.append(i)

    return numberOfGames

def graph(x,y):
    plt.plot(x,y,marker = 'o')
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel("Messi Games Played")
    plt.ylabel("Goals Scored")
    plt.title("Messi's Games Played vs. Goals Scored")

    plt.show()

if __name__ == '__main__':
    gamesPlayed = int(input("Amount of games Messi played: "))
    x = numberOfGamesArray(gamesPlayed)
    y = randomGoalsPerGame(gamesPlayed)
    print(x)
    print(y)

    goals = 0
    for i in y:
        goals = goals + i

    avg = goals / gamesPlayed
    print(avg)

    graph(x,y)



