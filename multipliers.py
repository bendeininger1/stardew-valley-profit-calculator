
def average_harvest_yield(crop_id):
    if int(crop_id) == 475:
        harvest_multiplier = 1.2
    if int(crop_id) == 273:
        harvest_multiplier = 1.1
    if int(crop_id) == 745:
        harvest_multiplier = 1.02
    if int(crop_id) == 480:
        harvest_multiplier = 1.05
    if int(crop_id) == 481:
        harvest_multiplier = 3.06
    if int(crop_id) == 482:
        harvest_multiplier = 1.03
    if int(crop_id) == 433:
        harvest_multiplier = 4.08
    if int(crop_id) == 488:
        harvest_multiplier = 1.002
    if int(crop_id) == 493:
        harvest_multiplier = 2.04
    else:
        harvest_multiplier = 1.0
    return harvest_multiplier

def quality_multiplier(farming_level):
    if farming_level == 0:
        return (1.01,1.04,1.07,1.10)
    if farming_level == 1:
        return (1.03,1.08,1.12,1.16)
    if farming_level == 2:
        return (1.05,1.11,1.17,1.22)
    if farming_level == 3:
        return (1.07,1.14,1.21,1.27)
    if farming_level == 4:
        return (1.09,1.17,1.25,1.31)
    if farming_level == 5:
        return (1.10,1.20,1.28,1.33)
    if farming_level == 6:
        return (1.12,1.23,1.31,1.35)
    if farming_level == 7:
        return (1.14,1.25,1.33,1.38)
    if farming_level == 8:
        return (1.16,1.28,1.34,1.40)
    if farming_level == 9:
        return (1.17,1.30,1.36,1.42)
    if farming_level == 10:
        return (1.19,1.32,1.38,1.44)
    if farming_level == 11:
        return (1.20,1.33,1.39,1.46)
    if farming_level == 12:
        return (1.22,1.34,1.41,1.48)
    if farming_level == 13:
        return (1.23,1.35,1.43,1.5)
    else:
        print('farming level needs to be between 0 and 13')
        return (1.01,1.04,1.07,1.10)

'''
###Fertilizer Not implemented
#Given a type of fertilizer, returns growth rate multiplier
def fertilizer_check_speed(fertilizer):
    if fertilizer = 'Speed-Gro'
        return 1.1 #Growth
    if fertilizer = 'Deluxe Speed-Gro'
        return 1.25 #Growth
    if fertilizer = 'Deluxe Speed-Gro'
        return 1.33 #Growth
    print('')
'''