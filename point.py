import math

class Point:

    def __init__(self, pt, dis = 0,pred = None):
        self.pt=pt
        self.dis=dis
        self.pred=pred
        
    @staticmethod
    def normsq(vector):
        return sum([x_i **2 for x_i in vector ])
        
    def distsq(self, other):
        return self.normsq(self - other)

    def dist(self, other):
        return math.sqrt(self.distsq(other))
        
    def updatepred(self, pt):
        d = self.distsq(pt)
        if self.pred == None or d < self.dis:
            self.pred = pt
            self.dis = d
    
    # returns a vector, not a point
    def __sub__(self, other):
        dim = min(len(self.pt), len(other.pt))
        return [self.pt[i] - other.pt[i] for i in range(dim)]
    
    def __lt__(self,other):
        return self.dis>other.dis
        
    def __str__(self):
        return 'pt: %s dis: %s pre: ( %s )'\
               % (self.pt, self.dis, self.pred) 
