from asyncio.windows_events import NULL
import discord
import json,urllib.request
from discord.ext import tasks

#Bot Token
TOKEN = ''

def createArray(category):   
    for i in range(0, len(category)):
        itemJson1 = productJson(category, i)
        if(category == jackets):
            oldJacketsJson[i] = itemJson1
        if(category == shirts):
            oldShirtsJson[i] = itemJson1
        if(category == topsSweaters):
            oldTopsSweatersJson[i] = itemJson1
        if(category == sweatshirts):
            oldSweatshirts[i] = itemJson1
        if(category == pants):
            oldPantsJson[i] = itemJson1
        if(category == hats):
            oldHatsJson[i] = itemJson1
        if(category == bags):
            oldBagsJson[i] = itemJson1
        if(category == accessories):
            oldAccessoriesJson[i] = itemJson1
        if(category == skate):
            oldSkateJson[i] = itemJson1


    if(category == jackets):    
        return oldJacketsJson
    if(category == shirts):
        return oldShirtsJson
    if(category == topsSweaters):
        return oldTopsSweatersJson
    if(category == sweatshirts):
        return oldSweatshirts
    if(category == pants):
        return oldPantsJson
    if(category == hats):
        return oldHatsJson
    if(category == bags):
        return oldBagsJson
    if(category == accessories):
        return oldAccessoriesJson
    if(category == skate):
        return oldSkateJson

def productJson(category, i):
    itemSite = urllib.request.urlopen("https://www.supremenewyork.com/shop/" + str(category[i]['id']) + ".json").read()
    itemJson = json.loads(itemSite)
    return itemJson

client = discord.Client()

data = urllib.request.urlopen("https://www.supremenewyork.com/mobile_stock.json").read()
output = json.loads(data)

try:
  new = output['products_and_categories']['new']
  nc = 1
except:
  print("No New Category")
  nc = 0

rs = 0
jackets = output['products_and_categories']['Jackets']
shirts = output['products_and_categories']['Shirts']
topsSweaters = output['products_and_categories']['Tops/Sweaters']
sweatshirts = output['products_and_categories']['Sweatshirts']
pants = output['products_and_categories']['Pants']
hats = output['products_and_categories']['Hats']
bags = output['products_and_categories']['Bags']
accessories = output['products_and_categories']['Accessories']

try:
  shoes = output['products_and_categories']['Shoes']
  sc = 1
except:
  print("No Shoe Category")
  sc = 0

skate = output['products_and_categories']['Skate']
string = ""

accessories = output['products_and_categories']['Accessories']

if sc == 1:
    oldShoesJson = [0 for i in range(len(shoes))]
oldSkateJson = [0 for i in range(len(skate))]

oldJacketsJson = [0 for i in range(len(jackets))]
oldShirtsJson = [0 for i in range(len(shirts))]
oldTopsSweatersJson = [0 for i in range(len(topsSweaters))]
oldSweatshirts = [0 for i in range(len(sweatshirts))]
oldPantsJson = [0 for i in range(len(pants))]
oldHatsJson = [0 for i in range(len(hats))]
oldBagsJson = [0 for i in range(len(bags))]
oldAccessoriesJson = [0 for i in range(len(accessories))]
oldJacketsJson = createArray(jackets)
oldShirtsJson = createArray(shirts)
oldTopsSweatersJson = createArray(topsSweaters)
oldSweatshirts = createArray(sweatshirts)
oldPantsJson = createArray(pants)  
oldHatsJson = createArray(hats)
oldBagsJson = createArray(bags)
oldAccessoriesJson = createArray(accessories)
if sc == 1:
    oldShoesJson = createArray(shoes)
oldSkateJson = createArray(skate)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    
    async def search(category, string):
                for i in range(0, len(category)):
                    
                    string = string + "\n"
                    string = "              " + "                **" + category[i]['name'] + "**\n" 
                    string = string + "\n"
                    itemSite = urllib.request.urlopen("https://www.supremenewyork.com/shop/" + str(category[i]['id']) + ".json").read()
                    itemJson = json.loads(itemSite)

                    #goes through each colour
                    for j in range(0, len(itemJson['styles'])):
                        temp = itemJson['styles'][j]['sizes']
                        
                        #No sizes
                        if temp[0]['name'] == 'N/A':
                            if temp[0]['stock_level'] == 0:
                                #prints colour and stock
                                string = string + itemJson['styles'][j]['name'] + "                OUT OF STOCK\n"
                            else:
                                string = string + itemJson['styles'][j]['name'] + "                IN STOCK\n"
                        
                        #Sizes
                        else:
                            string = string + "\n"
                            for k in range(0, len(temp)):
                                if temp[k]['stock_level'] == 0:
                                    #prints colour, size and stock
                                    string = string + itemJson['styles'][j]['name'] + " " + temp[k]['name'] + "                OUT OF STOCK\n"
                            
                                else:
                                    string = string + itemJson['styles'][j]['name'] + " " + temp[k]['name'] + "                IN STOCK\n"
                    string = string + "\n"
                    await message.channel.send(string)
                return string

    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'current-stock':
        if user_message.lower() == 'jackets':
            await search(jackets, string)            
            return

        elif user_message.lower() == 'shirts':
            await search(shirts, string)            
            return

        elif user_message.lower() == 'tops' or user_message.lower() == 'sweaters' or user_message.lower() == 'tops/sweaters':
            await search(topsSweaters, string)            
            return

        elif user_message.lower() == 'sweatshirts':
            await search(sweatshirts, string)            
            return

        elif user_message.lower() == 'pants':
            await search(pants, string)            
            return

        elif user_message.lower() == 'hats':
            await search(hats, string)            
            return
        
        elif user_message.lower() == 'bags':
            await search(bags, string)            
            return
        
        elif user_message.lower() == 'accessories':
            await search(accessories, string)            
            return
        
        elif user_message.lower() == 'shoes' and sc != 0:
            await search(shoes, string)            
            return

        elif user_message.lower() == 'skate':
            await search(skate, string)            
            return
        
        elif user_message.lower() == 'new' and nc != 0:
            await search(new, string)            
            return

        else:
            await message.channel.send("INVALID CATEGORY")
            return

client.run(TOKEN)