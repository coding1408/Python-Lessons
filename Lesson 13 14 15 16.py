def displayContacts(txtFile):
    with open(txtFile) as file:
        for line in file:
            values = line.split(',')

    return values

def contactSaver(object, txtFile):
    with open(txtFile, "a") as file:
        file.writelines((object))
        file.writelines(",")
    file.close()

def contactUpdater(txtFile, count, updatedInfo):
    allContacts = displayContacts(txtFile)
    if updatedInfo == "del":
        del allContacts[count]
    else:
        allContacts[count]=updatedInfo

#    with open(txtFile, "w") as file: #TO BE COMPLETED

addressBook = ('''1) Add contact
2) Update contact
3) Display all contacts
4) Search a contact
5) Delete contact
6) Quit''')
print(addressBook)

quit = (False)

phoneNumbers = []
names = []

while quit == False:
    userSelection = int(input("\nWhat option: "))
    if userSelection == 1:
        name = input("What's your name and by the way i have candy in the white van behind you: ")
        phoneNumber = input("What's your phone number: ")
        # names.append(name)
        # phoneNumbers.append(phoneNumber)
        # print("\nYour contact has been added: " + name +" "+ phoneNumber)

        contactSaver(name,'names.txt')
        contactSaver(phoneNumber, 'contacts.txt')

    elif userSelection == 2:
        print(phoneNumbers)
        searchedNumber = input("Which phone would you like to update: ")
        count = (0)
        newChecker =False
        for number in phoneNumbers:
            if number == searchedNumber:
                print("worked")
                newNumber = input("Whats your new number: ")
                newName = input("What is the new name: ")
                newChecker = True
            else:
                count += 1


        if newChecker == True:
            names[count] = newName
            phoneNumbers[count] = newNumber
            newChecker = False
        else:
            print("No such phone number!")

    elif userSelection == 3:
        names =  displayContacts("names.txt")
        contacts = displayContacts("contacts.txt")
        print(names)
        print(contacts)
        #count = 0
        # for i in names:
        #     print(i + ": " + phoneNumbers[count])
        #     count += 1

    elif userSelection == 4:
        found = False
        searchedNumber = input("Which phone would you like to search: ")
        # count = (0)
        # for number in phoneNumbers:
        #     if number == searchedNumber:
        #         print("The name is: " + names[count])

            # else:
            #     count += 1

        contactList = displayContacts('contacts.txt')

        for i in contactList:

            if i == searchedNumber:
                found = True
                print("found it")

        if found == False:
                print("can't find it")


    elif userSelection == 5:
        deletedNumber = input("Which phone number would you like to delete: ")
        count = (0)
        for number in phoneNumbers:
            if number == deletedNumber:
                print("The deleted name is: " + names[count])
                print("The deleted number is: " + phoneNumbers[count])
                del phoneNumbers[count]
                del names[count]


            else:
                count += 1


    elif userSelection == 6:
        quit = True
        print("You're a quiter")

    else:
        print("Not a Valid Option!")