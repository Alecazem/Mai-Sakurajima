import datetime
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import json
import time
import asyncio

client = discord.Client()
prefix = "m!"

announceChannelid = (IDHERE)
asmrChannelid = (IDHERE)

def readcmd(message):
    if str(message.content.startswith(prefix)):
        return message.content.lstrip(prefix)
    else:
        return


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your sins"))
    print(f'We have logged in as {client.user}')

async def DMcountdown(seconds, member : discord.Member):
    timer = seconds
    while timer > 0:
        await member.send(f'YOU HAVE {timer} SECONDS TO GET OUT OF THAT VOICE CHANNEL')
        timer -= 1
        await asyncio.sleep(1)
        if member.voice.channel.id != asmrChannelid:
            break


@client.event
async def on_voice_state_update(member : discord.Member, firstVoiceState, newVoiceState):
    if newVoiceState.channel != 'None':
        if newVoiceState.channel.id == asmrChannelid:
            await client.get_channel(announceChannelid).send(f'<@{member.id}> GET OUT OF THAT ASMR CHANNEL THIS VERY SECOND')
            await DMcountdown(10, member)
            time.sleep(10)
            if member.voice.channel.id == asmrChannelid:
                await member.kick()

    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = readcmd(message)

    if command  == ("ping"):
        await message.channel.send("pong")

client.run('TOKEN')
