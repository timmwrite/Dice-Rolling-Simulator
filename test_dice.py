import unittest
import dice

class TestDice(unittest.TestCase):
    
    def test_result_in_expected_range(self):
        expected_range = range(0, 6)
        self.assertIn(dice.rand(), expected_range)    

    def test_result_not_zero(self):
        self.assertNotEqual(dice.rand(), 0) 

if __name__ == '__main__':
    unittest.main()