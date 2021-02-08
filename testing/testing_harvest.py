import unittest
import harvest

class TestInputs(unittest.TestCase):
    
    def test_inputs(self):
        self.assertEqual(input_checkers.input_value_crop(None,'spring'),'472','Should be 472')
    
        
if __name__ == '__main__':
    unittest.main()

    
    