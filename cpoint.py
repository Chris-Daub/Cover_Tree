from point import Point
from heapq import heapify,heappop,heappush


class CPoint(Point):
    def __init__(self,pt):
        Point.__init__(self,pt)
        self.neighbors = [self]
        self.rnn = []

    # overridden: does not change key
    def updatePred(self,pt):
        self.pred=pt

    # sets key only if current key (dis) is bigger.
    def updateKey(self,pt):
        d = self.distsq(pt)
        if d < self.dis or self.dis==0:
            self.dis = d
            
#heap methods
    #adds point to self.rnn in a heap invariant
    def addRNN(self, point):
        point.updateKey(self)
        heappush(self.rnn,point)
        
    #peeks top of RNN. Farthest
    def rnnPeek(self):
        return self.rnn[0]
    #pops farthest and maintains heap
    def rnnPop(self):
        return heappop(self.rnn)
    #is RNN empty?
    def rnnIsEmpty(self):
        return len(self.rnn) == 0
    
    #if RNN of Pt are closer to self, places RNN in self.rnn
    def newRNN(self,pt):
        for rnbr in pt.rnn:
            d = rnbr.dis
            if self.distsq(rnbr) < d:
                pt.rnn.remove(rnbr)
                self.addRNN(rnbr)
        if(len(pt.rnn)!=0):
            heapify(pt.rnn)
            pt.updateKey(pt.rnnPeek())
        
    
           
   
            



    
