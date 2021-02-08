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
import constants
import input_checkers





###Main


###Need to remove these

current_year = 1
deluxe_speed_gro_location='Pierres'#can be 'Pierres' or 'Oasis'




###take out of main?
###move to crops list
#creates an object for each crop type
crop_list_keys = list(data_import.crops.keys())
crop_list=[]
crop_seed_list=[]
for i in range(len(crop_list_keys)):
    crop_list.append({'label':classes.SeedSelection(crop_list_keys[i]).crop_name,'value':crop_list_keys[i]})
    crop_seed_list.append(classes.SeedSelection(crop_list_keys[i]))
    #print(crop_seed_list[i].growing_seasons)

'''
for i in range(len(crop_list_keys)):
    print (crop_seed_list[i].growing_seasons)
'''
'''
for i in range(len(crop_seed_list[i].growing_seasons)):
    print (crop_seed_list[i].growing_seasons)
'''
#quality_multiplier_value=multipliers.quality_multiplier(farming_level_input,fertilizer_input)




### Website stuffs


'''
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
'''
app = dash.Dash(__name__)

server = app.server

#inital setup of charts, placeholders
df = pd.DataFrame({(0,1),(0,1)})
fig = px.line(df, x=1, y=1,)
average_profit_fig = fig

app.layout =html.Div([
    html.Div([
        html.Div([html.H1('Stardew Valley Profit Calculator')], id='title'),
        html.Div([
            html.Div([
                dcc.Graph(id='Profit Graph',figure=fig)],className='graphs',
            ),
            html.Div([
                dcc.Graph(id='Average Profit Graph',figure=average_profit_fig)],className='graphs',
            ),
        ],style={'columnCount': 2},id = 'graphbody'),
        html.Div([
            html.Table([
                html.Th([
                    html.Table([
                        html.Tr([
                            html.Td('Crop Selection'),
                            html.Th([
                            dcc.Dropdown(options=crop_list,value='472',
                                         id = 'crop-selection-input',
                                         multi=True)])
                            ]),
                        html.Tr([
                            html.Td('Starting Season Selection'),
                            html.Th([
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'spring', 'value': 'spring'},
                                        {'label': 'summer', 'value': 'summer'},
                                        {'label': 'fall', 'value': 'fall'}
                                        ],
                                    value='spring',id='season-input')
                            ])
                            ]),
                        html.Tr([
                            html.Td('Starting Day Selection'),
                            html.Th([dcc.Input(id='current-day-input',type='number',value='1')])
                            ])
                        ],)
                    ],),
                html.Th([
                    html.Table([
                        html.Tr([
                            html.Td('Crop Count'),
                            html.Th([
                            dcc.Input(id='crop-count-input',type='number',value='1',),
                                ],)
                            ]),
                        html.Tr([
                            html.Td('Fertilizer Selection'),
                            html.Th([
                            dcc.Dropdown(options=constants.fertilizer_type,value='None',id = 'fertilizer-selection-input')
                                ])
                            ]),
                        html.Tr([
                            html.Td('Buy Fertilizer?'),
                            html.Th([
                            dcc.RadioItems(
                                options=[{'label':'Buy','value':'Buy'},
                                         {'label':'Don\'t Buy','value':'Don\'t Buy'},
                                    ],
                                value='Buy',id='fertilizer-buy-input',),
                                ],)
                            ]),
                        ],)
                    ],),
                html.Th([
                    html.Table([
                        html.Tr([
                            html.Td('Farming Level'),
                            html.Th([
                            dcc.Input(id='farming-level-input',type='number',value='0',),
                                ],)
                            ]),
                        html.Tr([
                            html.Td('Farming Skills'),
                            html.Th([
                            dcc.Dropdown(options=constants.farming_skills,value='None',id = 'farming-skills-input')
                                ],)
                            ]),
                        ],)
                    ],),
                ],)
            
            ],id='options'),
        
        
        html.Div([html.A('Stardew Valley Copyright © 2016-2020 ConcernedApe LLC',
                         href='https://www.stardewvalley.net/'),
            ' |  Source code on my ',
            html.A('GitHub',href='https://github.com/bendeininger1/stardew-valley-profit-calculator'),
            html.Div([
                html.A(rel='license',href='http://creativecommons.org/licenses/by-nc-sa/3.0/'),
                html.Img(alt='Creative Commons License',
                         style={'border-width':'0'},
                         src='https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png',),
                html.Br(),
                'This work is licensed under a ',
                html.A('Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License',
                       rel='license',href='http://creativecommons.org/licenses/by-nc-sa/3.0/'),
                    ])
            ],id='footer')
        ])
    ],id='mainbody'
)



#callback function to change which crops appear in the dropdown0
@app.callback(Output(component_id='crop-selection-input', component_property='options'),
              Output(component_id='crop-selection-input', component_property='value'),
              Input(component_id='season-input', component_property='value'),
              )

def update_season_dropdown(season_input):
    crop_selection_list=[]
    j=0
    for i in range(len(crop_list_keys)):
        if season_input in crop_seed_list[i].growing_seasons:
            crop_selection_list.append({'label':str(crop_seed_list[i].crop_name),
                                        'value':str(crop_seed_list[i].seed_number)})
            if j == 0:#just so it picks the first crop as the default, for improved performance
                default_crop_value = str(crop_seed_list[i].seed_number)
                #print('default_crop_value '+str(default_crop_value))
                j=1
            
            #print('Test crop_selection_list '+str(crop_selection_list))
    return crop_selection_list,default_crop_value


@app.callback(Output(component_id='current-day-input', component_property='value'),
              Output(component_id='crop-count-input', component_property='value'),
              Output(component_id='farming-level-input', component_property='value'),
              Output('Profit Graph', 'figure'),
              Output('Average Profit Graph', 'figure'),
              Input(component_id='crop-selection-input', component_property='value'),
              Input(component_id='season-input', component_property='value'),
              Input(component_id='current-day-input', component_property='value'),
              Input(component_id='crop-count-input', component_property='value'),
              Input(component_id='fertilizer-selection-input', component_property='value'),
              Input(component_id='fertilizer-buy-input', component_property='value'),
              Input(component_id='farming-level-input', component_property='value'),
              Input(component_id='farming-skills-input', component_property='value'),
              )

def update_figure(input_value_crop,
                  input_value_season,
                  input_value_current_day,
                  input_value_crop_count,
                  input_value_fertilizer,
                  input_value_buy_fertilizer,
                  input_value_farming_level,
                  input_value_farming_skills):
    
    #error checking inputs
    input_value_current_day=input_checkers.current_day_checker(input_value_current_day)
    input_value_crop_count=input_checkers.crop_count_checker(input_value_crop_count)
    input_value_buy_fertilizer=input_checkers.fertilizer_checker(input_value_buy_fertilizer)
    input_value_farming_level=input_checkers.farming_level_checker(input_value_farming_level)
    input_value_crop=input_checkers.input_value_crop(input_value_crop,input_value_season)

    seed=[]
    seed_combined_df=pd.DataFrame()
    if type(input_value_crop) == str:#handle when only 1 crop is selected
        input_value_crop=[input_value_crop]
    
    print('input_value_crop '+str(input_value_crop))
    print(type(input_value_crop))
    print(len(input_value_crop))
    print(range(len(input_value_crop)))
    
    
    for i in range(len(input_value_crop)):
        '''
        print('i '+str(i))
        print('input_value_crop '+str(input_value_crop[i]))
        '''
        seed=classes.SeedSelection(input_value_crop[i])#get info associated with the crop/seed selected
        print(str(seed.crop_name)+str(i))
        if i == 0:
            seed_combined_df=harvest.harvest_calculation(seed,
                                                         input_value_crop_count,
                                                         input_value_farming_skills,
                                                         classes.Fertilizer(input_value_fertilizer,
                                                                            input_value_buy_fertilizer,
                                                                            input_value_farming_level),
                                                         input_value_season,
                                                         input_value_current_day)
            #melted=pd.melt(seed_combined_df,id_vars=['Display Day'],value_vars=['Total Profit','Total Revenue','Total Expenses Negative'])
            #print(melted)
            #print(seed_combined_df)
            #df_test = px.data.tips()
            #print(df_test)
            
        if i >0:
            seed_df=harvest.harvest_calculation(seed,
                                                input_value_crop_count,
                                                input_value_farming_skills,
                                                classes.Fertilizer(input_value_fertilizer,
                                                                   input_value_buy_fertilizer,
                                                                   input_value_farming_level),
                                                input_value_season,
                                                input_value_current_day)
            df=[seed_combined_df,seed_df]
            seed_combined_df = pd.concat(df)
            #print(seed_combined_df)

    '''
    fig = px.line(seed_combined_df, x="Display Day", y=["Total Profit", "Total Revenue","Total Expenses Negative"],
                  title="Stardew Valley Profit Calculator",
                  color='Seed Name',
                  labels={'Seed Name'})
    

    #average_profit_fig = px.line(seed_combined_df, x="Display Day", y="Average Profit",title="Average Profits",color='Seed Name')
    average_profit_fig = px.line(melted, x="Display Day", y="variable",title="Test")
    '''
    excluding_profits_df=seed_combined_df[seed_combined_df['Finance Category']!='Average Profits']
    fig = px.line(excluding_profits_df, x='Day', y='Values',
                  title="Stardew Valley Profit Calculator",
                  color='Finance Category',
                  line_group='Crop',
                  )###add labels for seed_name
    #profits_df=seed_combined_df.query('`Finance Category` == `Average Profits`')
    profits_df=seed_combined_df[seed_combined_df['Finance Category']=='Average Profits']
    #print(profits_df.values)
    #print(excluding_profits_df.values)
    
    average_profit_fig=px.line(profits_df, x='Day', y='Values',title='Average Profits',
                  color='Finance Category',line_group='Crop')###add labels for seed_name

    #labels={'Seed Name'}
    #average_profit_fig =fig
    #average_profit_fig = px.line(seed_combined_df, x="Display Day", y="Average Profit",title="Average Profits",color='Seed Name')
    
    fig.update_layout(transition_duration=500)
    fig.update_yaxes(type='linear')
    average_profit_fig.update_yaxes(type='linear')
    return input_value_current_day,input_value_crop_count,input_value_farming_level,fig,average_profit_fig


if __name__ == '__main__':
    import unittest
    app.run_server(debug=True)








