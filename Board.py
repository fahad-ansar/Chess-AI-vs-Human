

#Name: Fahad Ansar
#St#: 6203384


import sys
import Pieces
import Team

#This script has all the methods and class that needed for only board


# Square object to form a complete board
class Square:
    color = None
    piece = None
    pr = Pieces.PeiceMkr()

    def __init__(self):
        self.color = None

    def setColor(self, nm):
        self.color = nm

    def getColor(self):
        return self.color

    def getName(self):
        temp = ""
        if self.piece != None:
            temp = self.piece.getName()
        return temp

    def mkrPiece(self, p, team, colour, no):
        self.piece = self.pr.createPiece(p, team, colour, no)

    def setPiece(self, pi):
        self.piece = None
        self.piece = pi

    def getPiece(self):
        return self.piece
        # print(self.team.getName()[-1])


# Board object to act as a chess board
class Board:


    # initializing primitives
    teamA = Team.Team()
    teamA.bin = 0
    teamB = Team.Team()
    teamB.bin = 1
    teamA.setName("PlayerA")
    teamB.setName("PlayerB")

    turnCount = 0  # ---------------------------------------------------------------------------------

    # using square object to create a chess board
    brd = [[Square() for j in range(8)] for i in range(8)]

    # for loop to set colour of squares in the board
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                brd[i][j].setColor("White")
            elif (i + j) % 2 == 1:
                brd[i][j].setColor("Black")

    print("Board Initialized!")

    # Methods
    def getBoard(self):
        return self.brd


    def initializePieces(self):

        # Pwn
        for i in range(8):
            self.brd[1][i].mkrPiece("P", self.teamA,"B",i+1)
            self.brd[6][i].mkrPiece("P", self.teamB,"W",i+1)

        # Rook
        self.brd[0][0].mkrPiece("R", self.teamA,"B",1)
        self.brd[0][7].mkrPiece("R", self.teamA,"B",2)
        self.brd[7][0].mkrPiece("R", self.teamB,"W",1)
        self.brd[7][7].mkrPiece("R", self.teamB,"W",2)

        # Bishop
        self.brd[0][2].mkrPiece("B", self.teamA,"B",1)
        self.brd[0][5].mkrPiece("B", self.teamA,"B",2)
        self.brd[7][2].mkrPiece("B", self.teamB,"W",1)
        self.brd[7][5].mkrPiece("B", self.teamB,"W",2)

        # Knight
        self.brd[0][1].mkrPiece("Kn", self.teamA,"B",1)
        self.brd[0][6].mkrPiece("Kn", self.teamA,"B",2)
        self.brd[7][1].mkrPiece("Kn", self.teamB,"W",1)
        self.brd[7][6].mkrPiece("Kn", self.teamB,"W",2)

        # Rook
        self.brd[0][3].mkrPiece("Q", self.teamA,"B",1)
        self.brd[7][3].mkrPiece("Q", self.teamB,"W",1)

        # King
        self.brd[0][4].mkrPiece("K", self.teamA,"B",1)
        self.brd[7][4].mkrPiece("K", self.teamB,"W",1)

    def setTeamA(self, namea):
        self.teamA.setName(namea)

    def setTeamB(self, nameb):
        self.teamB.setName(nameb)

    def getTeam(self, ab):
        return self.teamA if ab == 1 else self.teamB





    def flipBoard(self):
        for i in self.brd:
            i.reverse()
        self.brd.reverse()
        self.turnCount = 1


    def restart(self):
        self.brd.clear()
        self.brd = [[Square() for j in range(8)] for i in range(8)]
        self.turnCount = 0  # -------------------------------------------------------------------
        self.initializePieces()
        print("EVERYTHING RESTARTED!")


    def toString(self):
        st = ""
        st = st + "Game State---------------------\n"

        st = st + "Teams: " + self.teamA.getName() + " , " + self.teamB.getName() + "\n"

        st = st + "Score: " + str(self.teamB.getPoints()) + " , " + str(self.teamB.getPoints()) + "\n"

        return st
