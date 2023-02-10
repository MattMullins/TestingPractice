import unittest
from scoringDemo import ScoreMachine

class testAce(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_zeros(self):
        self.assertEqual(self.machine.aces([6,2,3,4,5]), 0, "Should be 0")
    
    def test_aces(self):
        self.assertEqual(self.machine.aces([1,2,3,4,5]), 1, "Should be 1")
        self.assertEqual(self.machine.aces([2,3,4,1,1]), 2, "Should be 2")
        self.assertEqual(self.machine.aces([1,1,1,1,1]), 5, "Should be 5")


class testDeuce(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
    
    def test_deuces(self):
        self.assertEqual(self.machine.deuces([1,2,1,4,5]), 2, "Should be 2")
        self.assertEqual(self.machine.deuces([1,3,1,4,5]), 0, "Should be 0")
        self.assertEqual(self.machine.deuces([1,2,2,4,5]), 4, "Should be 4")
        self.assertEqual(self.machine.deuces([2,2,2,2,2]), 10, "Should be 10")



class testTre(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()
        
    def test_tres(self):
        self.assertEqual(self.machine.tres([1,2,1,4,5]), 0, "Should be 0")
        self.assertEqual(self.machine.tres([1,2,3,4,5]), 3, "Should be 3")
        self.assertEqual(self.machine.tres([1,3,3,3,3]), 12, "Should be 12")
        self.assertEqual(self.machine.tres([3,3,3,3,3]), 15, "Should be 15")



class testQuad(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_quads(self):
        self.assertEqual(self.machine.quads([1,2,1,4,5]), 4, "Should be 4")
        self.assertEqual(self.machine.quads([1,2,1,1,5]), 0, "Should be 0")
        self.assertEqual(self.machine.quads([1,2,4,4,5]), 8, "Should be 8")
        self.assertEqual(self.machine.quads([4,4,4,4,4]), 20, "Should be 20")



class testPenta(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_pentas(self):
        self.assertEqual(self.machine.pentas([1,2,1,4,5]), 5, "Should be 5")
        self.assertEqual(self.machine.pentas([1,2,1,4,1]), 0, "Should be 0")
        self.assertEqual(self.machine.pentas([1,5,1,5,5]), 15, "Should be 15")
        self.assertEqual(self.machine.pentas([5,5,5,5,5]), 25, "Should be 25")



class testHexta(unittest.TestCase):
    
    def setUp(self):
        self.machine = ScoreMachine()

    def test_hextas(self):
        self.assertEqual(self.machine.hextas([1,2,1,4,5]), 0, "Should be 0")
        self.assertEqual(self.machine.hextas([1,2,6,4,5]), 6, "Should be 6")
        self.assertEqual(self.machine.hextas([6,2,6,4,6]), 18, "Should be 18")
        self.assertEqual(self.machine.hextas([6,6,6,6,6]), 30, "Should be 30")



if __name__ == '__main__':
    unittest.main()