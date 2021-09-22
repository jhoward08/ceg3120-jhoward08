#! /usr/bin/python3
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
#from PIL import Image

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    halo_quotes = [
        'Hmm… I’m detecting a high degree of cerebral cortex activity. You’re not the muscle-bound automatons the press makes you out to be.” -Cortana',
        'It means always… It means always… It means always strip you always strip our enemy of weapons before you interrogate him.” -Unknown Spartan',
        'Relax! I’d Rather Not Piss This Thing Off!” -Master Chief',
        ('Enjoy it while you can, Marines. Soon as we land, we’re right back to it. Priority one: Secure a Landing Zone for the Commander’s Frigate. Keep your eyes and ears open. We need all the Intel we can get… on wherever the hell we are.” -Avery Johnson(SgtMaj USMC)'),
        'Thought I’d Try Shooting My Way Out—Mix Things Up A Little.” -Master Chief'
    ]

    ready_player_one_quotes = [
        'Being human totally sucks most of the time. Videogames are the only thing that make life bearable.',
        'You would be amazed how much research you can get done when you have no life whatsoever.',
        'No one in the world gets what they want and that is beautiful.',
        'That was when I realized, as terrifying and painful as reality can be, it is also the only place where you can find true happiness. Because reality is real.'
    ]
    
    if message.content == 'Marines!':
        response = random.choice(halo_quotes)
        await message.channel.send(response)
    elif message.content == 'Ready?':
        response = random.choice(ready_player_one_quotes)
        await message.channel.send(response)
client.run(TOKEN)
