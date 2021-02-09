import unittest
import harvest
import classes
import plotly.express as px

class TestInputs(unittest.TestCase):
    
    def test_harvest_calculation(self):
        self.assertEqual(input_checkers.input_value_crop(None,'spring'),'472','Should be 472')
    
        
if __name__ == '__main__':
    unittest.main()

    
    