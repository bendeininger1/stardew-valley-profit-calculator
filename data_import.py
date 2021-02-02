import pandas as pd

import json
#Load crop data
with open('Crops.json') as f:
    crops = json.load(f)
#Load Object data including prices
with open('ObjectInformation.json') as f:
    ObjectInformation = json.load(f)

      
#parse this data
'''"493": "1 2 1 1 2/fall/21/282/5/0/true 2 2 0 .1/false/false"
crops 'Key' (Crop name): Days in each growing stage / Seasons spring, summer, fall, winter/sprite/
Index of crop/regrow after harvest (-1 no regrowth, 3 = 3days),
Harvest Method,Chance for extra harvest false or true
'''
def parsed_crops():
    for i in crops:
        #split dict values into a list using the '/' serparator
        #print(str(i)+str(crops[i]))
        crops[i] = crops[i].split('/')
        #split the 'days in each cycle' into a list, covnerts to int, then sum that list returing  total days to grow
        crops[i][0] = sum([int (x) for x in crops[i][0].split(' ')])
        #split the 'Regrow after Harvest'
        #print(crops[i][6])
        crops[i][6] = crops[i][6].split(' ')
        #print(crops[i][6])
        #convert true/false to boolean of 'Regrow after Harvest'
        crops[i][6][0] = crops[i][6][0] == 'true'
        if (crops[i][6][0]== True):
            for x in [1,2,3]:
                crops[i][6][x] = int(crops[i][6][x])
            crops[i][6][4] = float(crops[i][6][4])
        # the 'season' into a list
        #print(crops[i][1])
        crops[i][1] = crops[i][1].split(' ')
        #print(crops[i][1])
        '''
    ### maybe turn this into a data frame?
    print('look here')
    print(crops)
    data={'Seed Index':,
          }
    crops_df=pd.DataFrame(data)
    '''
    return(crops)
crops=parsed_crops()
#print(parsed_crops())


'''parse the object information
"493": "Cranberry Seeds/120/-300/Seeds -74/Cranberry Seeds/Plant these in the fall.
        Takes 7 days to mature, and continues to produce after first harvest."
'''
def parsed_object_information():
    for i in ObjectInformation:
    #split dict values into a list using the '/' serparator
        ObjectInformation[i] = ObjectInformation[i].split('/')
        ObjectInformation[i]
    return(ObjectInformation)
ObjectInformation=parsed_object_information()
