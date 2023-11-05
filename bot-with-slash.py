import discord
import qrcode
from discord.ext import commands
from discord import app_commands
import os
from keep_alive import keep_alive

client =discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)
@client.event
async def on_command_error(ctx, error):
  await ctx.send(f"An error occured: {str(error)}")
@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=865202347038605362))
  print(f"I am ready to go - {client.user.name}")
  await client.change_presence(activity=discord.Activity(
      type=discord.ActivityType.watching, name=f'Barbenheimer'))
@tree.command(name="ping",description="Displays server ping.",
             guild=discord.Object(id=865202347038605362))
async def _ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"Ping: {client.latency}")
@tree.command(name="qr",description="Generates a QR with slash commands",guild=discord.Object(id=865202347038605362))
async def _command(interaction: discord.Interaction, url: str):
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
  await interaction.response.send_message(embed=embed, file=file)

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
