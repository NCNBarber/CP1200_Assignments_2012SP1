"""
Nicholas Barber
Assignment 2 - 18/05/2012
GUI Application

Pseudocode:

class GUIApplication

    method pregameCheck(self)
        if the entry field for player 1's name is empty
            display enter player's name message
        otherwise
            call setupGame(self)

    method setupGame(self)
        set WINNING_SCORE
        initialise a Player object for player 1, taking the name from the player 1 name entry field
        initialise a Player object for player 2
        initialise a Player object for player 3
        playersList = [player 1 object, player 2 object, player 3 object]
        namesInUse = [player 1's name]
        initialise totalRounds variable

        for each player in playersList (except the first)
            use method "setComputerName" on player 
            repeat while player's name is not unique
                use method "setComputerName" on player
            append player's name to namesInUse

        set GUI Labels, Status Label, Choice Entry Field and Text Display
        replace the Setup Button with the Play Round Button

    method playRound(self)
        choices = blank list
        get player 1's choice
        repeat while player 1's choice is invalid
            get player 1's choice
        append player 1's choice to choices

        add 1 to totalRounds
        set Text Display to show Round number
            
        for each player in playersList (except the first)
            append player's choice

        for each choice in choices
            if the number of "choice" in choices = 1
                move player "choice" places

        display computer's choices

        display every player's position

        set Status Label's display

        if any player's position is equal to or greater than WINNING_SCORE
            winners = blank list
            for each player in playersList
                if a player's position is equal to or greater than WINNING_SCORE
                    append player to winners

        if the number of winners = 1
            remove Play Round Button
            set Text Display to display the winner
            set Status Label's display
        otherwise if the length of winners is greater than 1 but less than the length of playersList
            remove Play Round Button
            set Text Display to display the winners
            set Status Label's display
        otherwise
            remove Play Round Button
            set Text Display to display everyone won
            set Status Label's display

    method getValidInt(self, error)        
        try
            get value from p1ChoiceEntry
            if the value is an integer
                return integer
        except
            display error
    

"""

from tkinter import *
from Player import Player

class GUIApplication(Frame):

    def __init__(self):
        """Constructs the GUI."""
        Frame.__init__(self)
        self.master.title("Choosem Racing - Nicholas Barber")
        self["bg"] = "white"
        self.grid()
                
        self.p1NameEntry = Entry(self)
        self.p1NameEntry.grid(row=0, column=0, columnspan=4)

        self.setupBtn = Button(self, text="Setup Game", command=self.preSetupCheck)
        self.setupBtn.grid(row=4, column=0, columnspan=4)
        
        self.gameText = Text(self, width=50, height=3, wrap=WORD)
        self.gameText.grid(row=6, column=0, columnspan=4)
        self.gameText.delete(0.0, END)
        self.gameText.insert(0.0, "Welcome to Choosem Racing!\nEnter your name and click the button to start!")

        self.statusLbl = Label(self, text="Please enter player name", bg="white")
        self.statusLbl.grid(row=7, column=0, columnspan=4, sticky=W)

    def preSetupCheck(self):
        """Checks the player has put in a name before the game can start."""
        if self.p1NameEntry.get() == "":
            self.gameText.delete(0.0, END)
            self.gameText.insert(0.0, "Player name can not be blank.")
        else:
            self.setupGame()
        
    def setupGame(self):
        """Sets the game up to play."""
        self._WINNING_SCORE = 10
        self.p1 = Player(self.p1NameEntry.get())
        self.p2 = Player()
        self.p3 = Player()
        self._playersList = [self.p1, self.p2, self.p3]
        self._namesInUse = [self._playersList[0].getName()]
        self._totalRounds = 0

        #Sets the computer player's names.
        for player in self._playersList[1:]:
            player._setComputerName()
            while player.getName() in self._namesInUse:
                player._setComputerName()
            self._namesInUse.append(player.getName())

        self.nameLbl = Label(self, text="Name:", bg="white")
        self.nameLbl.grid(row=1, column=0, sticky=W)
        self.p1NameLbl = Label(self, text=self._playersList[0].getName(), bg="white")
        self.p1NameLbl.grid(row=1, column=1, sticky=W)
        self.p2NameLbl = Label(self, text=self._playersList[1].getName(), bg="white")
        self.p2NameLbl.grid(row=1, column=2, sticky=W)
        self.p3NameLbl = Label(self, text=self._playersList[2].getName(), bg="white")
        self.p3NameLbl.grid(row=1, column=3, sticky=W)

        self.positionLbl = Label(self, text="Position:", bg="white")
        self.positionLbl.grid(row=2, column=0, sticky=W)
        self.p1PositionLbl = Label(self, text=self._playersList[0].getPosition(), bg="white")
        self.p1PositionLbl.grid(row=2, column=1, sticky=W)
        self.p2PositionLbl = Label(self, text=self._playersList[1].getPosition(), bg="white")
        self.p2PositionLbl.grid(row=2, column=2, sticky=W)
        self.p3PositionLbl = Label(self, text=self._playersList[2].getPosition(), bg="white")
        self.p3PositionLbl.grid(row=2, column=3, sticky=W)

        self.positionLbl = Label(self, text="Choice:", bg="white")
        self.positionLbl.grid(row=3, column=0, sticky=W)
        self.p1ChoiceEntry = Entry(self, width=2)
        self.p1ChoiceEntry.grid(row=3, column=1, columnspan=1, sticky=W)

        self.gameText.delete(0.0, END)
        self.gameText.insert(0.0, "Enter your choice in the box.\nClick Play Round each round.")

        self.statusLbl["text"] = "Ready to begin!"

        self.p1NameEntry.destroy()
        self.setupBtn.destroy()
        
        self.playRoundBtn = Button(self, text="Play Round", command=self.prePlayRoundCheck)
        self.playRoundBtn.grid(row=4, column=0, columnspan=4)

    def prePlayRoundCheck(self):
        """Checks the player has put in a valid choice before starting the round."""
        self._player1Choice = self.getValidInt("Please enter a valid number")
        if self._player1Choice == None:
            return
        if self._player1Choice < 1 or self._player1Choice > 3:
            self.gameText.delete(0.0, END)
            self.gameText.insert(0.0, "Please enter a valid number between 1 and 3")
            return
        self.playRound()
        
    def playRound(self):
        """Runs the main game."""
        choices = [self._player1Choice]

        self._totalRounds += 1
        self.gameText.delete(0.0, END)
        self.gameText.insert(0.0, "Round " + str(self._totalRounds))
        
        for player in self._playersList[1:]:
            choices.append(player.getChoice())

        for choice in choices:
            if choices.count(choice) == 1:
                self._playersList[choices.index(choice)].move(choice, self._WINNING_SCORE)
                
        self.p2ChoiceLbl = Label(self, text=choices[1], bg="white")
        self.p2ChoiceLbl.grid(row=3, column=2, sticky=W)
        self.p3ChoiceLbl = Label(self, text=choices[2], bg="white")
        self.p3ChoiceLbl.grid(row=3, column=3, sticky=W)

        self.p1PositionLbl = Label(self, text=self._playersList[0].getPosition(), bg="white")
        self.p1PositionLbl.grid(row=2, column=1, sticky=W)
        self.p2PositionLbl = Label(self, text=self._playersList[1].getPosition(), bg="white")
        self.p2PositionLbl.grid(row=2, column=2, sticky=W)
        self.p3PositionLbl = Label(self, text=self._playersList[2].getPosition(), bg="white")
        self.p3PositionLbl.grid(row=2, column=3, sticky=W)

        self.statusLbl["text"] = "Game On..."

        #Checks if there are any winners and if there are, finishes the game.
        if self._playersList[0].getPosition() >= self._WINNING_SCORE or self._playersList[1].getPosition() >= self._WINNING_SCORE or self._playersList[2].getPosition() >= self._WINNING_SCORE:
            winners = []
            for player in self._playersList:
                if player.getPosition() >= self._WINNING_SCORE:
                    winners.append(player)

            if len(winners) == 1:
                self.playRoundBtn.destroy()
                self.gameText.delete(0.0, END)
                self.gameText.insert(0.0, "Round " + str(self._totalRounds) + "\nThe winner is: " + winners[0].getName() + "!")
                self.statusLbl["text"] = "Game Over..."
            elif len(winners) > 1 and len(winners) != len(self._playersList):
                self.playRoundBtn.destroy()
                string = "Tie! The winners are:"
                for player in winners[:-1]:
                    string += " " + player.getName() + ","
                string = string[:-1]
                string += " and " + winners[-1].getName() + "!"
                self.gameText.delete(0.0, END)
                self.gameText.insert(0.0, "Round " + str(self._totalRounds) + "\n" + string)
                self.statusLbl["text"] = "Game Over..."
            else:
                self.playRoundBtn.destroy()
                self.gameText.delete(0.0, END)
                self.gameText.insert(0.0, "Round " + str(self._totalRounds) + "\nEveryone wins!")
                self.statusLbl["text"] = "Game Over..."

    def getValidInt(self, error):
        """ Takes an input from the user and tests that it is a valid integer before returning it, or an error."""
        try:
            integer = int(self.p1ChoiceEntry.get())
            return integer
        except:
            self.gameText.delete(0.0, END)
            self.gameText.insert(0.0, error)
                          
GUIApplication().mainloop()
