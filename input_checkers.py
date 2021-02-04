#checks input values to make sure they are valid
def current_day_checker(input_value_current_day):
    if type(input_value_current_day) != int:
        output = 1
    elif input_value_current_day == None:
        output = 1
    elif input_value_current_day <1:
        output = 1
    elif input_value_current_day >27:
        output = 27
    else:
        output = input_value_current_day
    return output