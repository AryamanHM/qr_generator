import discord
import os
import cv2
from discord.ext import commands
import requests
from keep_alive import keep_alive
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("bot online")

@client.event
async def on_message(ctx):
    if ctx.attachments:
        url = ctx.attachments[0].url
        myfile = requests.get(url)
        open('todecode.png', 'wb').write(myfile.content)
        try:
          img = cv2.imread('todecode.png')
          detect = cv2.QRCodeDetector()
          value, points, straight_qrcode = detect.detectAndDecode(img)
          await ctx.channel.send(value)  # Use "await" to send a message
        except:
          await ctx.channel.send("Invalid Image")

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
