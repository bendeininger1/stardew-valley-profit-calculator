import unittest
import classes



class TestFertilizer(unittest.TestCase):
    
    def test_cost(self):
        self.assertEqual(classes.Fertilizer('Basic Fertilizer',0,0).cost,0.0)
        self.assertEqual(classes.Fertilizer('Basic Fertilizer',1,0).cost,100.0)
        self.assertEqual(classes.Fertilizer('Quality Fertilizer',1,0).cost,150.0)
        self.assertEqual(classes.Fertilizer('Deluxe Fertilizer',1,0).cost,0.0)
        self.assertEqual(classes.Fertilizer('Speed-Gro',1,0).cost,20.0)
        self.assertEqual(classes.Fertilizer('Deluxe Speed-Gro',1,0,deluxe_speed_gro_location='Pierres').cost,150.0)
        self.assertEqual(classes.Fertilizer('Deluxe Speed-Gro',1,0,deluxe_speed_gro_location='Oasis').cost,80.0)
        
    def test_growth_multiplier(self):
        self.assertEqual(classes.Fertilizer('Basic Fertilizer',0,0).growth_rate_increase,0.0)
        self.assertEqual(classes.Fertilizer('Quality Fertilizer',1,0).growth_rate_increase,0.0)
        self.assertEqual(classes.Fertilizer('Deluxe Fertilizer',1,0).growth_rate_increase,0.0)
        self.assertEqual(classes.Fertilizer('Speed-Gro',1,0).growth_rate_increase,.1)
        self.assertEqual(classes.Fertilizer('Deluxe Speed-Gro',1,0,deluxe_speed_gro_location='Pierres').growth_rate_increase,.25)
        self.assertEqual(classes.Fertilizer('Deluxe Speed-Gro',1,0,deluxe_speed_gro_location='Oasis').growth_rate_increase,.25)
        self.assertEqual(classes.Fertilizer('Hyper Speed-Gro',1,0,deluxe_speed_gro_location='Pierres').growth_rate_increase,.33)
        self.assertEqual(classes.Fertilizer('Hyper Speed-Gro',1,0,deluxe_speed_gro_location='Oasis').growth_rate_increase,.33)
        
        
        
if __name__ == '__main__':
    unittest.main()

    
    