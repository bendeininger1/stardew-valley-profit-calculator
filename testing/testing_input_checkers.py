import unittest
import input_checkers

class TestInputs(unittest.TestCase):
    
    def test_inputs(self):
        self.assertEqual(input_checkers.input_value_crop_checker(None,'spring'),'472','Should be 472')
        
    def test_inputs2(self):
        self.assertEqual(input_checkers.input_value_crop_checker(None,'summer'),'479','Should be 479')
    
    def test_inputs3(self):
        self.assertEqual(input_checkers.input_value_crop_checker(None,'fall'),'490','Should be 490')
        
if __name__ == '__main__':
    unittest.main()

    
    