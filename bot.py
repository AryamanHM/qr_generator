import discord
from discord.ext import commands
import qrcode
prefix = "!qr "
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
@client.event
async def on_ready():
  print(f"I am ready to go - {client.user.name}")
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.streaming, name=f"Barbenheimer"))
@client.event
async def on_command_error(ctx, error):
  await ctx.send(f"An error occured: {str(error)}")
@client.command(name="ping")
async def _ping(ctx):
  await ctx.send(f"Ping: {client.latency}")  
@client.command()
async def _command(ctx, arg1):
    qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=50,
                 border=2)
    qr.add_data(f'{arg1}')
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    img.save("advanced.png")
    with open('advanced.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
  