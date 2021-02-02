import pandas as pd
import multipliers

def harvest_calculation(seed,farming_skills,fertilizer,current_season,current_day):
    
        

    crop_count = seed.crop_count
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
        print(harvest_multiplier)
        if harvest_multiplier != 1.0:
            revenue_from_other_crops = crop_count * crop_price * (harvest_multiplier-1) * quality_multiplier_other_crops
        total_crop_sale_revenue = revenue_from_first_crop + revenue_from_other_crops
        print(revenue_from_first_crop,revenue_from_other_crops,total_crop_sale_revenue)
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
    total_expense=float(crop_count*seed_price*2*1)#2* because price is player sell price.  Players buy at 2x this price
    total_revenue=0.0
    total_profit=total_revenue-total_expense
    average_profit=0.0
    days_elapsed=0
    day=1
    ###Replace the above values with the lists below and rename the lists
    
    display_day_list=[]
    day_list=[]
    days_elapsed_list=[]#used for graphing proifts
    days_remaining_list=[]
    total_profit_list=[]
    total_expense_list=[]
    total_expense_list_negative=[]
    total_revenue_list=[]
    average_profit_list=[]
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
        average_profit=float(total_profit)/day
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
        
        days_remaining += -1
        display_day += 1
        day+=1
        
        days_elapsed += 1
        
        #print(days_elapsed_list)
        #print(total_profit_list)
        ### Will need to save this data in a variable.
    #use pandas dataframe to store values
    data={'Display Day':display_day_list,
          'Day':day_list,
          'Days Elapsed':days_elapsed_list,
          'Days Remaining':days_remaining_list,
          'Total Revenue':total_revenue_list,
          'Total Expenses Negative':total_expense_list_negative,
          'Total Profit':total_profit_list,
          'Average Profit':average_profit_list}
    df = pd.DataFrame(data)
    print(df)
    return(df)
    

    #return(days_elapsed_list,total_profit_list,total_revenue_list,total_expense_list_negative,average_profit_list)
#count of harvest if multiple seasons
