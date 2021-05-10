import random

def partialyPi(dots):
    dotsCircle = 0
    dotsSquare = 0
    xArray = []
    yArray = []

    for i in range(dots):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        xArray.append(x)
        yArray.append(y)
        distance = (x**2+y**2)**0.5
        dotsSquare = dotsSquare + 1
        if distance <= 1:
            dotsCircle = dotsCircle + 1 # dotsCircle += 1

        print(xArray)
        print(yArray)
    return 4 * dotsCircle/dotsSquare

if __name__== '__main__':
    a=partialyPi(1000)
    print(a)