'''harvest.py
This script is where the actual calculations take place using seed class,
number of crops, farming skills, fertilizer selection, and current day/
season 

'''


import pandas as pd
import multipliers
import numpy as np
import math

def harvest_calculation(seed,crop_count,farming_skills,fertilizer,current_season,current_day):
    
    growth_rate_increase=fertilizer.growth_rate_increase
    base_stages=seed.base_stages
    if farming_skills=='Agriculturist':
        growth_rate_increase+=.1
    #days_to_grow = int(math.floor(seed.days_to_grow*(1/growth_multiplier)))
    days_to_grow=days_to_grow_calc(base_stages, growth_rate_increase)

    
    regrowth_days = seed.regrowth_days
    harvest_multiplier=seed.harvest_multiplier
    quality_multiplier_first_crop=fertilizer.quality_multiplier_first_crop
    quality_multiplier_other_crops=fertilizer.quality_multiplier_other_crops
    ###implement later
    #if farming_skills == Agriculturist
    seed_price=seed.seed_price
    crop_price = seed.crop_price
    growing_seasons = seed.growing_seasons
    display_day = current_day 
    ###also implement if converting items to wine, jam, this value = 0
    
    
    
    def sell_crops():#calculates revenue when crops are sold
        revenue_from_first_crop = crop_count * crop_price * quality_multiplier_first_crop
        revenue_from_other_crops=0
        if harvest_multiplier != 1.0:
            revenue_from_other_crops = crop_count * crop_price * (harvest_multiplier-1) * quality_multiplier_other_crops
        total_crop_sale_revenue = revenue_from_first_crop + revenue_from_other_crops
        return(total_crop_sale_revenue)

    if current_season not in growing_seasons:
        print('Cannot plant this in this season')
        days_remaining = 0
        #seasons come in a list like ['spring'] or ['spring','summer']or ['spring','summer','fall'] etc.  ['spring','fall'] is not possible
    elif current_season == growing_seasons[-1]:#can only grow for the rest of the current season
        days_remaining = 28 - current_day
        
    elif current_season == growing_seasons[0]:#can grow for remainder of this season plus 28 days in each of the other seasons
        days_remaining = len(growing_seasons)*28-current_day
  
    elif current_season == growing_seasons[1]:
        days_remaining = (len(growing_seasons)-1)*28-current_day
  
    elif current_season == growing_seasons[2]:
        days_remaining = (len(growing_seasons)-2)*28-current_day
   
    #initial conditions i.e. days_elapsed == 0
    total_crops_grown=0.0
    total_expense=float(crop_count*seed_price*2*1)+ fertilizer.cost#2* because price is player sell price.  Players buy at 2x this 
    total_revenue=0.0
    total_profit=total_revenue-total_expense
    average_profit=float(0.0)
    days_elapsed=0
    day=1

    while days_remaining >= 0:
        
        #calculate finanical values for crops that dont regrow
        if regrowth_days == -1:
            if (days_elapsed != 0) and (days_elapsed % days_to_grow==0):
                total_crops_grown = total_crops_grown + crop_count *harvest_multiplier
                #dont plant if they there is not enough time remaining to grow
                if days_remaining>days_to_grow:
                    total_expense = round(total_expense + crop_count*seed_price*2,2)
                total_revenue = round(total_revenue + sell_crops(),2)
                total_profit = round(total_revenue - total_expense,2)
        
        #calculate finanical values for crops that regrow
        else:
            if days_elapsed == days_to_grow:
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = round(total_revenue + sell_crops(),2)
                total_profit = round(total_revenue - total_expense,2)
            
            elif ((days_elapsed>=days_to_grow) and (days_elapsed-days_to_grow)% regrowth_days== 0):
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = round(total_revenue + sell_crops(),2)
                total_profit = round(total_revenue - total_expense,2)
                
        
        ## average profits section
        average_profit=round(float(total_profit)/float(day),2)
        
        #store finanical information in np array and update array as needed
        if day==1:
            #np array that is used to store the harvest calculations
            data = np.array([[day,total_revenue,'Revenue',seed.crop_name,'Revenue '+str(seed.crop_name)],
                             [day,total_expense*-1.0,'Expenses',seed.crop_name,'Expenses '+str(seed.crop_name)],
                             [day,total_profit,'Profit',seed.crop_name,'Profit '+str(seed.crop_name)],
                             [day,average_profit,'Avg Profits',seed.crop_name,'Avg Profits '+str(seed.crop_name)]])
        else:
            #add new harvest data to np array
            data = np.append(data,[[day,total_revenue,'Revenue',seed.crop_name,'Revenue '+str(seed.crop_name)],
                                   [day,total_expense*-1.0,'Expenses',seed.crop_name,'Expenses '+str(seed.crop_name)],
                                   [day,total_profit,'Profit',seed.crop_name,'Profit '+str(seed.crop_name)],
                                   [day,average_profit,'Avg Profits',seed.crop_name,'Avg Profits '+str(seed.crop_name)]],axis=0)
        #increment
        days_remaining += -1
        display_day += 1
        day+=1
        days_elapsed += 1
    #create pandas DataFrame uing np array.  This is needed for the web app.
    
    df=pd.DataFrame(data,columns=['Day','Values','Finance Category','Crop','Finance Category of Crop'])
    
    return(df,days_to_grow)
    

def days_to_grow_calc(base_stages,growth_rate_increase):
    #https://docs.google.com/spreadsheets/d/16vjeFnexYJ4n2Ib_nA9JubB6mvUcJanf9zu0SjpvPSI/edit#gid=770413564
    #base_stages is the number of crop stages from ObjectInformation
    #growth_multiplier is based on fertilizer and if player has Agriculturist skill
    base_number_of_stages=len(base_stages)
    base_days=sum(base_stages)
    #Handle no skills or Speed Grow
    if growth_rate_increase==0.0:
        days_to_grow =base_days
        return(days_to_grow)
    #handle all other cases
    else:
        if base_stages[0]==1:
            x = 1
        else:
            x = 0
        if math.ceil(growth_rate_increase*base_days)>(base_number_of_stages-x):
            days_reduced = base_number_of_stages-x
            days_to_grow = base_days-days_reduced
        else:
            days_reduced = math.ceil(growth_rate_increase*base_days)
            days_to_grow = base_days-days_reduced
        return(days_to_grow)

if __name__ == '__main__':
    
    #blueberry
    growth_rate_increase = [0.0,.1,.25,.2,.35]
    base_stages=[1,3,3,4,2]


    correct_days_to_grow=[13,11,10,9,9]
    for i in range(len(growth_rate_increase)):
        days_to_grow_calc(base_stages,growth_rate_increase[i]),correct_days_to_grow[i]
    
    
    
    
    '''
    import classes
    import plotly.express as px
 
    soil_type='Basic Fertilizer'
    purchase_fertilizer=True
    farming_level=1
    farming_skills='None'
    current_season='spring'
    current_day=1
    crop_count=1
    seed=classes.SeedSelection('429')
    fertilizer=classes.Fertilizer(soil_type, purchase_fertilizer, farming_level)
    df=harvest_calculation(seed,crop_count,farming_skills,fertilizer,current_season,current_day)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    '''
    

    
    
    
    
    
    
    
    
    
    
    