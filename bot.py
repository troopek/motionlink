# bot.py
# import neccesarey libraries for discord.py
import os
from dotenv import load_dotenv
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



######################################



class Greetings(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
      channel = member.guild.system_channel
      if channel is not None:
        await channel.send(f'Welcome {member}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
      """Says hello"""
      member = member or ctx.author
      if self._last_member is None or self._last_member.id != member.id:
          await ctx.send('Hello {0.name}~'.format(member))
      else:
          await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
      self._last_member = member


    
    @app_commands.command(name="top-command")
    async def my_top_command(self, interaction: discord.Interaction) -> None:
      """ /top-command """
      await interaction.response.send_message("Hello from top level command!", ephemeral=True)




    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(MyCog(bot))


  
################################################################




# initialization
@bot.event
async def on_ready():
  print(f"""{pri}MotionLink is connected to:
----------------------------------------------------""", end = ' ')
  guild = discord.utils.get(bot.guilds)
  print(f"""\n{sec}{guild.name} {acc}[{guild.id}]""")
  print(f"""{pri}----------------------------------------------------""")




  

# funcitons
  
@bot.command(name='flip', help="Flip a coin!")
async def flip(ctx):
  sides = ["heads", "tails"]
  choice = random.choice(sides)
  await ctx.send(f"The coin landed on **{choice}**")
  

  

@bot.command(name='setup', help="Easily setup your server by creating channels and roles!")
@commands.has_role('admin')
async def setup(ctx, channel_name):
  guild = ctx.guild
  if channel_name != '':
    exists_channel = discord.utils.get(guild.channels, name=channel_name)
    if not exists_channel:
      channel_name = f"💬》{channel_name}"
      print(f"{pri}New channel: {channel_name}")
      await guild.create_text_channel(channel_name)




# error handling
      
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
      await ctx.send('You do not have the correct role for this command.')







bot.run(TOKEN)
