import unittest
from point import Point
from covertree import CoverTree, Node
from cheap import CHeap
from cpoint import CPoint

class TestCoverTreeNode(unittest.TestCase):
    def testNewNode(self):
        p = Point([3,4])
        n = Node(p)
        n = Node(p,10)
        
class TestCoverTree(unittest.TestCase):
    def testNewCT(self):
        ct = CoverTree()
        self.assertEqual(ct.root, None)
        ct = CoverTree(3)
        self.assertEqual(ct.tau, 3)
        ct = CoverTree(3,2,4)
        self.assertEqual(ct.tau, 3)
        self.assertEqual(ct.cp, 2)
        self.assertEqual(ct.cc, 4)

    def testLevelOf(self):
        ct = CoverTree()
        input_coords = [[0], [64], [32], [16], [8], [4], [2], [1]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        perm = h.makePerm()
        test = ct.levelof(perm[1])>ct.levelof(perm[2])
        self.assertEqual(test, True)

    def testCTInit(self):
        ct = CoverTree()
        p = Point([3,4])
        ct.insert(p)
        r = ct.root
        self.assertEqual(r.point, p)
        self.assertEqual(r.level, None)
        self.assertEqual(r.isleaf(),True)

    def testCTwith2points(self):
        # Make some points 
        p = Point([3,4])
        q = Point([1,1])
        q.updatepred(p)
        
        # Make a covertree
        ct = CoverTree()
        ct.insert(p)
        ct.insert(q)
        r = ct.root
        
        # The root should be p
        self.assertEqual(r.point, p)
        # The root should have 2 children
        self.assertEqual(len(r.ch), 2)
        # The children should have points 1 and 2
        self.assertEqual({r.ch[0].point, r.ch[1].point}, {p,q})
        # Updated leaves points to new p
        self.assertEqual(ct.leaves[p].level, ct.leaves[q].level)
    
    def testCTwith3points(self):
        #get permutation
        input_coords = [[0], [64], [32], [16], [8], [4], [2], [1]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        perm = h.makePerm()

        ct = CoverTree()
        ct.insert(perm[0])
        ct.insert(perm[1])
        ct.insert(perm[4])
        r = ct.root

        self.assertEqual(r.point, perm[0])
        self.assertEqual(r.level, 7)
        self.assertEqual({r.ch[0].point, r.ch[1].point}, {perm[0],perm[1]})

        lowRoot = ct.leaves[perm[0]]
        self.assertEqual(lowRoot.level, 3)
        lowRootPar = lowRoot.par
        self.assertEqual(lowRootPar.point, perm[0])
        self.assertEqual(lowRootPar.level, 4)

    def testBuildCT(self):
        input_coords = [[3,4], [1,1], [2,0] , [2,4], [10,2], [9, 3], [8,5]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        perm = h.makePerm()
#        for p in perm:
#            print(p)
        ct = CoverTree()
        ct.build(perm)
        r = ct.root

        
        
        
if __name__ == "__main__":
    unittest.main()
