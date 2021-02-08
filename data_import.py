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
def parsed_crops_function():
    crops.pop('802')#remove Cactus Seeds
    crops.pop('890')#remove QI Seeds
    crops.pop('885')#remove Fiber Seeds
    crops.pop('495')#remove Spring Seeds
    crops.pop('496')#remove Summer Seeds
    crops.pop('497')#remove Fall Seeds
    crops.pop('498')#remove Winter Seeds
    crops.pop('431')#remove Sunflower Seeds
    crops.pop('273')#remove Rice shoots
    crops.pop('833')#remove Pineapple Seeds
    crops.pop('347')#remove Rare seed
    crops.pop('831')#remove Taro Tuber
    
    for i in crops:
        #split dict values into a list using the '/' serparator
        crops[i] = str(crops[i]).split('/')#split the 'days in each cycle' into a list, covnerts to int, then sum that list returing  total days to grow
        crops[i][0] = sum([int (x) for x in crops[i][0].split(' ')])
        #split the 'Regrow after Harvest'
        crops[i][6] = crops[i][6].split(' ')
        #convert true/false to boolean of 'Regrow after Harvest'
        crops[i][6][0] = crops[i][6][0] == 'true'
        if (crops[i][6][0]== True):
            for x in [1,2,3]:
                crops[i][6][x] = int(crops[i][6][x])
            crops[i][6][4] = float(crops[i][6][4])
        # the 'season' into a list
        crops[i][1] = crops[i][1].split(' ')
        
        
    return(crops)

parsed_crops=parsed_crops_function()


'''parse the object information
"493": "Cranberry Seeds/120/-300/Seeds -74/Cranberry Seeds/Plant these in the fall.
        Takes 7 days to mature, and continues to produce after first harvest."
'''
def parsed_object_information_function():
    for i in ObjectInformation:
    #split dict values into a list using the '/' serparator
        ObjectInformation[i] = str(ObjectInformation[i]).split('/')
    return(ObjectInformation)
parsed_object_information=parsed_object_information_function()

if __name__ == '__main__':
    import pandas as pd
    x=parsed_crops
    #print(x)
    y=parsed_object_information
    #print(y)
    #print(ObjectInformation)
    #print()
    for i in parsed_crops:
        print(str(i)+str(parsed_object_information[i][0]))
        
    print(x.get('472'))
    print(y['472'][0])
    #print(parsed_object_information()[parsed_crops['472'][3]][0])
    
    #x=crops
    #print(x)
    #parsed_crops()
    