import math
from point import Point
from operator import attrgetter


#t is our tao constant
#sf is scalefactor
#g heap is our greedy permutation

class Node:
    def __init__(self, point, level = None):
        self.point = point
        self.level = level
        self.par = None
        self.ch = []
        self.rel = []
        
    def attachparent(self, parent):
        self.par = parent
        if self.point == parent.point:
            parent.ch.insert(0,self)
        else:
            parent.ch.append(self)
        
    def child(self):
        if not self.isleaf():
            return self.ch[0]
        else:
            return None
    
    def isleaf(self):
        return len(self.ch) == 0

    def dis(self,node):
        return self.point.distsq(node.point)

class CoverTree:
    def __init__(self, tau = 2, cp = 1, cc = 1):
        self.tau = tau
        self.cp = cp
        self.cc = cc
        self.root = None
        self.leaves = dict()

    def build(self, permutation):
        for p in permutation:
            self.insert(p)
    
    def insert(self, point):
        if self.root == None:
            self.root = Node(point)
            self.leaves[point] = self.root
        else:
            prednode = self.leaves[point.pred]
            level = self.levelof(point)
            newnode = Node(point, level)
            if prednode.level == None:
                prednode.level = level+1
            if prednode.level == level:
                #finds new prednode, which is really the new parent
                prednode = self.findParent(newnode, prednode)
            if prednode.level > level + 1:
                prednode = self.newleaf(prednode, level+1)
                self.skipRelatives(prednode)
            self.insertbelow(newnode, prednode)
            self.updateRelatives(newnode)
                
    #if prednode on same leve, I call this to find parent.
    #it goes to the relatives of prednode,
    #finds the distance between new node and relaatives paren
    #returns sucha parent with shortest dist
            
    def findParent(self, newnode, prednode):
        parent = prednode.par
        parDis = parent.dis(newnode)
        for rel in prednode.par.rel:
            testDis = rel.dis(newnode) 
            if testDis < parDis:
                parDis = testDis
                parent = rel
        return parent
 
    
# may be faster, but may be incorrect

 #   def findParent(self, newnode, prednode):
#        parent = min(prednode.par, key = lambda p: p.rel.dis(newnode))
#        return(parent)

       

    def insertbelow(self, newnode, oldnode):
        level = newnode.level
        self.newleaf(oldnode,level)
        newnode.attachparent(oldnode)
        self.leaves[newnode.point] = newnode
        
    def newleaf(self, parent, level):
        newnode = Node(parent.point, level)
        newnode.attachparent(parent)
        self.leaves[parent.point] = newnode
        return newnode
    
    def levelof(self, point):
        return math.ceil(math.log(point.dis, self.tau)/2)

    def relativeConstant(self):
        return (3*self.cc*self.tau**2)/(self.tau-1)**2

    def compConstant(self, rc, lvl):
        return rc*(self.tau**lvl)
    
    def skipRelatives(self,node):
        rc = self.relativeConstant()
        cc = self.compConstant(rc, node.level)
        potentialRel = node.par.par.ch
        for child in potentialRel:
            if child.dis(node) <= cc:
                child.rel.append(node)
            
    def updateRelatives(self, node):
        parent = node.par
        level = node.level
        rc = self.relativeConstant()
        cc = self.compConstant(rc, level)
        if parent == None:
            pass
        for child in parent.ch:
            if child.point.distsq(node.point) <= cc:
                self.addRelative(node, child)

    def addRelative(self, node, child):
        if node != child:
            node.rel.append(child)
            child.rel.append(node)
                
        
        

