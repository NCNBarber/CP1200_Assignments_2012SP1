"""
CP1200 - Assignment 1, Part 2
Nicholas Barber 02/05/2012
The Great CP1200 Catering Calculator 2.0

Pseudocode: 

function main()
    MENU = menu text
    packageNames = blank list
    packagesData = empty map
    
    display Welcome
    
    get menuChoice
    repeat while menuChoice is not = to Q
        if menuChoice = I
            display Information                   
        otherwise if menuChoice = C
            check if the number of packages in memory = 0
                display "add or load packages first" message
            otherwise
                call calculateCatering(packageNames, packagesData)
        otherwise if menuChoice = D
            check if the number of packages in memory = 0
                display "add or load packages first" message
            otherwise
                call displayPackages(packageNames, packagesData)
        otherwise if menuChoice = L
            set packageNames, packagesData to loadPackages()
        otherwise if menuChoice = S
            call savePackages(packageNames, packagesData)
        otherwise if menuChoice = A
            set packageNames, packagesData to addPackage(packageNames, packagesData)   
        otherwise
            display "Invalid menu choice."
        get menuChoice
    display farewell message


function calculateCatering(packageNames, packagesData)
    get numberOfAdults
    repeat while numberOfAdults is invalid
        get numberOfAdults        
    get numberOfChildren
    repeat while numberOfChildren is invalid
        get numberOfChildren
    call displayPackages(packageNames, packagesData)
    get packageChoice
    repeat while packageChoice is invalid
        get packageChoice       
    set discountBonusChance as a random integer between 1 and 10 (inclusive)

    if discountBonusChance = 1    
	adultCost = chosen package's child price × numberOfAdults        
    otherwise
        adultCost = chosen package's adult price × numberOfAdults 
    childrenCost = chosen package's child price × numberOfChildren
    totalCost = adultCost + childrenCost

    if numberOfAdults = 1
        display "adult" instead of "adults" within catering cost statement
    otherwise
        display "adults" in catering cost statement
    if numberOfChildren = 1
        display "child" instead of "children" within catering cost statement
    otherwise
        display "children" in catering cost statement

    if discountBonusChance = 1    
        display catering cost statement with adults at children's prices
    otherwise
        display catering cost statement with adults at adult prices
          
 
function displayPackages(packageNames, packagesData)
    for each package
        display packageName, adultCost and childCost (in respect to each package)


function loadPackages(packagesFileName (Default: packages.txt))
    packageNames = blank list
    packagesData = empty map
    open packagesFileName as packagesFile for reading
    for each package in packagesFile
        get packageName from packagesFile
        get adultPrice from packagesFile
        get childPrice from packagesFile
        append packageName to packageNames
        add packageName to packagesData with the values for adultPrice and childPrice
    close packagesFile
    return packageNames, packagesData


function savePackages(packageNames, packagesData, packagesFileName (Default: packages.txt))
    textToSave = blank list
    for each package
        combine packageName, adultPrice and childPrice (in respect to each package) into a string
        add string to textToSave
    open packagesFileName as packagesFile for writing
    for each line in textToSave
        write line to packagesFile
    close packagesFile


function addPackage(packageNames, packagesData)    
    get packageName
    repeat while packageName is blank or packageName is greater than 16 characters long
        display invalid package name message
        get packageName
    get adultPrice
    repeat while adultPrice is invalid
        get adultPrice       
    get childPrice
    repeat while childPrice is invalid
        get childPrice       
    append packageName to packageNames
    add packageName to packagesData with the values for adultPrice and childPrice
    return packageNames, packagesData


function getValidInt(prompt, error)
    try
        get integer
        if integer is less than 0
            go to except
        return integer
    except
        display error


function getValidFloat(prompt, error)
    try
        get floatNumber
        if floatNumber is less than 0.01
            go to except
        return floatNumber
    except
        display error


function getValidPackageChoice(prompt, error1, error2)
    try
        get integer
        if integer is less than 1
            display error1
            return integer
        if integer is greater than the number of packages
            display error2
        return integer
    except
        display error1


main()


"""

def main():
    import random
    MENU = "\nMenu:\n(I)nstructions\n(C)alculate Catering\n(D)isplay Packages\n(L)oad Packages\n(S)ave Packages\n(A)dd Package\n(Q)uit\n>>> "
    packageNames = []
    packagesData = {}
    
    print("Welcome to the Great CP1200 Catering Calculator 2.0!\nWritten by Nicholas Barber, April 2012")

    menuChoice = str.upper(input(MENU))
    while menuChoice != "Q":
        if menuChoice == "I":
                   print("This program allows you to calculate catering costs based on choice of package and number of adults and children.\nYou can load packages from a file, add new ones and save the file for next time.")
        elif menuChoice == "C":
            if len(packageNames) == 0:
                print("You need to add or load a package first.")
            else:
                calculateCatering(packageNames, packagesData, random)
        elif menuChoice == "D":
            if len(packageNames) == 0:
                print("You need to add or load a package first.")
            else:
                displayPackages(packageNames, packagesData)
        elif menuChoice == "L":
            packageNames, packagesData = loadPackages()
        elif menuChoice == "S":
            savePackages(packageNames, packagesData)
        elif menuChoice == "A":
            packageNames, packagesData = addPackage(packageNames, packagesData)   
        else:
            print("Invalid menu choice.")
        menuChoice = str.upper(input(MENU))
    print("Thank you for using the Great CP1200 Catering Calculator 2.0.")


def calculateCatering(packageNames, packagesData, random):
    """ Takes a user input to choose a package and then calculates the catering for it accordingly."""
    INVALID_INT = "Number must be valid and >= 0"

    numberOfAdults = getValidInt("Please enter the number of adults: ", INVALID_INT)
    while type(numberOfAdults) != int:
        numberOfAdults = getValidInt("Please enter the number of adults: ", INVALID_INT)
    numberOfChildren = getValidInt("Please enter the number of children: ", INVALID_INT)
    while type(numberOfChildren) != int:
        numberOfChildren = getValidInt("Please enter the number of children: ", INVALID_INT)
    displayPackages(packageNames, packagesData)
    packageChoice = getValidPackageChoice(packageNames, "Which package would you like?: ", "Number must be valid and >= 1", "Number must be <=" + str(len(packageNames)))
    while type(packageChoice) != int or packageChoice < 1 or packageChoice > len(packageNames):
        packageChoice = getValidPackageChoice(packageNames, "Which package would you like?: ", "Number must be valid and >= 1", "Number must be <=" + str(len(packageNames)))       
    #The discountBonusChance number is used to determine whether or not adults are charged at adult prices or child prices
    discountBonusChance = random.randint(1, 10)
 
    if discountBonusChance == 1:    
        adultCost = float(packagesData[packageNames[packageChoice - 1]][1]) * numberOfAdults
    else:
        adultCost = float(packagesData[packageNames[packageChoice - 1]][0]) * numberOfAdults
    childrenCost = float(packagesData[packageNames[packageChoice - 1]][1]) * numberOfChildren
    totalCost = adultCost + childrenCost

    if numberOfAdults == 1:
        adults = "adult"
    else:
        adults = "adults"
    if numberOfChildren == 1:
        children = "child"
    else:
        children = "children"

    if discountBonusChance == 1:    
        print("\nThat will be $%0.2f" % totalCost, "for the " + packageNames[packageChoice - 1] + " (adults at kids' prices!) package for", numberOfAdults, adults + " and", numberOfChildren, children +". Enjoy!")
    else:
        print("\nThat will be $%0.2f" % totalCost, "for the " + packageNames[packageChoice - 1] + " package for", numberOfAdults, adults + " and", numberOfChildren, children +". Enjoy!")
          
 
def displayPackages(packageNames, packagesData):
    """ Displays any package details currently in the working memory."""
    for x in range(len(packageNames)):
        print(str(x + 1) + "." + "%16s" % packageNames[x] + " - $%0.2f" % float(packagesData[packageNames[x]][0]) + " / $%0.2f" % float(packagesData[packageNames[x]][1]))


def loadPackages(packagesFileName="packages.txt"):
    """ Loads package information from a text file (Default file name: "packages.txt")."""
    packageNames = []
    packagesData = {}
    packagesFile = open(packagesFileName, "r")
    for line in packagesFile:
        line = line.strip()
        packageName, adultPrice, childPrice = line.split(",")
        packageNames.append(packageName)
        packagesData[packageName] = (adultPrice, childPrice)
    packagesFile.close()
    return packageNames, packagesData


def savePackages(packageNames, packagesData, packagesFileName="packages.txt"):
    """ Saves any packages loaded in memory to a text file (Default file name: "packages.txt"), overriding any previously stored data."""
    textToSave = []
    for x in range(len(packageNames)):
        string = packageNames[x] + "," + str(packagesData[packageNames[x]][0]) + "," + str(packagesData[packageNames[x]][1]) + "\n"
        textToSave += string
    file = open("packages.txt", "w")
    for i in textToSave:
        file.write(i)
    file.close()


def addPackage(packageNames, packagesData):
    """ Adds a new package and its details to the working memory."""
    ADULT_PROMPT = "Enter package price per adult: $"
    CHILD_PROMPT = "Enter package price per child: $"
    INVALID_FLOAT_ERROR = "Price must be valid and >= $0.01."
    
    packageName = input("Enter package name: ")
    while packageName == "" or len(packageName) > 16:
        print("Package name can not be blank and must be less than 17 characters")
        packageName = input("Enter package name: ")
    adultPrice = getValidFloat(ADULT_PROMPT, INVALID_FLOAT_ERROR)
    while type(adultPrice) != float:
        adultPrice = getValidFloat(ADULT_PROMPT, INVALID_FLOAT_ERROR)       
    childPrice = getValidFloat(CHILD_PROMPT, INVALID_FLOAT_ERROR)
    while type(childPrice) != float:
        childPrice = getValidFloat(CHILD_PROMPT, INVALID_FLOAT_ERROR)       
    packageNames.append(packageName)
    packagesData[packageName] = (adultPrice, childPrice)
    return packageNames, packagesData


def getValidInt(prompt, error):
    """ Takes an input from the user and tests that it is a valid integer before returning it, or an error."""
    try:
        integer = int(input(prompt))
        if integer < 0:
            raise
        return integer
    except:
        print(error)


def getValidFloat(prompt, error):
    """ Takes an input from the user and tests that it is a valid float before returning it, or an error."""
    try:
        floatNumber = float(input(prompt))
        if floatNumber < 0.01:
            raise
        return floatNumber
    except:
        print(error)


def getValidPackageChoice(packageNames, prompt, error1, error2):
    """ Takes an input from the user and tests that it is a valid package number before returning it, or an error."""
    try:
        integer = int(input(prompt))
        if integer < 1:
            print(error1)
            return integer
        if integer > len(packageNames):
            print(error2)
        return integer
    except:
        print(error1)


main()
