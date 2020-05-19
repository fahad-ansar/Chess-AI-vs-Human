
#Name: Fahad Ansar
#St#: 6203384


#This script has all the methods that are commonly used throughout the project


import sys

#checks if the given indeces are empty
def isEmptyBox(i, j,brd):
    if 0<=i<=7 and 0<=j<=7:
        return brd[i][j].getPiece() == None
    else:
        return None


# From Point A to Point B - CHK and VERIFY
def movePiece(Ai, Aj, Bi, Bj,brd):
    # chk current team movement. user can only movie his piece (current playing team)
    #design check system for all indeces of array 'x'

    p = None
    x = validateMove(Ai, Aj, Bi, Bj,brd)
    if (x[0] and x[1] and not x[2]) or ( x[0] and not x[1] and not x[2]):
        p = brd[Bi][Bj].getPiece()
        brd[Bi][Bj].setPiece(brd[Ai][Aj].getPiece())
        brd[Ai][Aj].setPiece(None)
    return x,brd

#Print the bord that is passed in to it
def printBoard(ta, tb, brd, turnCount):
    if turnCount == 0:
        print("                                                   " + str(ta))
    elif turnCount == 1:
        print("                                                   " + str(tb))
    print("                                               -------------");

    print("                                                     j")
    print(" ")

    print(
        "              1             2             3             4             5             6             7             8");
    print(
        "       -----------------------------------------------------------------------------------------------------------------")

    for i in range(8):
        if i == 4:
            sys.stdout.write("i   ")
        else:
            sys.stdout.write("    ")
        sys.stdout.write(str(i + 1))
        sys.stdout.write("  |")
        for j in range(8):
            sys.stdout.write(" ")

            if brd[i][j].getPiece() != None:
                sys.stdout.write(brd[i][j].getPiece().getName())  # to strng for board printing

            else:
                kg = "           "
                sys.stdout.write(kg)
            sys.stdout.write(" |")

        print(" ")
        print(
            "       -----------------------------------------------------------------------------------------------------------------")

    print(" ")
    print("                                               -------------");
    if turnCount == 0:
        print("                                                   " + str(tb))
    elif turnCount == 1 :
        print("                                                   " + str(ta))

    # King validation


#Validates that passed in move from a to b in board brd for king
def RetKingValidate(c1, c2, a, b, tnamep,brd):
    retState = [bool] * 3
    if c1 and c2:
        if not isEmptyBox(a, b,brd):
            if brd[a][b].getPiece().getTeam().getName() != tnamep:
                retState[2] = False
            else:
                retState[2] = True
            retState[1] = False
        else:
            retState[1] = True
            retState[2] = False
        retState[0] = True
    else:
        retState[0] = False

    return retState

#Validates that passed in move from a to b in board brd for bishop
def RetCrossValidate(tname, bi, bj, a, b, rS, brd):

    if bi == a and bj == b:
        if not isEmptyBox(a, b,brd):
            if brd[a][b].getPiece() != None:
                if brd[a][b].getPiece().getTeam().getName() != tname:
                    rS[2] = False
                else:
                    rS[2] = True

            # print "i " + str(a) + " : j " + str(b)
            rS[1] = False
        else:
            rS[1] = True
            rS[2] = False

        rS[0] = True
    else:

        rS[0] = False

    return rS

#Validates the moves moving in plus  and cross directions
def chkNchiki(ai, aj, bi, bj, tname, cross, plus,brd):

    rS = [bool] * 3

    if cross == 1:
        # upperRight
        i = 0
        j = 0
        while 0 <= ai - i <= 7 and 0 <= aj + j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai - i, aj + j, rS,brd)
            if rS[0]: return rS
            i = i + 1
            j = j + 1



        # upperLeft
        i = 0
        j = 0
        while 0 <= ai - i <= 7 and 0 <= aj - j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai - i, aj - j, rS,brd)
            if rS[0]: return rS
            i = i + 1
            j = j + 1


        # lowerLeft
        i = 0
        j = 0
        while 0 <= ai + i <= 7 and 0 <= aj - j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai + i, aj - j, rS,brd)
            if rS[0]: return rS
            i = i + 1
            j = j + 1


        # lowerRight
        i = 0
        j = 0
        while 0 <= ai + i <= 7 and 0 <= aj - j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai + i, aj - j, rS,brd)
            if rS[0]: return rS
            i = i + 1
            j = j + 1



    if plus == 1:

        # up
        i = 0
        while 0 <= ai - i <= 7 :
            rS = RetCrossValidate(tname,bi,bj, ai - i, aj, rS,brd)
            if rS[0]: return rS
            i = i + 1



        # Down
        i = 0
        while 0 <= ai + i <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai + i, aj, rS,brd)
            if rS[0]: return rS
            i = i + 1



        # Left
        j = 0
        while 0 <= aj - j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai, aj - j, rS,brd)
            if rS != 0: return rS
            j = j + 1



        # Right
        j = 0
        while 0 <= aj + j <= 7:
            rS = RetCrossValidate(tname,bi,bj, ai, aj + j, rS,brd)
            if rS != 0: return rS
            j = j + 1



    return rS


#Chk the entered indexes and verify the appropriatness
def validateMove(ai, aj, bi, bj,brd):

    #0 Is valid
    #1 Is full
    #2 is my team

    fpiece = brd[ai][aj].getPiece()

    retState = [bool] * 3

    # current team name
    tmname = brd[ai][aj].getPiece().getTeam().getName()

    # begin and futher case for pawn
    if fpiece.getName().find("Pawn") != -1:
        if bi==ai-1 and bj==aj:

            retState = RetCrossValidate(tmname,bi,bj,ai-1,aj,retState,brd)
            if retState[0]: return retState

        elif bi==ai-2 and ai==6 and isEmptyBox(bi-1,bj,brd):

            retState = RetCrossValidate(tmname,bi,bj,ai-2,aj,retState,brd)
            if retState[0]: return retState

        elif (bi==ai-1 and bj==aj+1):
            if isEmptyBox(bi,bj,brd) == False:

                retState = RetCrossValidate(tmname, bi, bj, ai-1,aj+1,retState,brd)
                if retState[0]: return retState


        elif (bi==ai-1 and bj==aj-1):
            if isEmptyBox(bi,bj,brd) == False:
                retState = RetCrossValidate(tmname, bi, bj, ai-1, aj-1, retState,brd)
                if retState[0]: return retState




    #if entered piece is king (Entered Move validation)
    elif fpiece.getName().find("King") != -1:

        retState = RetKingValidate(ai > 0, (bi == ai - 1 and bj == aj), ai - 1, aj, tmname,brd)  # up
        if retState[0]: return retState

        retState = RetKingValidate(ai < 7, (bi == ai + 1 and bj == aj), ai + 1, aj, tmname,brd)  # down
        if retState[0]: return retState

        retState = RetKingValidate(aj > 0, (bi == ai and bj == aj - 1), ai, aj - 1, tmname,brd)  # left
        if retState[0]: return retState

        retState = RetKingValidate(aj < 7, (bi == ai and bj == aj + 1), ai, aj + 1, tmname,brd)  # right
        if retState[0]: return retState

        retState = RetKingValidate((ai > 0 and aj < 7), (bi == ai - 1 and bj == aj + 1), ai - 1, aj + 1,
                                        tmname,brd)  # up-right
        if retState[0]: return retState

        retState = RetKingValidate((ai > 0 and aj > 0), (bi == ai - 1 and bj == aj - 1), ai - 1, aj - 1,
                                        tmname,brd)  # up-left
        if retState[0]: return retState

        retState = RetKingValidate((ai < 7 and aj < 7), (bi == ai + 1 and bj == aj + 1), ai + 1, aj + 1,
                                        tmname,brd)  # up-right
        if retState[0]: return retState

        retState = RetKingValidate((ai < 7 and aj > 0), (bi == ai + 1 and bj == aj - 1), ai + 1, aj - 1,
                                        tmname,brd)  # up-left
        if retState[0]: return retState


    # if entered piece is Bishop (Entered Move validation)
    elif fpiece.getName().find("Bishop") != -1:
        retState = chkNchiki(ai, aj, bi, bj, tmname, 1, 0,brd)
        if retState[0]: return retState


    #if entered piece is Queen (Entered Move validation)
    elif fpiece.getName().find("Queen") != -1:
        retState = chkNchiki(ai, aj, bi, bj, tmname, 1, 1,brd)
        if retState[0]: return retState

    #if entered piece is Rook (Entered Move validation)
    elif fpiece.getName().find("Rook") != -1:
        retState = chkNchiki(ai, aj, bi, bj, tmname, 0, 1,brd)
        if retState[0]: return retState


    #if entered piece is Knight (Entered Move validation)
    elif fpiece.getName().find("Knight") != -1:



        for i in range(2):
            if i%2 == 0: it = ai+2
            elif i%2 == 1: it = ai-2
            for j in range(2):
                if j % 2 == 0: jt = aj + 1
                elif j % 2 == 1: jt = aj - 1
                if not (0<=it <=7 and 0<=jt <=7): continue
                retState = RetCrossValidate(tmname,bi,bj,it,jt,retState,brd)
                if retState[0] == True: break
            if retState[0] == True: break



        if retState[0] == True: return retState

        for i in range(2):
            if i%2 == 0: it = aj+2
            elif i%2 == 1: it = aj-2
            for j in range(2):
                if j % 2 == 0: jt = ai + 1
                elif j % 2 == 1: jt = ai - 1
                if not (0 <= it <= 7 and 0 <= jt <= 7): continue
                retState = RetCrossValidate(tmname, bi, bj, it, jt, retState,brd)
                if retState[0] == True: break
            if retState[0] == True: break

    return retState

#This method revives pawn reached at the end into another piece
def pawnConverter(brd):
    for i in range(len(brd)):
        if i == 0:
            for j in range(len(brd)):
                if brd[i][j].getPiece()!=None:
                    if brd[i][j].getPiece().getName().find("Pawn")!=-1:
                        tm = brd[i][j].getPiece().getTeam().getName()
                        clr = "B"
                        if brd[i][j].getPiece().getName().find("W")!=-1:
                            clr = "W"
                        elif brd[i][j].getPiece().getName().find("B")!=-1:
                            clr = "B"
                        brd[i][j].setPiece(None)
                        brd[i][j].mkrPiece("Q",tm,clr,24)
    return brd


