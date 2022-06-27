from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="!")
client = discord.Client()
import json
with open('TOKEN.json', "r", encoding = "utf8") as file:
    data = json.load(file)
@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('快 還要更快')
    await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.event
async def on_message(message):
    global stop
    if message.author == bot.user:
        return
    if message.content.startswith("!repeat'"):
        stop = False
        tmp = message.content.split("'",3)
        if tmp[2] == "":
            while(stop==False):
                await message.channel.send(tmp[1])
        else:
            for i in range(int(tmp[2])):
                if stop == False:
                    await message.channel.send(tmp[1])
            else:
                return
    if message.content.startswith('!repeat"'):
        stop = False
        tmp = message.content.split('"',3)
        if tmp[2] == "":
            while(stop==False):
                await message.channel.send(tmp[1])
        else:
            for i in range(int(tmp[2])):
                if stop == False:
                    await message.channel.send(tmp[1])
            else:
                return
    if message.content.startswith("!repeat '"):
        stop = False
        tmp = message.content.split("'",3)
        if tmp[2] == "":
            while(stop==False):
                await message.channel.send(tmp[1])
        else:
            for i in range(int(tmp[2])):
                if stop == False:
                    await message.channel.send(tmp[1])
            else:
                return
    if message.content.startswith('!repeat "'):
        stop = False
        tmp = message.content.split('"',3)
        if tmp[2] == "":
            while(stop==False):
                await message.channel.send(tmp[1])
        else:
            for i in range(int(tmp[2])):
                if stop == False:
                    await message.channel.send(tmp[1])
            else:
                return
    if message.content.startswith('!stop'):
        stop = True
        return
bot.run(data['TOKEN'])