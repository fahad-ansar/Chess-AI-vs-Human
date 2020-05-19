

#Name: Fahad Ansar
#St#: 6203384

#This script is the main script that acts as a hub between all the files and runs the game


from time import sleep, time

import Board
import sys
import os
import Pieces
import Team
import AI as ai
import CMethods as cm
from copy import deepcopy



#Method for taking player name input
def teamInput(ai):
    ta = None
    tb = None

    while ta==None:
        try:

            ta = str(raw_input("Give a name to Player A\n"))
            break
        except:
            print "Not a valid name format"

    if ai:
        print "\nAI would be player B"
        tb = "AI"
    else:
        while tb==None:
            try:

                tb = str(raw_input("Give a name to Player B \n"))
                break
            except:
                print "Not a valid name format"



    return ta,tb

#Method for taking indeces input
def indexInput(txt):
    i=None
    j=None
    while i > 8 or i < 1 or j < 1 or j > 8:
        try:
            i, j = map(int, raw_input(


                "Enter indices 'i' [1-8] and 'j' [1-8] " + txt + " (seperated by a space)\n").split())
            if i > 8 or i < 1 or j < 1 or j > 8: print str(i) + "," + str(j) + " Not in valid range of 1-8"

        except:
            print "Not Integers!! Please try again!"

    return i,j

#Method for check if someone has WOn
def checkWin(brd, tma, tmb):
    king = 0
    t1 = ""
    t2 = ""
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j].getPiece() != None:
                if brd[i][j].getPiece().getName().find("King") != -1:
                    king = king + 1
                    if brd[i][j].getPiece().getTeam().getName() == tma.getName():
                        t1 = tma.getName()
                    elif brd[i][j].getPiece().getTeam().getName() == tmb.getName():
                        t2 = tmb.getName()

    if king == 2:
        return False,None
    elif king == 1 or king == 0:
        ta=""
        if t1!="": ta = t1
        elif t2!="": ta=t2
        return True,ta

#Method for checking if there is a checking state
def checkMate(brd, temA, temB, turn):
    if turn == 0:
        a=0
        b=0
        for i in range(len(brd)):
            for j in range(len(brd)):
                if brd[i][j].getPiece() != None:
                    if brd[i][j].getPiece().getName().find("King") != -1:
                        if brd[i][j].getPiece().getTeam().getName() == temA.getName():
                            a=i
                            b=j


        ms = ai.getAllMoves(brd,ai.getPositions(brd,temA.getName()))
        for movs in ms:
            if movs[2] == a and movs[3] == b: return True



    elif turn == 1:
        a = 0
        b = 0
        for i in range(len(brd)):
            for j in range(len(brd)):
                if brd[i][j].getPiece() != None:
                    if brd[i][j].getPiece().getName().find("King") != -1:
                        if brd[i][j].getPiece().getTeam().getName() == temB.getName():
                            a = i
                            b = j

        ms = ai.getAllMoves(brd, ai.getPositions(brd,temB.getName()))
        for movs in ms:
            if movs[2] == a and movs[3] == b: return True

    return False


#Making new board
b=Board.Board()


#-----------------------------------------------------GAME START-------------------------------


print "---------------------------------------------------------------"
print "                        BASIC RULES"
print "- enter 'q' when to exit the program \nwhen asked about exiting game (after moves of both players"
print "- index range is from 1-8 ."
print "- after turn of each player the board would be ROTATED. due to which,\n the player whose turn it is will be at bottom part of the board always."
print "---------------------------------------------------------------"




#Taking input of the mode user want to play

AP = 0
try:
    AP = int(raw_input("Enter number associated with a mode to play in that mode:\n0 - human-VS-human\n1 - AI-VS-human\n2 - Testing (human vs human) give board state"
                       +"\n(Entering anything else will lead to player-VS-player)\n"))

except:
    print "\n---------------------------------------------------------------\nNot a valid entry but you can play human-VS-human"




#HUMAN VS HUMAN Game mode/*/*/*//*/*/*//*/*/*//*/*/*//*/*/*//*/*/*//*/*/*//*/*/*/

if AP == 0:

    b.initializePieces()

    print "\n---------------------------------------------------------------\n------------------Welcome to human-VS-human mode------------------\n"
    ta,tb = teamInput(AP)

    b.setTeamA(str(tb))
    b.setTeamB(str(ta))

    tnC = 0

    while True:
        cm.printBoard(b.teamA.getName(),b.teamB.getName(),b.brd, tnC)

        i=None
        j=None
        i2=None
        j2=None
        tp = deepcopy(b.brd)
        moved = False


        while not moved:

            i,j = indexInput("of the piece you want to move!")
            if cm.isEmptyBox(i-1, j-1, b.brd):
                print "There is not piece there, Null pointer!!!\n"
                continue

            i2,j2 = indexInput("of the box you want to move to!")
            if i == i2 and j == j2:
                print "Cant move a piece where it already is!\n"
                continue

            chk, tp = cm.movePiece(i - 1, j - 1, i2 - 1, j2 - 1, b.brd)

            if chk[0] and not chk[2]:
                b.brd = deepcopy(tp)
                break
            else:
                print "!!!! Not a valid move !!!! \nPlease try again \n"


        b.brd = cm.pawnConverter(b.brd)
        cm.printBoard(b.teamA.getName(),b.teamB.getName(),b.brd, tnC)

        CM = checkMate(b.brd,b.teamA,b.teamB,tnC)
        if CM: print "ITS A CHECKMATE!!"

        if ai.isTie(b.brd):
            print "ITS A TIE"
            break

        sleep(1)
        os.system("clear")
        b.flipBoard()

        win, won = checkWin(b.brd, b.teamA, b.teamB)

        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break

        print "-----------Board Rotated! (you are at the bottom side now)-------------------"
        if tnC == 0:
            tnC = 1
        else:
            tnC = 0

        if raw_input("Press Enter key to proceed or type 'q' to exit") == "q": sys.exit(0)

        sleep(1)




#Ai vs Human GAme Mode/*/*/*//*/*/*//*/*/*//*/*/*//*/*/*//*/*/*//*/*/*/
elif AP == 1:
    b.initializePieces()

    print "\n---------------------------------------------------------------\n------------------Welcome to AI-VS-human mode------------------\n"
    ta, tb = teamInput(AP)

    b.setTeamA(str(tb))
    b.setTeamB(str(ta))
    cm.printBoard(b.teamA.getName(), b.teamB.getName(), b.brd, 0)

    while True:

        i = None
        j = None
        i2 = None
        j2 = None

        moved = False

        print "-----------------------------YOUR TURN--------------------------------"
        while not moved:

            i, j = indexInput("of the piece you want to move!")
            if cm.isEmptyBox(i - 1, j - 1, b.brd):
                print "There is not piece there, Null pointer!!!\n"
                continue

            i2, j2 = indexInput("of the box you want to move to!")
            if i == i2 and j == j2:
                print "Cant move a piece where it already is!\n"
                continue

            chk, tp = cm.movePiece(i - 1, j - 1, i2 - 1, j2 - 1, b.brd)

            if chk[0] and not chk[2]:
                b.brd = deepcopy(tp)
                break
            else:
                print "!!!! Not a valid move !!!! \nPlease try again \n"


        win, won = checkWin(b.brd, b.teamA, b.teamB)

        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break

        if ai.isTie(b.brd):
            print "ITS A TIE"
            break

        CM = checkMate(b.brd, b.teamA, b.teamB, 0)
        if CM: print "ITS A CHECKMATE!!"

        cm.printBoard(b.teamA.getName(), b.teamB.getName(), b.brd, 0)
        if raw_input("Press Enter key to proceed or type 'q' to exit") == "q": sys.exit(0)

        sleep(1)
        os.system("clear")
        print "-----------------------------AI TURN--------------------------------"

        print "---------------------AI Calculating its moves------------------------------"
        b.brd = ai.performMinimax(b.brd,b.teamA,b.teamB)

        print "-----------Board Rotated! (you are at the bottom side now)-------------------"


        cm.printBoard(b.teamA.getName(), b.teamB.getName(), b.brd, 0)

        win,won = checkWin(b.brd, b.teamA, b.teamB)

        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break

        if ai.isTie(b.brd):
            print "ITS A TIE"
            break

        CM = checkMate(b.brd, b.teamA, b.teamB, 0)
        if CM: print "ITS A CHECKMATE!!"

        sleep(1)
        os.system("clear")




#Human vs human Testing mode*/*/*/*/*/*/*/*/*/*/*/*//*/*/*//*/*/*//*/*/*//*/*/*/
elif AP == 2:
    print "\n---------------------------------------------------------------\n------------------Welcome to human-VS-human Testing mode------------------\n"
    ta, tb = teamInput(0)

    b.setTeamA(str(tb))
    b.setTeamB(str(ta))



    #Creation of Testing Board

    print "\nNow you will be placing piece one by one on the board!\n----------------------------------------------------\n"

    # Pwn
    for i in range(8):

        if raw_input("if you want to place Black pawn " + str(i) + " enter Y else press any key to proceed") == "Y":

            a,bb = indexInput(" of Black Pawn " + str(i) + " ")
            b.brd[a-1][bb-1].mkrPiece("P", b.teamA, "B", i + 1)

    for i in range(8):

        if raw_input("if you want to place White pawn " + str(i) + " enter Y else press any key to proceed") == "Y":

            a,bb = indexInput(" of White Pawn " + str(i) + " ")
            b.brd[a-1][bb-1].mkrPiece("P", b.teamB, "W", i + 1)



    # Rook
    if raw_input("if you want to place Black Rook 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Rook 1 ")
        b.brd[a-1][bb-1].mkrPiece("R", b.teamA, "B", 1)

    if raw_input("if you want to place Black Rook 2 enter Y else press any key to proceed") == "Y":
        a, b = indexInput(" of Black Rook 2 ")
        b.brd[a-1][bb-1].mkrPiece("R", b.teamA, "B", 2)

    if raw_input("if you want to place White Rook 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Rook 1 ")
        b.brd[a-1][bb-1].mkrPiece("R", b.teamB, "W", 1)

    if raw_input("if you want to place White Rook 2 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Rook 2 ")
        b.brd[a-1][bb-1].mkrPiece("R", b.teamB, "W", 2)




    # Bishop
    if raw_input("if you want to place Black Bishop 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Bishop 1 ")
        b.brd[a-1][bb-1].mkrPiece("B", b.teamA, "B", 1)

    if raw_input("if you want to place Black Bishop 2 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Bishop 2 ")
        b.brd[a-1][bb-1].mkrPiece("B", b.teamA, "B", 2)

    if raw_input("if you want to place White Bishop 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Bishop 1 ")
        b.brd[a-1][bb-1].mkrPiece("B", b.teamB, "W", 1)

    if raw_input("if you want to place White Bishop 2 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Bishop 2 ")
        b.brd[a-1][bb-1].mkrPiece("B", b.teamB, "W", 2)



    # Knight
    if raw_input("if you want to place Black Knight 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Knight 1 ")
        b.brd[a-1][bb-1].mkrPiece("Kn", b.teamA, "B", 1)

    if raw_input("if you want to place Black Knight 2  enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Knight 2 ")
        b.brd[a-1][bb-1].mkrPiece("Kn", b.teamA, "B", 2)

    if raw_input("if you want to place White Knight 1 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Knight 1 ")
        b.brd[a-1][bb-1].mkrPiece("Kn", b.teamB, "W", 1)

    if raw_input("if you want to place White Knight 2 enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Bishop 2 ")
        b.brd[a-1][bb-1].mkrPiece("Kn", b.teamB, "W", 2)


    # Queen
    if raw_input("if you want to place Black Queen  enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black Queen ")
        b.brd[a-1][bb-1].mkrPiece("Q", b.teamA, "B", 1)

    if raw_input("if you want to place White Queen enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White Queen ")
        b.brd[a-1][bb-1].mkrPiece("Q", b.teamB, "W", 1)


    # King
    if raw_input("if you want to place Black King  enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of Black King ")
        b.brd[a-1][bb-1].mkrPiece("K", b.teamA, "B", 1)

    if raw_input("if you want to place White King enter Y else press any key to proceed") == "Y":
        a, bb = indexInput(" of White King ")
        b.brd[a-1][bb-1].mkrPiece("K", b.teamB, "W", 1)

    tnC = 0

    while True:
        cm.printBoard(b.teamA.getName(), b.teamB.getName(), b.brd, tnC)

        i = None
        j = None
        i2 = None
        j2 = None
        tp = deepcopy(b.brd)
        moved = False

        while not moved:

            i, j = indexInput("of the piece you want to move!")
            if cm.isEmptyBox(i - 1, j - 1, b.brd):
                print "There is not piece there, Null pointer!!!\n"
                continue

            i2, j2 = indexInput("of the box you want to move to!")
            if i == i2 and j == j2:
                print "Cant move a piece where it already is!\n"
                continue

            chk, tp = cm.movePiece(i - 1, j - 1, i2 - 1, j2 - 1, b.brd)

            if chk[0] and not chk[2]:
                b.brd = deepcopy(tp)
                break
            else:
                print "!!!! Not a valid move !!!! \nPlease try again \n"

        b.brd = cm.pawnConverter(b.brd)
        cm.printBoard(b.teamA.getName(), b.teamB.getName(), b.brd, tnC)
        CM = checkMate(b.brd,b.teamA,b.teamB,tnC)
        if CM: print "ITS A CHECKMATE!!"

        if ai.isTie(b.brd):
            print "ITS A TIE"
            break

        sleep(1)
        os.system("clear")
        b.flipBoard()

        win, won = checkWin(b.brd, b.teamA, b.teamB)

        if win:
            print "-----------------------------------------------------------"
            print won + " has just won the game"
            break

        print "-----------Board Rotated! (you are at the bottom side now)-------------------"
        if tnC == 0:
            tnC = 1
        else:
            tnC = 0

        if raw_input("Press Enter key to proceed or type 'q' to exit") == "q": sys.exit(0)

        sleep(1)
