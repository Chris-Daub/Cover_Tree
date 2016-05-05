import unittest
from point import Point

class TestPoint(unittest.TestCase):
    
    def test_newpoint(self):
        Point([3,4])
        Point([0,0])
        Point([1.23,-3.134])
        Point([0,0,3, 1241, 235402])
    
    def test_dist_sq(self):
        p = Point([3,4])
        q = Point([0,0])
        self.assertEqual(p.distsq(q), 25)
        p = Point([6,6])
        q = Point([2,3])
        self.assertEqual(p.distsq(q), 25)
        p = Point([0,5])
        q = Point([-12,0])
        self.assertEqual(p.distsq(q), 169)
        
    def test_dist(self):
        p = Point([3,4])
        q = Point([0,0])
        self.assertEqual(p.dist(q), 5.0)
        p = Point([6,6])
        q = Point([2,3])
        self.assertEqual(p.dist(q), 5.0)
        p = Point([0,5])
        q = Point([-12,0])
        self.assertEqual(p.dist(q), 13.0)
        
    def test_updatepred(self):
        p = Point([0])
        p.updatepred(Point([100]))
        self.assertEqual(p.dis, 100**2)
        p.updatepred(Point([101]))
        self.assertEqual(p.dis, 100**2)
        p.updatepred(Point([99]))
        self.assertEqual(p.dis, 99**2)

if __name__ == '__main__':
    unittest.main()
