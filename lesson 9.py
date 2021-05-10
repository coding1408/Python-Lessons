import matplotlib.pyplot as plt
import random

def randomArray():
    arr = []
    for i in range(100):
        arr.append(random.randint(-10, 10))
    return arr

def positive_negative(ar):
     negative = 0
     positive = 0
     zero = 0
     for i in ar:
         if i > 0:
             positive += 1
         elif i < 0:
             negative += 1
         else:
             zero += 1

     labels = 'Positive #', 'Negative #', "Zero #"
     sizes = [positive, negative, zero]
     explode = [0, 0, 0]

     fig1, graph1 = plt.subplots()
     graph1.pie(sizes, explode = explode, labels = labels, autopct='%1.1f%%', shadow = True, startangle= 90)
     graph1.axis('equal')
     plt.show()


if __name__== '__main__':
    arr =randomArray()
    print(arr)
    #test = [0,0, 0 ,0, 0, 0,0,0,0, 1]
    positive_negative(arr) #try it with test instead of arr
