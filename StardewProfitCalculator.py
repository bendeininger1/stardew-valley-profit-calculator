

import json
import math
import numpy as np
import matplotlib.pyplot as plt
import classes
import data_import
import multipliers
import harvest





###Main
#inputs, make this so there can be up to x amount of crops?
farming_level_input = 10 #int from 0 to 13
current_day = 1 #int from 1 to 28
current_season = 'spring' #string 'spring', 'summer', 'fall, 'winter'
current_year = 1
deluxe_speed_gro_location='Pierres'#can be 'Pierres' or 'Oasis'
fertilizer_input ='None'#cant buy 'Hyper Speed-Gro' or 'Deluxe Fertilizer'
fertilizer_buy_input = True #True or False
farming_skills_input = 'Tiller' #None, Tiller, Agriclut, Artisian

#money_input = 100000.0 #float, but will only allow them to enter ints
plant_count_input = 1 #int

###take out of main?
crop_list_keys = list(data_import.crops.keys())
crop_list=[]
for i in range(len(crop_list_keys)):
    crop_list.append({'label':classes.SeedSelection(crop_list_keys[i], 1).crop_name,'value':crop_list_keys[i]})



seedinput=['475',plant_count_input]

#crop1=classes.SeedSelection()

quality_multiplier_value=multipliers.quality_multiplier(farming_level_input,fertilizer_input)

#sets up seed1
seed = classes.SeedSelection(seedinput[0],seedinput[1])
print(seed.crop_name)
#assigns seed1 to a DataFrame
seed_df=harvest.harvest_calculation(seed,farming_skills_input,classes.Fertilizer(fertilizer_input,True,farming_level_input),current_season,current_day)

'''
seed_df=harvest.harvest_calculation(seed.crop_count,
                                    seed.days_to_grow,
                                    seed.regrowth_days,
                                    agriculturist_input,
                                    seed.harvest_multiplier,
                                    quality_multiplier_value,
                                    seed.seed_price,
                                    seed.crop_price,
                                    1,
                                    seed.growing_seasons,
                                    current_season,
                                    current_day)
'''

'''
plt.figure()
plt.subplot(211,ylabel='Total Profits')
plt.title('Profit Calculations of '+str(seed1.crop_name))
plt.plot(plot_points_seed1[0],plot_points_seed1[1],'g',plot_points_seed1[0],plot_points_seed1[2],'b',plot_points_seed1[0],plot_points_seed1[3],'r')

plt.subplot(212,ylabel='Average Profits',xlabel='Day')
plt.plot(plot_points_seed1[0],plot_points_seed1[4],'b')
plt.show()
'''








