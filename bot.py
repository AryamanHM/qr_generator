import discord
import qrcode
import os
from keep_alive import keep_alive

client =discord.Client(command_prefix='!',intents=discord.Intents.all())
@client.event
async def on_command_error(ctx, error):
  await ctx.send(f"An error occured: {str(error)}")
@client.event
async def on_ready():
  print(f"I am ready to go - {client.user.name}")
  await client.change_presence(activity=discord.Activity(
      type=discord.ActivityType.watching, name=f'Eras Tour'))
@client.command(name="ping")
async def _ping(ctx):
  await ctx.send(f"Ping: {client.latency}")
@client.command(name="qr")
async def _command(ctx,url):
  qr = qrcode.QRCode(version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_L,
             box_size=50,
             border=2)
  qr.add_data(f'{url}')
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save("qr.png")
  
  # Create an embed with the image as an attachment
  embed = discord.Embed(title="HERE'S YOUR QR!", color=discord.Color.random())
  
  # Attach the image file to the embed
  file = discord.File("qr.png")
  embed.set_image(url="attachment://qr.png")
  
  # Send the embed with the attached image
  await ctx.send(embed=embed, file=file)

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
