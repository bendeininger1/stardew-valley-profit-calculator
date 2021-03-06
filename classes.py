import data_import
import multipliers


class SeedSelection:
    def __init__(self,
                 seed_number,#
                 seed_name=None,
                 crop_name=None,
                 harvest_multiplier=None,
                 seed_price=None,
                 crop_price=None,
                 base_stages=None,
                 regrowth_days=None,
                 growing_seasons=None):
        
        self.seed_number = int(seed_number)
        self.seed_name = data_import.parsed_object_information[seed_number][0]
        self.crop_name = data_import.parsed_object_information[data_import.parsed_crops[seed_number][3]][0]
        self.harvest_multiplier = multipliers.average_harvest_yield(seed_number)
        self.seed_price = int(data_import.parsed_object_information[seed_number][1])
        self.crop_price = int(data_import.parsed_object_information[data_import.parsed_crops[seed_number][3]][1])
        self.base_stages = data_import.parsed_crops[seed_number][0]
        self.regrowth_days = int(data_import.parsed_crops[seed_number][4])
        self.growing_seasons =data_import.parsed_crops[seed_number][1] #growing_seasons #['spring']
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
                growth_rate_increase=0.0):
        self.cost=cost
        self.growth_rate_increase=growth_rate_increase
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
                self.growth_rate_increase = .1
                self.cost = 20.0
            elif soil_type == 'Deluxe Speed-Gro':
                self.growth_rate_increase = .25
                if deluxe_speed_gro_location=='Oasis':
                    self.cost = 80.0
                else:
                    self.cost = 150.0
            elif soil_type == 'Hyper Speed-Gro':
                self.growth_rate_increase = .33
                #can't buy 'Hyper Speed-Gro'
            elif soil_type == 'None':
                self.cost = 0.0
                self.quality_multiplier_first_crop=multipliers.quality_multiplier(farming_level,soil_type)[0]
            else:
                raise Exception("Wrong Fertilizer Selected from fertilizer class")
        if purchase_fertilizer == False:
            self.cost = 0.0
        
        
        

if __name__ == '__main__':
    print(Fertilizer('Deluxe Fertilizer',1,0).cost)
    '''
    #x=crops
    #print(x)
    #parsed_crops()
    '''
    