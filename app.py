import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

import json
import math
import numpy as np
import matplotlib.pyplot as plt
import classes
import data_import
import multipliers
import harvest





###Main
###These might not be needed at all....
#inputs, make this so there can be up to x amount of crops?
farming_level_input = 0 #int from 0 to 13
current_day = 1 #int from 1 to 28
current_season = 'spring' #string 'spring', 'summer', 'fall, 'winter'
current_year = 1
deluxe_speed_gro_location='Pierres'#can be 'Pierres' or 'Oasis'
fertilizer_input ='None'#cant buy 'Hyper Speed-Gro' or 'Deluxe Fertilizer'
fertilizer_buy_input = True #True or False
farming_skills_input = 'None' #None, Tiller, Agriclut, Artisian
seedinput='475'

#money_input = 100000.0 #float, but will only allow them to enter ints
crop_count_input = 1 #int

###take out of main?
crop_list_keys = list(data_import.crops.keys())
crop_list=[]
for i in range(len(crop_list_keys)):
    crop_list.append({'label':classes.SeedSelection(crop_list_keys[i], 1).crop_name,'value':crop_list_keys[i]})
    






quality_multiplier_value=multipliers.quality_multiplier(farming_level_input,fertilizer_input)

#initial setup for display
#sets up seed
seed = classes.SeedSelection(seedinput,crop_count_input)

#assigns seed to a DataFrame
seed_df=harvest.harvest_calculation(seed,farming_skills_input,classes.Fertilizer(fertilizer_input,True,farming_level_input),current_season,current_day)



### Website stuffs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


fig = px.line(seed_df, x="Display Day", y=["Total Profit", "Total Revenue","Total Expenses Negative"],
              title="Stardew Valley Profit Calculator")

average_profit_fig = px.line(seed_df, x="Display Day", y="Average Profit",title="Average Profits")

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='Profit Graph',figure=fig)],
        ),
        html.Div([
            dcc.Graph(id='Average Profit Graph',figure=average_profit_fig)],
        ),
    ],style={'columnCount': 2}),
    html.Div([
        dcc.Dropdown(
                options=crop_list,
                placeholder='Select a crop',
                value='472',
                id = 'crop-selection-input'
            ),
        dcc.RadioItems(
            options=[
                {'label': 'spring', 'value': 'spring'},
                {'label': 'summer', 'value': 'summer'},
                {'label': 'fall', 'value': 'fall'}
            ],
            value='spring',
            id='season-input'
        ),
        dcc.Input(
            id='current-day-input',
            type='number',
            placeholder='input current day',
            value=current_day,   
        ),
        html.Div(id='crop-selection-output'),
    ],style={'borderBottom': 'thin lightgrey solid'})
],style={'borderBottom': 'thin lightgrey solid'})

'''
#callback function to change which crops appear in the dropdown
@app.callback(Output(component_id='crop-selection-output', component_property='children'),
              Input(component_id='crop-selection-input', component_property='value'),
              Input(component_id='season-input', component_property='value'),
              )

def update_season_dropdown(selected_country):
   return [{'label': i, 'value': i} for i in all_options[selected_country]]
'''




@app.callback(Output(component_id='crop-selection-output', component_property='children'), 
              Output(component_id='current-day-input', component_property='value'),
              Output('Profit Graph', 'figure'),
              Output('Average Profit Graph', 'figure'),
              Input(component_id='crop-selection-input', component_property='value'),
              Input(component_id='season-input', component_property='value'),
              Input(component_id='current-day-input', component_property='value'),
              )

def update_figure(input_value_crop,input_value_season,input_value_current_day):
    print('input_value_crop '+str(input_value_crop)+' input_value_season '+str(input_value_season)+' input_value_current '+str(input_value_current_day))
    seed=classes.SeedSelection(input_value_crop,crop_count_input)
    #error checking inputs
    if type(input_value_current_day) != int:
        input_value_current_day = 1
    elif input_value_current_day == None:
        input_value_current_day = 1
    elif input_value_current_day <1:
        input_value_current_day = 1
    elif input_value_current_day >27:
        input_value_current_day = 27
    seed_df=harvest.harvest_calculation(seed,farming_skills_input,classes.Fertilizer(fertilizer_input,True,farming_level_input),input_value_season,input_value_current_day)
    
    fig = px.line(seed_df, x="Display Day", y=["Total Profit", "Total Revenue","Total Expenses Negative"],
                  title="Stardew Valley Profit Calculator")
    
    average_profit_fig = px.line(seed_df, x="Display Day", y="Average Profit",title="Average Profits")
    fig.update_layout(transition_duration=500)
    return 'Output: {}'.format(input_value_crop),input_value_current_day,fig,average_profit_fig


if __name__ == '__main__':
    app.run_server(debug=True)








