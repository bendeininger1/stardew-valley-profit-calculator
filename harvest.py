import pandas as pd

def harvest_calculation(crop_count,
                        days_to_grow,
                        regrowth_days,
                        agriculturist_check,
                        harvest_multiplier,
                        quality_multiplier_value,
                        seed_price,
                        crop_price,
                        fertilizer_multiplier,
                        growing_seasons,
                        current_season,
                        current_day):
    #agricultrualist not implemented
    crop_count = int(crop_count)
    days_to_grow = int(days_to_grow)
    regrowth_days = int(regrowth_days)
    seed_price = int(seed_price)
    crop_price = int(crop_price)
    ###based on fertilizer choice... needs to be implemented
    ###also implement if converting items to wine, jam, this value = 0
    quality_multiplier = quality_multiplier_value[0]
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
    print(str(days_remaining)+' days remaining')
    display_day = current_day 
    total_crops_grown=0.0
    total_expense=float(crop_count*seed_price*2*1)#2* because price is player sell price.  Players buy at 2x this price
    total_revenue=0.0
    total_profit=total_revenue-total_expense
    average_profit=0.0
    days_elapsed=0
    ###Replace the above values with the lists below and rename the lists
    
    days_elapsed_list=[days_elapsed]#used for graphing proifts
    total_profit_list=[total_profit]
    total_expense_list=[total_expense]
    total_expense_list_negative=[-total_expense]
    total_revenue_list=[total_revenue]
    average_profit_list=[average_profit]
    while days_remaining > 0:
        if regrowth_days == -1:#crops that dont regrow
            if days_remaining<days_to_grow:#dont plant if they there is not enough time to 
                pass
            elif (days_elapsed != 0) and (days_elapsed % days_to_grow==0):
                total_crops_grown = total_crops_grown + crop_count *harvest_multiplier
                total_expense = total_expense + crop_count*seed_price*2
                total_revenue = total_revenue + crop_count * crop_price * harvest_multiplier * quality_multiplier
                total_profit = total_revenue - total_expense
                #print('1')
        else:#crops that do regrow
            if days_elapsed == days_to_grow:
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = total_revenue + crop_count * crop_price * harvest_multiplier * quality_multiplier
                total_profit = total_revenue - total_expense
                #print('2')
            
            elif ((days_elapsed>=days_to_grow) and (days_elapsed-days_to_grow)% regrowth_days== 0):
                #print(str(days_elapsed-days_to_grow)+' days_elapsed-days_to_grow')
                total_crops_grown = total_crops_grown + crop_count*harvest_multiplier
                total_revenue = total_revenue + crop_count * crop_price * harvest_multiplier * quality_multiplier
                total_profit = total_revenue - total_expense    
                #print('3')
        days_elapsed += 1
        if days_elapsed==0:#avoid divide by 0
            pass
        else:
            if regrowth_days>0:#multiple harvests
                if days_remaining<regrowth_days:#no more harvests
                    pass
                else:
                    average_profit=float(total_profit)/days_elapsed
            else:#if no new plants are planted, average_profits won't change.
                if days_remaining<days_to_grow:#dont plant if they there is not enough time to
                    pass
                else:
                    average_profit=float(total_profit)/days_elapsed
        days_remaining += -1
        display_day += 1

        days_elapsed_list.append(days_elapsed)#used for graphing proifts
        total_profit_list.append(total_profit)
        total_expense_list.append(total_expense)
        total_revenue_list.append(total_revenue)
        total_expense_list_negative.append(-total_expense)
        average_profit_list.append(average_profit)
        #print(days_elapsed_list)
        #print(total_profit_list)
        ### Will need to save this data in a variable.
    #use pandas dataframe to store values
    data={'Day':days_elapsed_list,
          'Total Profit':total_profit_list,
          'Total Revenue':total_revenue_list,
          'Total Expenses Negative':total_expense_list_negative,
          'Average Profit':average_profit_list}
    df = pd.DataFrame(data)
    print(df)
    return(df)
    #return(days_elapsed_list,total_profit_list,total_revenue_list,total_expense_list_negative,average_profit_list)
#count of harvest if multiple seasons
