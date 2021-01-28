import data_import
import multipliers

class SeedSelection:
    def __init__(self,
                 seed_number,#
                 crop_count,#
                 seed_name=None,
                 crop_name=None,
                 harvest_multiplier=None,
                 seed_price=None,
                 crop_price=None,
                 days_to_grow=None,
                 regrowth_days=None,
                 growing_seasons=None):
        self.seed_number = seed_number
        self.crop_count = crop_count
        
        self.seed_name = data_import.ObjectInformation[seed_number][0]
        self.crop_name = data_import.ObjectInformation[data_import.crops[seed_number][3]][0]
        self.harvest_multiplier = multipliers.average_harvest_yield(seed_number)
        self.seed_price = data_import.ObjectInformation[seed_number][1]
        self.crop_price = data_import.ObjectInformation[data_import.crops[seed_number][3]][1]
        self.days_to_grow = data_import.crops[seed_number][0]
        self.regrowth_days = data_import.crops[seed_number][4]
        self.growing_seasons =data_import.crops[seed_number][1] #growing_seasons #['spring']
        ### need to add seed1.quality_multiplier
    
#runs only when testing and not on load
#if __name__ == '__main__':
        

'''
seed1 = SeedSelection(data_import.parsed_object_information[seed1input[0]][0],
                      ObjectInformation[crops[seed1input[0]][3]][0],
                      seed1input[1],
                      average_harvest_yield(seed1input[0]),
                      ObjectInformation[seed1input[0]][1],
                      ObjectInformation[crops[seed1input[0]][3]][1],
                      crops[seed1input[0]][0],
                      crops[seed1input[0]][4],
                      crops[seed1input[0]][1])
'''
'''
class SeedSelection:
    def __init__(self,
                 seed_name,
                 crop_name,
                 crop_count,
                 harvest_multiplier,
                 seed_price,
                 crop_price,
                 days_to_grow,
                 regrowth_days,
                 growing_seasons):
        self.seed_name = seed_name
        self.crop_name = crop_name
        self.crop_count = crop_count
        self.harvest_multiplier = harvest_multiplier
        self.seed_price = seed_price
        self.crop_price = crop_price
        self.days_to_grow = days_to_grow
        self.regrowth_days = regrowth_days
        self.growing_seasons = growing_seasons
        ### need to add seed1.quality_multiplier
'''