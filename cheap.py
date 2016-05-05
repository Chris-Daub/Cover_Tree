import math
from heapq import heapify, heappush, heappop
from cpoint import CPoint
from permutation import Permutation

class CHeap:
    def __init__(self,cue):
        self.cue = cue   # uninserted points (used to compute keys)
        self.heap = []   # points in the heap
        self.perm = Permutation()   # points already removed (permutation)
        self.eps = float('inf')

    def makePerm(self):
        self.iniHeap(self.cue.pop(0))
        while (len(self.cue) != 0):
            self.insert(self.remove())
        return self.perm.perm
        
    #Initializes Heap
    def iniHeap(self, point):
        for pt in self.cue:
            point.addRNN(pt)
        point.updateKey(point.rnnPeek())
        self.perm.addpoint(point)
        heappush(self.heap,point)
        
    #inserts any point into permutation,
    #inserts point into heap if rnn is not empty
    def insert(self, point):
        self.updateNbrs(point)
        self.newCluster(point)
        self.perm.addpoint(point)
        if not point.rnnIsEmpty():
            point.updateKey(point.rnnPeek())
            heappush(self.heap,point)
            
    #For nbrs of pred,
    #if rnn are closer to self.point,
    #becomes rnn of self.point
    #and also removes nbr from heap if it has no rnn
    def newCluster(self,point):
        for nbr in point.pred.neighbors:
            point.newRNN(nbr)
            if nbr.rnnIsEmpty() and nbr in self.heap:
                self.heap.remove(nbr)
        heapify(self.heap)

    def remove(self):
        top = self.heap[0]
        farthest = top.rnnPop()
        self.cue.remove(farthest)
        farthest.updatepred(top)
        heapify(self.heap)
        return farthest

    #sets epsilon and updates nbrs based on eps
    def updateNbrs(self,point):
        self.setEps(point)
        for p in self.heap:
            if p.distsq(point) < 8*self.eps:
                p.neighbors.append(point)
                point.neighbors.append(p)
#this block may or may not be necessary
#            else:
#                if p in point.neighbors:
#                    point.neighbors.remove(p)
#                if point in p.neighbors:
#                    p.neighbors.remove(point)
            
    def setEps(self, point):
        self.eps = min(self.perm.minDis(point), self.eps)
