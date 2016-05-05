from point import Point
from cpoint import CPoint

class Permutation():
    def __init__(self):
        self.perm = []

    def addpoint(self, cpoint):
        if cpoint.pred == None:
            self.perm.append(Point(cpoint.pt))
        else:
            for p in self.perm:
                if cpoint.pred.pt == p.pt:
                    self.perm.append(Point(cpoint.pt, cpoint.distsq(p), p))

    def minDis(self, cpoint):
        minDis = float('inf')
        for p in self.perm:
            minDis = min(cpoint.distsq(p),minDis)
        return minDis
            
    
        
