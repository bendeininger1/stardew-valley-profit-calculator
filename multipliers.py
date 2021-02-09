
def average_harvest_yield(seed_number):
    if int(seed_number) == 475:
        harvest_multiplier = 1.25
    elif int(seed_number) == 273:
        harvest_multiplier = 1.1
    elif int(seed_number) == 745:
        harvest_multiplier = 1.02
    elif int(seed_number) == 480:
        harvest_multiplier = 1.05
    elif int(seed_number) == 481:
        harvest_multiplier = 3.06
    elif int(seed_number) == 482:
        harvest_multiplier = 1.03
    elif int(seed_number) == 433:
        harvest_multiplier = 4.08
    elif int(seed_number) == 488:
        harvest_multiplier = 1.002
    elif int(seed_number) == 493:
        harvest_multiplier = 2.04
    else:
        harvest_multiplier = 1.0
    return (harvest_multiplier)

def quality_multiplier(farming_level,soil_type):
    import constants
    #regular crops are the default sell price (from ObjectInfomration),silver are x1.25,  gold are  x1.5, iridium are 2x
    #values use the sum of (the %freqency for each quality type (normal, gold, silver, idium) mutipled by the sell prices above) for each farming level and for each fertilizer type
 
    quality_price_multipliers=constants.quality_price_multipliers
    normal_quality_price_multipler=quality_price_multipliers[0][farming_level]#reduce references to constants.py
    if soil_type =="Basic Fertilizer":
        return(quality_price_multipliers[1][farming_level],normal_quality_price_multipler)
    if soil_type =="Quality Fertilizer":
        return(quality_price_multipliers[2][farming_level],normal_quality_price_multipler)
    if soil_type =="Quality Fertilizer":
        return(quality_price_multipliers[3][farming_level],normal_quality_price_multipler)
    else:
        return(normal_quality_price_multipler,normal_quality_price_multipler)#returns multiplier for crops impacted by fertilizer and those that are not impacted (multiharvest crops)
        
