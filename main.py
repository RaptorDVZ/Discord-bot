import discord
import os
import random
from alive import alive
from discord.ext import commands

client= commands.Bot(command_prefix = '>')

bad_words=['fuck','bhosadike','madarchod','gandu','chutiye','jhaatu','jhatu','chut','loda','lauda','lawda','motherfucker','asshole','shithole','cunt','lode','lawde','lund','behenchod','banchod','benchod','benchoda','chod','chuda','ass','dick','chud']

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
  
  

  if any(word in msg.lower() for word in bad_words):
    await message.channel.purge(limit=1)
    embedVar = discord.Embed(title="WARNING:You cannot send this message here!", description=mention, color=0x00ff00)
    #embedVar.add_field(name="Field1", value="hi", inline=False)
    #embedVar.add_field(name="Field2", value="hi2", inline=False)
    await message.channel.send(embed=embedVar)
  await client.process_commands(message)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=5):
  await ctx.channel.purge(limit=amount)

@client.command()
async def hi(ctx):
  embedVar = discord.Embed(title="HELLO THERE", description=ctx.author.mention, color=0x00ff00)
  #embedVar.add_field(name="Field1", value="hi", inline=False)
  #embedVar.add_field(name="Field2", value="hi2", inline=False)
  await ctx.channel.send(embed=embedVar)

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx,member,message):
  embed = discord.Embed(title="You have been WARNED!!", description=member, color=0x00ff00)
  
  embed.add_field(name="Reason:", value=message, inline = False)
  #embedVar.add_field(name="Reason", value="hi2", inline=False)
  await ctx.channel.purge(limit=1)
  await ctx.channel.send(embed=embed)



alive()
client.run(os.getenv('TOKEN'))
