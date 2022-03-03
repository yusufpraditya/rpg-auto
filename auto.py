import discord
import os
import ast
import re
import time
import keyboard
import random
import asyncio

keyboard.wait('Ctrl')
client = discord.Client()

bad_chars = ['~', '-', "`", "*", "\n"]
health = 999
hunt = None
adventure = None
farm = None

async def startHunt(heal):
    print("test")
    if int(heal) < 200:
        keyboard.write("rpg heal\n")
    randTime = random.randint(1, 4)
    await asyncio.sleep(randTime)
    keyboard.write("rpg hunt\n")

async def startAdventure(heal):
    if int(heal) < 350:
        keyboard.write("rpg heal\n")
    randTime = random.randint(1, 4)
    await asyncio.sleep(randTime)
    keyboard.write("rpg adventure\n")

async def startFarm():
    randTime = random.randint(1, 4)
    await asyncio.sleep(randTime)
    keyboard.write("rpg farm carrot\n")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))    
    while True:
        if keyboard.is_pressed('Alt'):
            break
        randTime = random.randint(1, 4)
        
        keyboard.write("rpg cd\n")
        await asyncio.sleep(2)
        print("Health:" + str(health))
        print(hunt)
        print(adventure)  
        print(farm)      
        
        if hunt == "1":
            print("hunt coy")
            await startHunt(health)
        if adventure == "2":
            await startAdventure(health)
        if farm == "3":
            await startFarm()
        await asyncio.sleep(28+randTime)

@client.event
async def on_message(message):
    global hunt, farm, adventure
    embeds = message.embeds # return list of embeds    
    print("\n\n\n")
    for embed in embeds:  
        print(embed.to_dict())
        footer = "{'text': 'Check the short version of this command with rpg rd'}"
        if str(embed.to_dict()['footer']).replace('"', "") == footer:
            print("mantab bos\n") 
            print("\n")
            dictionary = embed.to_dict()['fields']

            exp = str(dictionary[1])
            progress = str(dictionary[2])
            
            exp = ''.join((filter(lambda i: i not in bad_chars, exp)))

            progress = ''.join((filter(lambda i: i not in bad_chars, progress)))

            exp_dict = ast.literal_eval(exp)
            progress_dict = ast.literal_eval(progress)

            new_exp = re.sub(":white_check_mark:  ", "", exp_dict['value'])
            new_exp = re.sub(":clock4:  ", "", new_exp)

            new_progress = re.sub(":white_check_mark:  ", "", progress_dict['value'])
            new_progress = re.sub(":clock4:  ", "", new_progress)

            new_exp = new_exp.splitlines()
            new_progress = new_progress.splitlines()

            print(new_exp)
            print(new_progress)
            hunt = new_exp[0]
            adventure = new_exp[1]
            farm = new_progress[1]
            print("\n")
            hunt = re.sub("Hunt", "", hunt)
            adventure = re.sub("Adventure", "", adventure)
            farm = re.sub("Farm", "", farm)
            if hunt == "":
                hunt = "1"
            if adventure == "":
                adventure = "2"
            if farm == "":
                farm = "3"
            print(hunt)
            print(adventure)
            print(farm)

    if message.author == client.user:
        return
    
    if message.author.name == "EPIC RPG":
        if message.content:
            global health
            msg = message.content.splitlines()
            check = "**yusufpraditya1** found and killed a"
            flag = msg[0]
            flag = flag[:37]
            if flag == check:
                health = msg[2]
                health = health[-7:-4]       

    if message.content.startswith('$hello'):        
        await message.channel.send(type(message.author.name))        
        await message.channel.send('Hello!')

print("no1")
client.run('TOKEN')
print("no2")
