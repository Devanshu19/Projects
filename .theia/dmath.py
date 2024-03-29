import math

#Calculates 'num' raise to the power of 'power'
def getPower(num, power):
        if power == 0:
            return 1
        
        return num * getPower(num, power - 1)

def getSide_RighiTriangle(side, hypo):
    return math.sqrt(getPower(hypo, 2) - getPower(side, 2))

def getHypo_RightTriangle(side1, side2):
    return math.sqrt(getPower(side1, 2) + getPower(side2, 2))