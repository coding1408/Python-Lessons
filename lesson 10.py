import matplotlib.pyplot as plt

def graph(x,y):
    plt.plot(x,y, marker = 'X')
    plt.xlabel('Distance between the Masses')
    plt.ylabel('Gavitational Force')
    plt.title('The relationship between the force vs Distances')
    plt.show()

def gravLaw():
    F = []
    G = 6.674*(10**-11)
    M1 = 3
    M2 = 1
    r = range(100, 1001, 50)
    for distance in r:
        force = G * M1 * M2 / (distance ** 2)
        F.append(force)


    graph(r, F)


if __name__== '__main__':
    gravLaw()
