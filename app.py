import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


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
tiller_input = False #True or False
artisan_input = False #True or False
agriculturist_input = False #True or False
current_day = 1 #int from 1 to 28
current_season = 'spring' #string 'spring', 'summer', 'fall, 'winter'
#money_input = 100000.0 #float, but will only allow them to enter ints
plant_count_input = 1 #int

###take out of main?
crop_list_keys = list(data_import.crops.keys())
crop_list=[]
for i in range(len(crop_list_keys)):
    crop_list.append({'label':classes.SeedSelection(crop_list_keys[i], 1).crop_name,'value':crop_list_keys[i]})



seed1input=['473',plant_count_input]
seed2input=['475',plant_count_input]

#crop1=classes.SeedSelection()

quality_multiplier_value=multipliers.quality_multiplier(farming_level_input)

#sets up seed1
seed1 = classes.SeedSelection(seed1input[0],seed1input[1])
#assigns seed1 to a DataFrame
seed1_df=harvest.harvest_calculation(seed1.crop_count,
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

### Website stuffs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


fig = px.line(seed1_df, x="Day", y=["Total Profit", "Total Revenue","Total Expenses Negative", "Average Profit"],
              title="Stardew Valley Profit Calculator")



app.layout = html.Div([
    dcc.Graph(
        id='Profit Graph',
        figure=fig
    ),
    dcc.Dropdown(
        options=crop_list,
        placeholder="Select a crop",
        value='472',
        id = 'crop-selection-input'
    ),
    html.Div(id='crop-selection-output'),
    

])

@app.callback(
    Output(component_id='crop-selection-output', component_property='children'), 
    Output('Profit Graph', 'figure'),
    Input(component_id='crop-selection-input', component_property='value'),
    #Input('year-slider', 'value')
)

def update_figure(input_value):
    ###replace 1 with crop count
    seed=classes.SeedSelection(input_value,1)
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
    fig = px.line(seed_df, x="Day", y=["Total Profit", "Total Revenue","Total Expenses Negative", "Average Profit"],
                  title="Stardew Valley Profit Calculator")
    
    fig.update_layout(transition_duration=500)
    return 'Output: {}'.format(input_value),fig
'''
def update_output_div(input_value):
    
    return 'Output: {}'.format(input_value)
'''

if __name__ == '__main__':
    app.run_server(debug=True)








