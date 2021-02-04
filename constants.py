#regular crops are the default sell price (from ObjectInfomration),silver are x1.25,  gold are  x1.5, iridium are 2x
#values use the sum of (the %freqency for each quality type (normal, gold, silver, idium) mutipled by the sell prices above) for each farming level and for each fertilizer type
#each index is the farming level


quality_price_multipliers=((1.01,1.03,1.05,1.07,1.09,1.10,1.12,1.14,1.16,1.17,1.19,1.20,1.22,1.23),#Normal Soil
                           (1.04,1.08,1.11,1.14,1.17,1.20,1.23,1.25,1.28,1.30,1.32,1.33,1.34,1.35),#Soil with Basic Fertilizer
                           (1.07,1.12,1.17,1.21,1.25,1.28,1.31,1.33,1.34,1.36,1.38,1.39,1.41,1.43),#Soil with Quality Fertilizer
                           (1.10,1.16,1.22,1.27,1.31,1.33,1.35,1.38,1.40,1.42,1.44,1.46,1.48,1.50))

#data for fertilizer-selection-input
fertilizer_type=[{'label':'None','value':'None'},
                 {'label':'Basic Fertilizer','value':'Basic Fertilizer'},
                 {'label':'Quality Fertilizer','value':'Quality Fertilizer'},
                 {'label':'Speed-Gro','value':'Speed-Gro'},
                 {'label':'Deluxe Speed-Gro','value':'Deluxe Speed-Gro'},
                 {'label':'Deluxe Fertilizer','value':'Deluxe Fertilizer'},
                 {'label':'Hyper Speed-Gro','value':'Hyper Speed-Gro'},]

farming_skills=[{'label':'None','value':'None'},
                {'label':'Tiller','value':'Tiller'},
                {'label':'Artisan','value':'Artisan'},
                {'label':'Agriculturist','value':'Agriculturist'},]






