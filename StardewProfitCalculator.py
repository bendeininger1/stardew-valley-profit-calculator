import json
import math
import numpy as np
import matplotlib.pyplot as plt
import classes
import data_import
import multipliers
import harvest




###create an object that has the stuff needed to calc for each crop

'''
def extra_harvest(min_harvest,max_harvest,max_harvest_increase_per_farming_level,chance_for_extra_crops,farming_level):
    if min_harvest >1 and max_harvest >1:
        min(min_harvest + 1,max_harvest + 1 + farming_level/max_harvest_increase_per_farming_level)
    if chance_for_extra_crops > 0.0:
'''

###Main
#inputs, make this so there can be up to x amount of crops?
farming_level_input = 10 #int from 0 to 13
tiller_input = False #True or False
artisan_input = False #True or False
agriculturist_input = False #True or False
current_day = 1 #int from 1 to 28
current_season = 'spring' #string 'spring', 'summer', 'fall, 'winter'
#money_input = 100000.0 #float, but will only allow them to enter ints
plant_count_input = 1 #int
seed1input=['474',plant_count_input]
seed2input=['475',plant_count_input]

#crop1=classes.SeedSelection()

quality_multiplier_value=multipliers.quality_multiplier(farming_level_input)
seed1 = classes.SeedSelection(seed1input[0],seed1input[1])

print(data_import.crops[seed1input[0]])
print(str(seed1.seed_name)+' seed_name')
print(str(seed1.crop_name)+' crop_name')
print(str(seed1.crop_count)+' crop_count')
print(str(seed1.harvest_multiplier)+' harvest_multiplier')
print(str(seed1.seed_price)+' seed_price')
print(str(seed1.crop_price)+' crop_price')
print(str(seed1.days_to_grow)+' days_to_grow')
print(str(seed1.regrowth_days)+' regrowth_days')
print(str(seed1.growing_seasons)+' growing_seasons')
print('''
      Calculation''')

plot_points_seed1=harvest.harvest_calculation(seed1.crop_count,
                                      seed1.days_to_grow,
                                      seed1.regrowth_days,
                                      agriculturist_input,
                                      seed1.harvest_multiplier,
                                      quality_multiplier_value,
                                      seed1.seed_price,
                                      seed1.crop_price,
                                      1,
                                      seed1.growing_seasons,
                                      current_season,
                                      current_day)


plt.figure()
plt.subplot(211,ylabel='Total Profits')
plt.title('Profit Calculations of '+str(seed1.crop_name))
plt.plot(plot_points_seed1[0],plot_points_seed1[1],'g',plot_points_seed1[0],plot_points_seed1[2],'b',plot_points_seed1[0],plot_points_seed1[3],'r')

plt.subplot(212,ylabel='Average Profits',xlabel='Day')
plt.plot(plot_points_seed1[0],plot_points_seed1[4],'b')
plt.show()


