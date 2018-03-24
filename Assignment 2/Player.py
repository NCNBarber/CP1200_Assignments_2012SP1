"""
Nicholas Barber
Assignment 2 - 18/05/2012
Player class

Pseudocode:

class Player

    COMPUTER_NAMES = list of names

    constructor(name, position)
        instance.setName(name)
        instance.setPosition(position)

    method __str__(self)
        return instance's name and position

    method __lt__(self, other)
        return self's position compared in terms of less than to other's position

    basic getter for name

    basic setter for name

    method _setComputerName(self)
        set randomNumber as a random integer between the range 0 and the length of COMPUTER_NAMES
        set name to the name in COMPUTER_NAMES with the index randomNumber
        set instance's name to name
        
    method getPosition(self)
        return self._position

    method move(self, distance, WINNING_SCORE)
        set instance's position to instance's position plus distance
        if instance's position is greater than or equal to WINNING_SCORE
            return True
        return False

    method getChoice(self)
        return random integer between 1 and 3 inclusively

function test()
    set WINNING_SCORE to 10
    
    initialise a Player object for player 1
    initialise a Player object for player 2
    initialise a Player object for player 3
    set playersList to [player 1 object, player 2 object, player 3 object]
    set namesInUse to [player 1's name]

    for each player in playersList (except the first)
            use method "setComputerName" on player 
            repeat while player's name is not unique
                use method "setComputerName" on player
            append player's name to namesInUse

    while every player's position is less than WINNING_SCORE
        for each player in playersList
            use "print" function on player

        choices = blank list
        get player 1's choice
        append player 1's choice to choices
       
        for each player in playersList (except the first)
            append player's choice

        for count from 0 to the length of playersList
            display the name and choice of the player corresponding to count

        for each choice in choices
            if the number of choice in choices = 1
                move the player who's choice it is, choice moves
                
    for each player in playersList
        use "print" function on player

    winners = blank list
    for each player in playersList
        if the player's position is greater than or equal to WINNING_SCORE
            append player to winners

    if the length of winners is equal to 1
        display the winner
    otherwise if the length of winners is greater than 1 but less than the length of playersList
        display the winners
    otherwise
        display "Everyone wins!"

if the file is run directly
    test()
"""
from random import randrange

class Player(object):

    COMPUTER_NAMES = ["Mindi", "Nick", "Emily", "Jonathon", "Katie", "Nakita"]
    
    def __init__(self, name="", position=0):
        """ Initialises a Player object. """
        self._name = name
        self._position = position

    def __str__(self):
        return self._name + " Position: " + str(self._position)

    def __lt__(self, other):
        """ Compares player's positions in terms of less than. """
        return self._position < other._position
    
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def _setComputerName(self):
        """ Picks a random name for a computer player from a set list. """
        randomNumber = randrange(0, len(Player.COMPUTER_NAMES))
        name = Player.COMPUTER_NAMES[randomNumber]
        self._name = name
        
    def getPosition(self):
        return self._position

    def move(self, distance, WINNING_SCORE):
        self._position += distance
        if self._position >= WINNING_SCORE:
            return True
        return False

    def getChoice(self):
        return randrange(1, 4)

def test():
    WINNING_SCORE = 10
    
    p1 = Player("Me")
    p2 = Player()
    p3 = Player()
    playersList = [p1, p2, p3]
    namesInUse = [p1.getName()]

    for player in playersList[1:]:
        player._setComputerName()
        while player.getName() in namesInUse:
            player._setComputerName()
        namesInUse.append(player.getName())

    while p1.getPosition() < WINNING_SCORE and p2.getPosition() < WINNING_SCORE and p3.getPosition() < WINNING_SCORE:
        for player in playersList:
            print(player)

        choices = [int(input("Choice: "))]
        for player in playersList[1:]:
            choices.append(player.getChoice())

        for i in range(0, len(playersList)):
            print(playersList[i].getName() + " : ", choices[i])

        for choice in choices:
            if choices.count(choice) == 1:
                playersList[choices.index(choice)].move(choice, WINNING_SCORE)

    for player in playersList:
        print(player)

    winners = []
    for player in playersList:
        if player.getPosition() >= WINNING_SCORE:
            winners.append(player)

    if len(winners) == 1:
        print("The winner is: " + winners[0].getName())
    elif len(winners) > 1 and len(winners) < len(playersList):
        string = "Tie! The winners are:"
        for player in winners[:-1]:
            string += " " + player.getName() + ","
        string = string[:-1]
        string += " and " + winners[-1].getName() + "!"
        print("Tie! The winners are: " + string)
    else:
        print("Everyone wins!")

if __name__=="__main__":
    test()
