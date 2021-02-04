#checks input values to make sure they are valid

#check the day value to make sure it is a positive integer less  as a season is 28 days
def current_day_checker(input_value):
    if type(input_value) != int:
        output_value = 1
    elif input_value == None:
        output_value = 1
    elif input_value <1:
        output_value = 1
    elif input_value >27:
        output_value = 27
    else:
        output_value = input_value
    return output_value

#checks to make sure tyhe crop count is a positive integer less than a really large number
def crop_count_checker(input_value):
    if type(input_value) != int:
        output_value = 1
    elif input_value == None:
        output_value = 1
    elif input_value <1:
        output_value = 1
    elif input_value >1000000000:
        output_value = 1000000000
    else:
        output_value = input_value
    return output_value

def fertilizer_checker(input_value):
    if input_value == 'Buy':
        output_value = True
    else:
        output_value = False
    return output_value

def farming_level_checker(input_value):
    if type(input_value) != int:
        output_value = 0
    elif input_value == None:
        output_value = 0
    elif input_value <0:
        output_value = 0
    elif input_value >13:
        output_value = 13
    else:
        output_value = input_value
    return output_value