# bot.py
# import neccesarey libraries for discord.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from discord.ext import commands


# import other neccesary libraies
import random


# initialize token
load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
# GUILD = os.getenv('DISCORD_GUILD')
# GUILD = os.environ['DISCORD_GUILD']

# clear terminal
os.system('clear')

# initialize colors
pri='\033[0;0m'  # reset color
sec='\033[1;34m' # secondary color
acc='\033[1;36m' # accent color

# initialize botr
bot = commands.Bot(command_prefix='/')


class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot

  @bot.command(name='flip', help="Flip a coin!")
  async def flip(ctx):
    sides = ["heads", "tails"]
    choice = random.choice(sides)
    await ctx.send(f"The coin landed on **{choice}**")
    

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(MyCog(bot))