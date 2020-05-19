


#Name: Fahad Ansar
#St#: 6203384


#This script is AI chess system that minimax function and all the related methods


import Board as b
import Team
import sys,time
import CMethods as cm
from copy import deepcopy

nodes = 0  #for counting nodes (TEsting)


#Gets positions of the pieces in a team for future use
def getPositions(brd,team):
    poss = [[int] * 2] * 16

    for i in range(len(brd)):
        for j in range(len(brd)):
            # print brd[i][j].getPiece()
            if brd[i][j].getPiece() != None:
                # print brd[i][j].getPiece().getTeam().getName() + team
                if brd[i][j].getPiece().getTeam().getName() == team:
                     name = brd[i][j].getName()

                     if "Bishop" in name:
                         if "1" in name:
                             poss[11-1] = [i,j]
                         elif "2" in name:
                             poss[12-1] = [i,j]

                     elif "Rook" in name:
                         if "1" in name:
                             poss[9-1] = [i,j]
                         elif "2" in name:
                             poss[10-1] = [i, j]

                     elif "Knight" in name:
                         if "1" in name:
                             poss[13-1] = [i,j]
                         elif "2" in name:
                             poss[14-1] = [i, j]

                     elif "Pawn" in name:
                         if "1" in name:
                             poss[1-1] = [i,j]
                         elif "2" in name:
                             poss[2-1] = [i, j]
                         elif "3" in name:
                             poss[3-1] = [i, j]
                         elif "4" in name:
                             poss[4-1] = [i, j]
                         elif "5" in name:
                             poss[5-1] = [i,j]
                         elif "6" in name:
                             poss[6-1] = [i, j]
                         elif "7" in name:
                             poss[7-1] = [i, j]
                         elif "8" in name:
                             poss[8-1] = [i, j]

                     elif "King" in name:
                         poss[15-1] = [i,j]
                     elif "Queen" in name:
                         poss[16-1] = [i,j]

    return poss


#Generates All the legal moves
def getAllMoves(brd, pcsPos):

    moves = []


    for indexes in pcsPos:
        i = indexes[0]
        j = indexes[1]

        if type(i) != int or type(j) != int: continue

        if brd[i][j].getPiece().getName().find("Pawn")!=-1:
            vlid = cm.validateMove(i,j,i-1,j,brd)
            vlid3 = cm.validateMove(i, j, i - 1, j + 1, brd)
            vlid4 = cm.validateMove(i, j, i - 1, j - 1, brd)

            if i==6:
                vlid2 = cm.validateMove(i, j, i - 2, j, brd)

                if (vlid2[0] and vlid2[1] and not vlid2[2]) or (vlid2[0] and not vlid2[1] and not vlid2[2]):
                    moves.append([i, j, i - 2, j])


            if (vlid[0] and vlid[1] and not vlid[2]) or (vlid[0] and not vlid[1] and not vlid[2]):
                moves.append([i,j,i-1,j])

            if type(vlid3[0])==bool and (vlid3[0] and vlid3[1] and not vlid3[2]) or (vlid3[0] and not vlid3[1] and not vlid3[2]):
                moves.append([i, j, i - 1, j + 1])

            if type(vlid3[0])==bool and (vlid4[0] and vlid4[1] and not vlid4[2]) or (vlid4[0] and not vlid4[1] and not vlid4[2]):
                moves.append([i, j, i - 1, j - 1])


        if brd[i][j].getPiece().getName().find("King")!=-1:
            vlid = cm.validateMove(i,j,i-1,j,brd) #up
            vlid2 = cm.validateMove(i,j,i+1,j,brd) #down
            vlid3 = cm.validateMove(i,j,i,j-1,brd) #left
            vlid4 = cm.validateMove(i,j,i,j+1,brd) #right
            vlid5 = cm.validateMove(i,j,i-1,j-1,brd) #upLeft
            vlid6 = cm.validateMove(i,j,i-1,j+1,brd) #upRight
            vlid7 = cm.validateMove(i,j,i+1,j-1,brd) #downLeft
            vlid8 = cm.validateMove(i,j,i+1,j+1,brd) #downRight

            if (vlid[0] and vlid[1] and not vlid[2]) or (vlid[0] and not vlid[1] and not vlid[2]):
                moves.append([i,j,i-1,j])

            if (vlid2[0] and vlid2[1] and not vlid2[2]) or (vlid2[0] and not vlid2[1] and not vlid2[2]):
                moves.append([i,j,i+1,j])

            if (vlid3[0] and vlid3[1] and not vlid3[2]) or (vlid3[0] and not vlid3[1] and not vlid3[2]):
                moves.append([i,j,i,j-1])

            if (vlid4[0] and vlid4[1] and not vlid4[2]) or (vlid4[0] and not vlid4[1] and not vlid4[2]):
                moves.append([i,j,i,j+1])

            if (vlid5[0] and vlid5[1] and not vlid5[2]) or (vlid5[0] and not vlid5[1] and not vlid5[2]):
                moves.append([i,j,i-1,j-1])

            if (vlid6[0] and vlid6[1] and not vlid6[2]) or (vlid6[0] and not vlid6[1] and not vlid6[2]):
                moves.append([i,j,i-1,j+1])

            if (vlid7[0] and vlid7[1] and not vlid7[2]) or (vlid7[0] and not vlid7[1] and not vlid7[2]):
                moves.append([i,j,i+1,j-1])

            if (vlid8[0] and vlid8[1] and not vlid8[2]) or (vlid8[0] and not vlid8[1] and not vlid8[2]):
                moves.append([i,j,i+1,j+1])



        if brd[i][j].getPiece().getName().find("Knight") != -1:

            vlid = cm.validateMove(i, j, i-2, j-1, brd)  # upLeft
            vlid2 = cm.validateMove(i, j, i-2, j+1, brd)  # upright
            vlid3 = cm.validateMove(i, j, i-1, j-2, brd)  # leftUp
            vlid4 = cm.validateMove(i, j, i+1, j-2, brd)  # leftDown
            vlid5 = cm.validateMove(i, j, i+2, j-1, brd)  # downLeft
            vlid6 = cm.validateMove(i, j, i+2, j+1, brd)  # downRight
            vlid7 = cm.validateMove(i, j, i+1, j+2, brd)  # rightUp
            vlid8 = cm.validateMove(i, j, i-1, j+2, brd)  # rightDown

            if (vlid[0] and vlid[1] and not vlid[2]) or (vlid[0] and not vlid[1] and not vlid[2]):
                moves.append([i, j, i-2, j-1])# upLeft

            if (vlid2[0] and vlid2[1] and not vlid2[2]) or (vlid2[0] and not vlid2[1] and not vlid2[2]):
                moves.append([i, j, i-2, j+1]) # upright

            if (vlid3[0] and vlid3[1] and not vlid3[2]) or (vlid3[0] and not vlid3[1] and not vlid3[2]):
                moves.append([i, j, i-1, j-2])# leftUp

            if (vlid4[0] and vlid4[1] and not vlid4[2]) or (vlid4[0] and not vlid4[1] and not vlid4[2]):
                moves.append([i, j, i+1, j-2]) # leftDown

            if (vlid5[0] and vlid5[1] and not vlid5[2]) or (vlid5[0] and not vlid5[1] and not vlid5[2]):
                moves.append([i, j, i+2, j-1])# downLeft

            if (vlid6[0] and vlid6[1] and not vlid6[2]) or (vlid6[0] and not vlid6[1] and not vlid6[2]):
                moves.append([i, j, i+2, j+1])# downRight

            if (vlid7[0] and vlid7[1] and not vlid7[2]) or (vlid7[0] and not vlid7[1] and not vlid7[2]):
                moves.append([i, j, i+1, j+2])# rightUp

            if (vlid8[0] and vlid8[1] and not vlid8[2]) or (vlid8[0] and not vlid8[1] and not vlid8[2]):
                moves.append([i, j, i-1, j+2])# rightDown


        if brd[i][j].getPiece().getName().find("Queen") != -1:
            moves = BQR(1,1,brd,i,j,moves)


        if brd[i][j].getPiece().getName().find("Rook") != -1:
            moves = BQR(0,1,brd,i,j,moves)


        if brd[i][j].getPiece().getName().find("Bishop") != -1:
            moves = BQR(1,0,brd,i,j,moves)

    return moves


#Used in 'getAllMoves' method to get moves of Queen Bishop and Rook
def BQR(cross, plus, brd, i, j, mvs):


    if cross == 1:

        #upLeft
        it=1
        jt=1
        while True:
            vld = cm.validateMove(i,j,i - it,j - jt,brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i,j,i - it,j - jt])
                it = it +1
                jt = jt +1
            else:
                break

        # upRight
        it = 1
        jt = 1
        while True:
            vld = cm.validateMove(i, j, i - it, j + jt, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i - it, j + jt])
                it = it + 1
                jt = jt + 1
            else:
                break

        # downRight
        it = 1
        jt = 1
        while True:
            vld = cm.validateMove(i, j, i + it, j + jt, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i + it, j + jt])
                it = it + 1
                jt = jt + 1
            else:
                break

        # downLeft
        it = 1
        jt = 1
        while True:
            vld = cm.validateMove(i, j, i + it, j - jt, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i + it, j - jt])
                it = it + 1
                jt = jt + 1
            else:
                break





    elif plus == 1:

        # down
        it = 1
        while True:
            vld = cm.validateMove(i, j, i + it, j, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i + it, j])
                it = it + 1
            else:
                break

        # up
        it = 1
        while True:
            vld = cm.validateMove(i, j, i - it, j, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i - it, j])
                it = it + 1
            else:
                break

        # Left
        jt = 1
        while True:
            vld = cm.validateMove(i, j, i, j+jt, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i, j+jt])
                jt = jt + 1
            else:
                break

        # Right
        jt = 1
        while True:
            vld = cm.validateMove(i, j, i, j-jt, brd)
            if (vld[0] and vld[1] and not vld[2]) or (vld[0] and not vld[1] and not vld[2]):
                mvs.append([i, j, i, j-jt])
                jt = jt + 1
            else:
                break

    return mvs


#To move a Piece from Ai,Aj to Bi,Bj
def movePes(Ai, Aj, Bi, Bj,brd):
    p = brd[Bi][Bj].getPiece()
    brd[Bi][Bj].setPiece(brd[Ai][Aj].getPiece())
    brd[Ai][Aj].setPiece(None)

    return brd


#Heuristics (evaluation function)
def heuristicate(brd, ta , tb):

    score  = 0

    quen = 0
    bishp = 0
    rook=0

    oquen = 0
    obishp = 0
    orook = 0

    k = []
    q = []

    ok = []
    oq =[]

    for i in range(len(brd)):
        for m in range(len(brd)):
            j = brd[i][m]
            if j.getPiece() != None:
                a = j.getPiece().getName()
                b = j.getPiece().getTeam().getName()
                if b == tb:
                    if a.find("Bishop")!=-1:
                        score = score+3
                        bishp = bishp +1

                    if a.find("Rook")!=-1:
                        score = score+50
                        rook = rook +1

                    if a.find("Knight")!=-1:
                        score = score+3

                    if a.find("Queen")!=-1:
                        score = score+15
                        q.append(i)
                        q.append(m)
                        quen=1

                    if a.find("Pawn")!=-1:
                        score = score + 1

                    if a.find("King")!=-1:
                        score = score + 5
                        k.append(i)
                        k.append(m)

                if b == ta:
                    if a.find("Bishop") != -1:
                        score = score - 3
                        obishp = obishp + 1

                    if a.find("Rook") != -1:
                        score = score - 2
                        orook = orook + 1

                    if a.find("Knight") != -1:
                        score = score - 2

                    if a.find("Queen") != -1:
                        score = score - 25
                        oq.append(i)
                        oq.append(m)
                        oquen=1

                    if a.find("Pawn") != -1:
                        score = score - 1


                    if a.find("King") != -1:
                        score = score - 5
                        ok.append(i)
                        ok.append(m)


    #if Ai queen and opponent queen present
    if quen==0: score = score - 2
    if oquen == 0: score = score + 3

    #both kings are present or not
    if len(k) == 2:
        score=score+50
    else:
        score=score-99999
    if len(ok) == 2:
        score = score - 30
    else:
        score=score+999999

    #if Bishops on both sides are present
    if bishp > 0:
        score = score + (bishp*1)

    if obishp > 0:
        score = score - (obishp*1)



    return score


#MEthod that check if the given board is a winning board
def isWin(brd):
    king=0
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j].getPiece() !=None:
                if brd[i][j].getPiece().getName().find("King")!=-1:
                    king = king + 1

    if king == 2:
        return False
    else:
        return True

#MEthod that checks if the given board is a TIE board
def isTie(brd):
    king=0
    other=0
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j].getPiece() !=None:
                if brd[i][j].getPiece().getName().find("King")!=-1:
                    king = king + 1
                else:
                    other= other +1

    if king==2 and other == 0:
        return True
    else:
        return False

#global variables
tempb = None
alphaOut = -999999
betaOut = 999999
vl = -999999
depthV = 5


#Actual minimax function----------------------------------------------------------------------
def Minimax(depth, brd, minimaxturn,pA,pB,alpha,beta):


    #BaseCases
    if depth == 0:
        global nodes
        nodes = nodes+ 1
        sc = heuristicate(brd,pA.getName(),pB.getName())
        return sc
    elif isWin(brd):
        return 9999999
    elif isTie(brd):
        return -9999999

    #score initialization
    score = 0

    #min:0
    #max:1

    #Turn flippers
    if minimaxturn == 1:
        minimaxturn =0
        score = 9999999
    elif minimaxturn == 0:
        minimaxturn = 1
        score = -9999999

    brd.reverse()
    for i in brd:
        i.reverse()

    #getting all the possible moves
    if minimaxturn==0:
        pcsPos = getPositions(brd,pB.getName())
    else:
        pcsPos = getPositions(brd,pA.getName())

    mvs =  getAllMoves(brd, pcsPos)


    #Running loop on all possible moves for Minimax with Alpha beta prunning
    for i in mvs:

        tempBrd = deepcopy(brd)
        tempBrd = movePes(i[0],i[1],i[2],i[3],tempBrd)

        if minimaxturn == 0:
            tscore = Minimax(depth-1,tempBrd,minimaxturn,pA,pB,alpha,beta)
            score = min(tscore,score)
            beta = min(score,beta)
            if alpha>=beta:
                break

        elif minimaxturn==1:
            tscore = Minimax(depth-1,tempBrd,minimaxturn,pA,pB,alpha,beta)
            score = max(tscore, score)
            alpha=max(score,alpha)
            if alpha>=beta:
                break

    #Selecting the best board one layer deep
    if depth == (depthV-1) :
        global vl
        global tempb
        if score>vl:
            vl = score
            tempb = deepcopy(brd)




    return score  # Score Minimum or maximum valus



#Method for operating minimax fucntion from outside of this file
def performMinimax(brd, teamA, teamB):
    global tempb
    global vl
    global alphaOut
    global betaOut
    vl=-500
    alphaOut = -999999
    betaOut = 999999

    Minimax(depthV, brd, 0, teamA, teamB, alphaOut, betaOut)


    return tempb
