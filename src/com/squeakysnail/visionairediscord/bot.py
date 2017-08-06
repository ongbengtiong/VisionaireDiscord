'''
Created on 5 Aug 2017

@author: bengt
'''
import pandas
import discord
import asyncio
from bs4 import BeautifulSoup
import requests
import re
import datetime

if __name__ == '__main__':
    print('Visionaire Discord Bot')

url = "http://www.mysg-property.com/the-visionaire-ec.html"
lastCheckedTime = datetime.datetime.now()
unitCount = ""
checkInterval = 8
client = discord.Client()
topDate = datetime.datetime(2018, 10, 31, 0,0,0)

      
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global lastCheckedTime
    global unitCount   
    currentTime = datetime.datetime.now()
    timeDelta = currentTime - lastCheckedTime  
    hours, remainder = divmod(timeDelta.seconds, 3600)
    if message.content == '!help':
        await client.send_message(message.channel, "!units: units left.\n!top: time to TOP")
    if message.content == '!v' or message.content == '!units':
        isCached = "!"
        if hours>checkInterval or unitCount=="":
            lastCheckedTime = datetime.datetime.now()
            await client.send_message(message.channel, 'Checking Visionaire units...')
            r  = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data)
            for link in soup.find_all(text=re.compile("Last(.*)units")):
                unitCount = link 
                isCached = ""
        await client.send_message(message.channel, unitCount + isCached)
    if message.content == '!cache':
        #timeToNextCheck = lastCheckedTime -timeDelta + checkInterval
        await client.send_message(message.channel, "Last checked: "+ str(lastCheckedTime) +"]" + " ["+ str(checkInterval-hours) +" hours before next check.]")
    if message.content == '!top':
        timeToTop = topDate - currentTime
        await client.send_message(message.channel, "Time to TOP: "+ str(timeToTop.days) +" days!\nEstimated TOP: " + str(topDate))
         
            


#client.run('MzQzMjQ0MDA0MDU5NjQzOTA2.DGgAOA.p41VGt3_wqKfkkD-acv432i2nIE')
client.run('MzQzMjk4NDY0NDI5Mzc1NDk5.DGcJJw.Bv_hjLODcpnJ8WtczjrPcApjxMs')
