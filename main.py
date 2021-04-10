import discord
import os
import random
from alive import alive
from discord.ext import commands

client= commands.Bot(command_prefix = '>')

bad_words=['fuck','bhosadike','madarchod','gandu','chutiye','jhaatu','jhatu','chut','loda','lauda','lawda','motherfucker','asshole','shithole','pussy','cunt','lode','lawde','lund','behenchod','banchod','benchod','benchoda']

response='WARNING :You cannot use this word here '

@client.event
async def on_ready():
  print('Raptor Dada is ready to be used')

  

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  mention = message.author.mention

  msg = message.content
  
  
  if msg.startswith('>hi'):
    embedVar = discord.Embed(title="HELLO THERE", description=mention, color=0x00ff00)
    #embedVar.add_field(name="Field1", value="hi", inline=False)
    #embedVar.add_field(name="Field2", value="hi2", inline=False)
    await message.channel.send(embed=embedVar)

  if any(word in msg.lower() for word in bad_words):
    await message.channel.purge(limit=1)
    embedVar = discord.Embed(title="WARNING:You cannot send this message here!", description=mention, color=0x00ff00)
    #embedVar.add_field(name="Field1", value="hi", inline=False)
    #embedVar.add_field(name="Field2", value="hi2", inline=False)
    await message.channel.send(embed=embedVar)
  await client.process_commands(message)

@client.command()
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit=amount)


alive()
client.run(os.getenv('TOKEN'))
