with open('savedDataErased.txt') as file:
    for line in file:
        values = line.split(',')

    values[2] = "3"

    with open('savedDataErased.txt', 'w') as file:
        for i in values:
            file.writelines(i)
            file.writelines(",")

    file.close()