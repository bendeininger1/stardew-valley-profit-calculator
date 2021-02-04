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
        self.seed_number = int(seed_number)
        self.crop_count = crop_count 
        self.seed_name = data_import.ObjectInformation[seed_number][0]
        self.crop_name = data_import.ObjectInformation[data_import.crops[seed_number][3]][0]
        self.harvest_multiplier = multipliers.average_harvest_yield(seed_number)
        self.seed_price = int(data_import.ObjectInformation[seed_number][1])
        self.crop_price = int(data_import.ObjectInformation[data_import.crops[seed_number][3]][1])
        self.days_to_grow = int(data_import.crops[seed_number][0])
        self.regrowth_days = int(data_import.crops[seed_number][4])
        self.growing_seasons =data_import.crops[seed_number][1] #growing_seasons #['spring']
        ### need to add seed1.quality_multiplier
class Fertilizer:
    def __init__(self,
                soil_type,
                purchase_fertilizer,
                farming_level,
                quality_multiplier_first_crop=None,
                quality_multiplier_other_crops=None,
                deluxe_speed_gro_location='Pierres',
                cost=0.0,
                growth_multiplier=1.0):
        self.soil_type=soil_type
        self.quality_multiplier_first_crop=multipliers.quality_multiplier(farming_level,soil_type)[0]
        self.quality_multiplier_other_crops=multipliers.quality_multiplier(farming_level,soil_type)[1]
        self.purchase_fertilizer=purchase_fertilizer
        self.farming_level=farming_level
        if True == True:
            if soil_type == 'Basic Fertilizer':
                self.cost = 100.0
            elif soil_type == 'Quality Fertilizer':
                self.cost = 150.0
            elif soil_type == 'Deluxe Fertilizer':
                pass
                #can't buy 'Deluxe Fertilizer'
            elif soil_type == 'Speed-Gro':
                self.growth_multiplier = 1.1
                self.cost = 20.0
            elif soil_type == 'Deluxe Speed-Gro':
                self.growth_multiplier = 1.25
                if deluxe_speed_gro_location=='Oasis':
                    self.cost = 80.0
                else:
                    self.cost = 150.0
            elif soil_type == 'Hyper Speed-Gro':
                self.growth_multiplier = 1.33
                #can't buy 'Hyper Speed-Gro'
            elif soil_type == 'None':
                self.cost = 0.0
                self.quality_multiplier_first_crop=multipliers.quality_multiplier(farming_level,soil_type)[0]
            else:
                raise Exception("Wrong Fertilizer Selected from fertilizer class")
        if purchase_fertilizer == False:
            self.cost = 0.0
            print('poopy')

        
        
        
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