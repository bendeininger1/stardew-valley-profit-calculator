import pandas as pd
import multipliers
import numpy as np

def harvest_calculation(seed,crop_count,farming_skills,fertilizer,current_season,current_day):

    days_to_grow = seed.days_to_grow
    regrowth_days = seed.regrowth_days
    ###farming skills stuff yet not implemented yet
    harvest_multiplier=seed.harvest_multiplier
    quality_multiplier_first_crop=fertilizer.quality_multiplier_first_crop
    quality_multiplier_other_crops=fertilizer.quality_multiplier_other_crops
    seed_price=seed.seed_price
    crop_price = seed.crop_price
    growing_seasons = seed.growing_seasons
    ###based on fertilizer choice... needs to be implemented
    ###also implement if converting items to wine, jam, this value = 0
    
    print(seed.crop_name)
    print('current season '+str(current_season))
    #prints
    #print('days_to_grow '+str(days_to_grow))
    
    def sell_crops():
        revenue_from_first_crop = crop_count * crop_price * quality_multiplier_first_crop
        revenue_from_other_crops=0
        if harvest_multiplier != 1.0:
            revenue_from_other_crops = crop_count * crop_price * (harvest_multiplier-1) * quality_multiplier_other_crops
        total_crop_sale_revenue = revenue_from_first_crop + revenue_from_other_crops
        return(total_crop_sale_revenue)
        #total_revenue += total_revenue +sell_crops 
    
    #quality_multiplier = quality_multiplier_first_crop
    if current_season not in growing_seasons:
        print('Cannot plant this in this season')
        days_remaining = 0
    elif current_season == growing_seasons[-1]:
        days_remaining = 28 - current_day
    elif current_season == growing_seasons[0]:
        days_remaining = len(growing_seasons)*28-current_day
        print('multi season path 1')
    elif current_season == growing_seasons[1]:
        days_remaining = (len(growing_seasons)-1)*28-current_day
        print('multi season path 2')
    elif current_season == growing_seasons[2]:
        days_remaining = (len(growing_seasons)-2)*28-current_day
        print('multi season path 3')
    #print(str(days_remaining)+' days remaining')
    display_day = current_day 
    total_crops_grown=0.0
    total_expense=float(crop_count*seed_price*2*1)+ fertilizer.cost#2* because price is player sell price.  Players buy at 2x this 
    '''
    if fertilizer.purchase_fertilizer == True:
        total_expense = total_expense + fertilizer.cost
        '''
    total_revenue=0.0
    total_profit=total_revenue-total_expense
    average_profit=float(0.0)
    days_elapsed=0
    day=1
    ###Replace the above values with the lists below and rename the lists
    '''
    display_day_list=[]
    day_list=[]
    days_elapsed_list=[]#used for graphing proifts
    days_remaining_list=[]
    total_profit_list=[]
    total_expense_list=[]
    total_expense_list_negative=[]
    total_revenue_list=[]
    average_profit_list=[]
    '''
    #values=[]
    data = np.array([[day,total_revenue,'Total Revenue',seed.crop_name],
                     [day,total_expense*-1.0,'Total Expenses Negative',seed.crop_name],
                     [day,total_profit,'Total Profit',seed.crop_name],
                     [day,average_profit,'Average Profits',seed.crop_name]])
    #print('regrowth days ' +str(regrowth_days))
    while days_remaining >= 0:
        if regrowth_days == -1:#crops that dont regrow
            if (days_elapsed != 0) and (days_elapsed % days_to_grow==0):
                total_crops_grown = total_crops_grown + crop_count *harvest_multiplier
                if days_remaining>days_to_grow:#dont plant if they there is not enough time to 
                    #print('no grow anymore '+str(days_remaining)+' days remaining')
                    total_expense = total_expense + crop_count*seed_price*2
                total_revenue = total_revenue + sell_crops()
                total_profit = total_revenue - total_expense
                #print('1')
        else:#crops that do regrow
            if days_elapsed == days_to_grow:
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = total_revenue + sell_crops()
                total_profit = total_revenue - total_expense
                #print('2')
            
            elif ((days_elapsed>=days_to_grow) and (days_elapsed-days_to_grow)% regrowth_days== 0):
                #print(str(days_elapsed-days_to_grow)+' days_elapsed-days_to_grow')
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = total_revenue + sell_crops()
                total_profit = total_revenue - total_expense    
                #print('3')
        #extra crops calculations (they are not impact by quality fertilizer)
        
        ## average profits section
        average_profit=float(total_profit)/float(day)
        '''
       
        if regrowth_days>0:#multiple harvests
            if days_remaining<regrowth_days:#no more harvests
                pass
            else:
                average_profit=float(total_profit)/day
        else:#if no new plants are planted, average_profits won't change.
            if days_remaining<days_to_grow-1:#dont plant if they there is not enough time to, but still make the last harvest (the -1)
                pass
            else:
                average_profit=float(total_profit)/day
        '''
        '''
        #print('days elapsed '+ str(days_elapsed))
        day_list.append(day)
        days_elapsed_list.append(days_elapsed)#used for graphing proifts
        days_remaining_list.append(days_remaining)
        total_profit_list.append(total_profit)
        total_expense_list.append(total_expense)
        total_revenue_list.append(total_revenue)
        total_expense_list_negative.append(-total_expense)
        average_profit_list.append(average_profit)
        display_day_list.append(display_day)
        '''
        
        data = np.append(data,[[day,round(total_revenue,2),'Total Revenue',seed.crop_name],
                     [day,round(total_expense*-1),'Total Expenses Negative',seed.crop_name],
                     [day,round(total_profit),'Total Profit',seed.crop_name],
                     [day,round(average_profit,2),'Average Profits',seed.crop_name]],axis=0)
        #data = np.array([[day,'Total Revenue'],[day,'Total Expenses Negative'],[day,'Total Profit']])        
        days_remaining += -1
        display_day += 1
        day+=1
        
        days_elapsed += 1

    df=pd.DataFrame(data,columns=['Day','Values','Finance Category','Crop'])
    #sorts array
    #df.Day=pd.to_numeric(df.Day, errors='coerce')
    #df.sort_values(by=['Finance Category','Day'],inplace=True)
    return(df)
    

if __name__ == '__main__':
    import classes
    import plotly.express as px
 
    soil_type='Basic Fertilizer'
    purchase_fertilizer=True
    farming_level=1
    farming_skills='None'
    current_season='spring'
    current_day=1
    crop_count=1
    seed=classes.SeedSelection('472')
    fertilizer=classes.Fertilizer(soil_type, purchase_fertilizer, farming_level)
    df=harvest_calculation(seed,crop_count,farming_skills,fertilizer,current_season,current_day)
    '''
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    '''
    #print(df.values)
    #print(df.dtypes)
    
    
    
    
    
    
    
    
    
    
    