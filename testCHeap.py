import unittest
from cpoint import CPoint
from cheap import CHeap
from heapq import heappush

class TestCHeap(unittest.TestCase):

    def test_ini(self):
        input_coords = [[0], [64], [32], [16], [8], [4], [2], [1]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        self.assertEqual(h.cue,cue)
        h.iniHeap(h.cue.pop(0))

    def test_remove(self):
        input_coords = [[0], [64], [1], [4], [16], [8], [2], [32]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        h.iniHeap(h.cue.pop(0))
        node = h.remove()
        if node in h.cue:
            assertEqual(1,0)
#        print(h.heap[0])

    def test_insert(self):
        input_coords = [[20], [64], [1], [4], [16], [8], [2], [32],[65]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        h.iniHeap(h.cue.pop(0))
        print(h.perm.perm[0])


    def test_insert(self):
        input_coords = [[20], [64], [1], [4], [16], [8], [2], [32],[65]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        h.iniHeap(h.cue.pop(0))
        while ( len(h.cue) != 0):
            h.insert(h.remove())
##        print('Heap')
##        for p in h.heap:
##            print(p)
##        print('Perm')
##        for p in h.perm.perm:
##            print(p)

    def test_makePerm(self):
        input_coords = [[20], [64], [1], [4], [16], [8], [2], [32],[65]]
        cue = [CPoint(coords) for coords in input_coords]
        h = CHeap(cue)
        perm = h.makePerm()
#        print('Perm')
#        for p in perm:
#            print(p)

if __name__ == '__main__':
    unittest.main()
