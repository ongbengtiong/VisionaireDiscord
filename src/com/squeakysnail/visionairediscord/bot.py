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


if __name__ == '__main__':
    print('Hello World')


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!v'):
       await client.send_message(message.channel, 'Checking Visionaire...')
       url = "http://www.mysg-property.com/the-visionaire-ec.html"
       r  = requests.get(url)
       data = r.text
       soup = BeautifulSoup(data)
       for link in soup.find_all(text=re.compile("Last(.*)units")):
           await client.send_message(message.channel, 'Visionaire: ' + link + "!")
           #print(link.get('href'))


client.run('MzQzMjQ0MDA0MDU5NjQzOTA2.DGbWeg._h3KQlAY3LK6xFtjJ8jqIyeUZmo')
