##HOMEWORK
# comment on lines 1-3, 5-11, 14-19, 42-52, explain how each line works!

#READING THE DATA FROM  A TXT FILE
with open('savedData.txt') as file:#it will open the file
    print(file.readlines())#it will print the lines

with open('savedData.txt') as file:#it will open it again
    for line in file:#for every line in the file...
        values = line.split(',')#it will put a comma beetween each sentance/phrase
        print(values)#it will print the values

    for i in values:#for loop
        print(i)#prints i

#ADDING TO THE TXT FILE
somethingToAdd = "Chicken wings are for people who love turkeys"#what we are adding (could be anything)

with open('savedData.txt', "a") as file: #a is for append #it will append it as a file

    file.writelines((somethingToAdd))
    file.writelines(",")
file.close()

#WRITING TO A TXT FILE
with open('savedDataCopy.txt', "w") as file: #w is for write
    file.write(("HAHA I Erased everything!,"))
file.close()

#Eraseing an element in a TXT File
with open('savedDataErased.txt') as file:
    for line in file:
        values = line.split(',')

    del values[2]

    with open('savedDataErased.txt', 'w') as file:
        for i in values:
            file.writelines(i)
            file.writelines(",")

    file.close()

#Updating an elemnt in a Txt File

with open('savedDataUpdate.txt') as file:#it will open it as a file
    for line in file:#for loop
        values = line.split(',')#it will put a comma beetween each phrase/sentance

    values[2] =" I reallly reallllly adoreeee hotpink"#another message ( could be anything)

    with open('savedDataUpdate.txt', 'w') as file:#it will open it as w (i forgot what w means)
        for i in values:#for loop
            file.writelines(i)
            file.writelines(",")
    file.close()