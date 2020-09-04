
#imports
import datetime
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import time
import asyncio

#definitions
client = discord.Client()
prefix = "m!"

announceChannelid = (IDHERE) #define channel to announce in
asmrChannelid = (IDHERE) #define which channel is the "ASMR" channel

def readcmd(message): 
    if str(message.content.startswith(prefix)): #check if message starts with command prefix
        return message.content.lstrip(prefix) #remove the prefix and return the command
    else: #return the command if the message is not a command
        return


@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your sins")) #change status to ((spotify)) listening to your sins
    print(f'We have logged in as {client.user}') #print msg on login

async def DMcountdown(seconds, member : discord.Member):
    timer = seconds
    while timer > 0:
        await member.send(f'YOU HAVE {timer} SECONDS TO GET OUT OF THAT VOICE CHANNEL') #DM user every second with how long they hae left to leave
        timer -= 1  #reduce timer by one
        await asyncio.sleep(1) #wait for 1 second
        if member.voice.channel.id != asmrChannelid: #if user voice channel is not the asmr channel anymore, stop counting
            break 


@client.event
async def on_voice_state_update(member : discord.Member, firstVoiceState, newVoiceState): #when any user updates a voice state
    if newVoiceState.channel != 'None': #if user is in a voice channel
        if newVoiceState.channel.id == asmrChannelid: #and the voice channel's id is the id of the asmr channel
            await client.get_channel(announceChannelid).send(f'<@{member.id}> GET OUT OF THAT ASMR CHANNEL THIS VERY SECOND') #do the funny thing and announce who entered the asmr channel
            await DMcountdown(10, member) #start countdown function
            time.sleep(10) #wait 10 seconds, usually ends up being a lot more
            if member.voice.channel.id == asmrChannelid: #check if user is still in asmr channel
                await member.kick() #kick them from the server if they are

#basic discord bot stuff - return if the bot calls itself for some reason, reply "pong" on the command "ping" and run the bot.    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = readcmd(message)

    if command  == ("ping"):
        await message.channel.send("pong")

client.run('TOKEN')
