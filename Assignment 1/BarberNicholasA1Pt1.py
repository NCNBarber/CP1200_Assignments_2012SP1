"""
CP1200 - Assignment 1, Part 1
Nicholas Barber 21/03/2012
The Great CP1200 Catering Calculator

Pseudocode: 

BASIC_ADULT_PRICE = 10.00
BASIC_CHILD_PRICE = BASIC_ADULT_PRICE * 0.6
PREMIUM_ADULT_PRICE = 12.50
PREMIUM_CHILD_PRICE = PREMIUM_ADULT_PRICE * 0.6

display welcome message
display menu

get menuChoice
while menuChoice != Q
    if menuChoice = I
        display instructions
    elif menuChoice = C
        numberOfAdults = -1
        while numberOfAdults < 0
            get numberOfAdults
        numberOfChildren = -1
        while numberOfChildren < 0
            get numberOfChildren
        serviceType = ""
        while serviceType != B and serviceType != P
            get serviceType
        if serviceType = B
            packagePrice = numberOfAdults * BASIC_ADULT_PRICE + numberOfChildren * BASIC_CHILD_PRICE
            display basic packagePrice statement
        else
            randomChanceNumber = randomly generated number between 1 and 10
            if randomChanceNumber = 1
                packagePrice = numberOfAdults * BASIC_ADULT_PRICE + numberOfChildren * BASIC_CHILD_PRICE
                display free premium packagePrice statement
            else
                packagePrice = numberOfAdults * PREMIUM_ADULT_PRICE + numberOfChildren * PREMIUM_CHILD_PRICE
                display premium packagePrice statement
    else
        display "Invalid menu choice" message
    get menuChoice
display farewell message

"""

import random
MENU = "Menu:\n(I)nstructions\n(C)alculate Catering\n(Q)uit\n>>> "
BASIC_ADULT_PRICE = 10.00
BASIC_CHILD_PRICE = BASIC_ADULT_PRICE * 0.6
PREMIUM_ADULT_PRICE = 12.50
PREMIUM_CHILD_PRICE = PREMIUM_ADULT_PRICE * 0.6

print("Welcome to the Great CP1200 Catering Calculator!\nWritten by Nicholas Barber, March 2012\n")

menuChoice = str.upper(input(MENU))
while menuChoice != "Q":

    if menuChoice == "I":
        """By inputting "I" the program presents the user with a description of how the program works"""
        print("Enter number of adults and children and choose a service type.\nBasic:   food only    = $%0.2f" % BASIC_ADULT_PRICE, "per adult\nPremium: food & drink = $%0.2f" % PREMIUM_ADULT_PRICE, "per adult\nChildren are always 60% of the price of adults.\n")

    elif menuChoice == "C":
        """By inputting "C" the program prompts the user to input the data required to calculate the package
           cost. By adding sentinel controlled loops the program will continue to prompt the user until it
           receives a valid input for each variable."""
        numberOfAdults = -1
        while numberOfAdults < 0:
            numberOfAdults = int(input("Please enter the number of adults: "))

        numberOfChildren = -1
        while numberOfChildren < 0:
            numberOfChildren = int(input("Please enter the number of children: "))

        serviceType = ""
        while serviceType != "B" and serviceType != "P":
            serviceType = str.upper(input("Would you like (B)asic or (P)remium service?: "))

        if serviceType == "B":
            """If the service selected is "basic" then the program will calculate the basic package price
               for the number of adults and children specified and print it for the user. If the service
               selected is not "basic" then it must be "premium" as it is the only other possible input
               due to the service type input loop only accepting "B" or "P"."""
            packagePrice = numberOfAdults * BASIC_ADULT_PRICE + numberOfChildren * BASIC_CHILD_PRICE
            print("\nThat will be $%0.2f" % packagePrice, "for the basic service for", numberOfAdults, "adults and", numberOfChildren, "children. Enjoy!\n")
        else:
            randomChanceNumber = random.randrange(1, 11)
            """randomChanceNumber is generated to determine whether or not the user gets the
               premium package for the basic package price. The user has a 10% chance of
               getting the premium package for the basic price. In a range of 1 to 10, every
               number has a 10% chance of being randomly picked. By generating a random
               number between 1 and 10 and then asking if the number is equal to 1 particular
               number, for example: 1, we can give an if statement with 2 possible paths with
               1 path having a 10% chance of being followed (giving the user the premium
               package for the basic price), while the other has a 90% chance (charging full
               price)."""
            if randomChanceNumber == 1:
                """If the randomChanceNumber is equal to 1, then the user gets the premium package for
                   the basic price, otherwise the program calculates the premium package price for the
                   number of people and prints it for the user."""
                packagePrice = numberOfAdults * BASIC_ADULT_PRICE + numberOfChildren * BASIC_CHILD_PRICE
                print("\nThat will be $%0.2f" % packagePrice, "for the premium (FREE!) service for", numberOfAdults, "adults and", numberOfChildren, "children. Enjoy!\n")
            else:
                packagePrice = numberOfAdults * PREMIUM_ADULT_PRICE + numberOfChildren * PREMIUM_CHILD_PRICE
                print("\nThat will be $%0.2f" % packagePrice, "for the premium service for", numberOfAdults, "adults and", numberOfChildren, "children. Enjoy!\n")

    else:
        """If the user fails to input their menu choice as "I", "C" or "Q", then the program prints an
           error message and then goes back to the start, re-printing the menu and prompting the user
           for a new menu choice."""
        print("Invalid menu choice.\n")
    menuChoice = str.upper(input(MENU))
print("Thank you for using the Great CP1200 Catering Calculator.")
