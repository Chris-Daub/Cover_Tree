import unittest
from cpoint import CPoint

class TestCPoint(unittest.TestCase):
    
    def test_newpoint(self):
        CPoint([3,4])
        CPoint([0,0])
        CPoint([1.23,-3.134])
        CPoint([0,0,3, 1241, 235402])

    def test_updates(self):
        tpoint = CPoint([0,0])
        a = CPoint([0,2])
        b = CPoint([1,0])
        c = CPoint([3,4])
        
        tpoint.updatePred(a)
        self.assertEqual(tpoint.pred, a)

        tpoint.updateKey(c)
        self.assertEqual(tpoint.dis, 25)
        tpoint.updateKey(b)
        self.assertEqual(tpoint.dis, 1)
        tpoint.updateKey(a)
        self.assertEqual(tpoint.dis, 1)

    def test_addRNN(self):
        tpoint = CPoint([0,3])
        a = CPoint([0,2])
        b = CPoint([1,0])
        c = CPoint([3,5])
        tpoint.addRNN(b)
        tpoint.addRNN(a)
        tpoint.addRNN(c)
#        print(tpoint.rnnPeek())

    def test_rnn_Peek_and_Pop(self):
        tpoint = CPoint([0,3])
        a = CPoint([0,2])
        b = CPoint([1,0])
        c = CPoint([3,5])
        tpoint.addRNN(b)
        tpoint.addRNN(a)
        tpoint.addRNN(c)
        peek = tpoint.rnnPeek()
        self.assertEqual(peek,tpoint.rnnPop())
        if peek == tpoint.rnnPeek():
            self.assertEqual(1,0)

    def test_farthest(self):
        tpoint = CPoint([0,3])
        a = CPoint([0,2])
        b = CPoint([1,0])
        c = CPoint([3,5])
        tpoint.addRNN(b)
        tpoint.addRNN(a)
        tpoint.addRNN(c)
#        print(tpoint.rnnPeek())
        
    def test_newRNN(self):
        tpoint = CPoint([0,3])
        point = CPoint([0,0])
        a = CPoint([0,2])
        b = CPoint([1,0])
        c = CPoint([3,5])
        point.addRNN(b)
        point.addRNN(a)
        point.addRNN(c)
        tpoint.newRNN(point)
        self.assertEqual(len(tpoint.rnn),2)
        self.assertEqual(len(point.rnn),1)
#        print(tpoint.rnnPeek())
#        print(point.rnnPeek())
    
if __name__ == '__main__':
    unittest.main()
