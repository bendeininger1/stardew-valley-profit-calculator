import unittest
import harvest
import classes
import plotly.express as px

class Test(unittest.TestCase):
    '''
    def test_days_to_grow_blue_jazz(self):
        #https://stardewcommunitywiki.com/Blue_Jazz
        seed=classes.SeedSelection('429')
        combinations_list=[[None, 'None',7],
                           [None,'Speed-Gro',6],
                           [None,'Deluxe Speed-Gro',5],
                           ['Agriculturist','Speed-Gro',5],
                           ['Agriculturist','Deluxe Speed-Gro',4]]
        for i in range(len(combinations_list)):
            self.assertEqual(harvest.harvest_calculation(seed=seed,
                                                         crop_count=1,
                                                         farming_skills=combinations_list[i][0],
                                                         fertilizer=classes.Fertilizer(combinations_list[i][1], True, 0),
                                                         current_season='spring',
                                                         current_day=1)[1],combinations_list[i][2])
    '''
    ### add base cases of no fertilizer or Agricultarlist skill
    def test_days_to_grow_calc_cali(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]
        
        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,4,4,1]
        correct_days_to_grow=[10,9,9,8]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])
    
    def test_days_to_grow_calc_ancient_fruit(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[2,7,7,7,5]
        correct_days_to_grow=[25,23,23,23]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])
            
    def test_days_to_grow_calc_kale(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,2,1]
        correct_days_to_grow=[5,4,4,3]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_blue_jazz(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,2,2]
        correct_days_to_grow=[6,5,5,4]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_blueberry(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,3,3,4,2]
        correct_days_to_grow=[11,10,9,9]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_starfruit(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[2,3,2,3,3]
        correct_days_to_grow=[11,10,9,8]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_poppy(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,2,2]
        correct_days_to_grow=[6,5,5,4]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_amaranth(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,2,2]
        correct_days_to_grow=[6,5,5,4]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_cranberries(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,1,1,2]
        correct_days_to_grow=[6,5,5,4]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    def test_days_to_grow_calc_pumpkin(self):
        #grow multiplers based on fertilizer and Agricultarlist skill
        growth_mutiplier = [.1,.2,.25,.35]

        #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
        base_stages=[1,2,3,4,3]
        correct_days_to_grow=[11,10,9,9]
        for i in range(len(growth_mutiplier)):
            self.assertEqual(harvest.days_to_grow_calc(base_stages,growth_mutiplier[i]),correct_days_to_grow[i])

    
        
if __name__ == '__main__':
    unittest.main()

    
    