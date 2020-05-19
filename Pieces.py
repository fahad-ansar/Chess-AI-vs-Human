#Name: Fahad Ansar
#St#: 6203384


import Team

#individual object classes of pieces

#-------------Pieces------------------
class Bishop:

    def __init__(self, team, cr,nu):
        self.team = team
        self.name = "Bishop"+cr+""+nu

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class King:

    def __init__(self, team, cr,nu):
        self.team = team
        self.name = " King "+cr+""+nu


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Knight:

    def __init__(self, team, cr,nu):
        self.team = team
        self.name = "Knight"+cr+""+nu


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Pawn:

    def __init__(self, team , cr,nu):
        self.team = team
        self.name = " Pawn "+cr+""+nu


    def getName(self):


        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name

        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Queen:

    def __init__(self, team, cr,nu):
        self.team = team
        self.name = " Queen"+cr+""+nu


    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-------------------------------------

class Rook:
    def __init__(self, team, cr,nu):
        self.team = team
        self.name = " Rook "+cr+""+nu

    def getName(self):
        temp = self.team.getName()[0] + self.team.getName()[-1] +"-"+ self.name
        return temp

    def getTeam(self):
        return self.team
#-----------------------------------
#---------Piece-Factory-------------
#Creates a desried piece and returns it as a completed object

class PeiceMkr:

    res = None

    def createPiece(self,name, team, clr, no):
        if name == "B":
            self.res = Bishop(team=team, cr=clr, nu =str(no))
        elif name == "R":
            self.res = Rook(team=team, cr=clr, nu =str(no))
        elif name == "P":
            self.res  = Pawn(team=team, cr=clr, nu =str(no))
        elif name == "Kn":
            self.res  = Knight(team=team, cr=clr, nu =str(no))
        elif name == "K":
            self.res  = King(team=team, cr=clr, nu =str(no))
        elif name == "Q":
            self.res  = Queen(team=team, cr=clr, nu =str(no))

        return self.res

