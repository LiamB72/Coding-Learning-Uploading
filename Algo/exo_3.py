from math import sqrt
def distance(ptA,ptB):
    xA,yA = ptA
    xB,yB = ptB
    AB = sqrt((xB-xA)**2+(yB-yA)**2)
    return AB

ptA=(1,1)
ptB=(2,2)
print(distance(ptA,ptB))