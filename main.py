# import neccesarey libraries for discord.py
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import discord
import typing
from translate import Translator

# import other neccesary libraies
import random

# initialize token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# style stuff
pri = '\033[0;0m'  # reset color
sec = '\033[1;34m'  # secondary color
acc = '\033[1;36m'  # accent color

# guild ids
guild_cmg = discord.Object(976586132391338054)
guild_test = discord.Object(978353904339288064)


# initialize bot
class Bot(commands.Bot):
    async def setup_hook(self):
        await bot.add_cog(Events(bot))  # Events
        await bot.add_cog(Random(bot))    # Random
        # await bot.add_cog(MyCog(bot))    # test
        tree = self.tree
        # await tree.sync(guild=discord.Object(976586132391338054))
        await tree.sync()

        # tree.copy_global_to(guild=guild_test)
        # await tree.sync(guild=guild_test)

        # tree.copy_global_to(guild=guild_cmg)
        # await tree.sync(guild=guild_cmg)


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = Bot(command_prefix=('!'), intents=intents,
          application_id="977995844097802240")


# create event cog


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"""\n{pri}MotionLink is connected to:""")
        print(f"""----------------------------------------------------""", end=' ')
        # guild = discord.utils.get(bot.guilds)
        for guild in bot.guilds:
            print(f"""\n{sec}{guild.name} {acc}[{guild.id}]""", end=' ')
        print(f"""\n{pri}----------------------------------------------------""")


# create sync cogs
class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    # add a command to sync the command tree lcoally or globally
    @bot.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: typing.Optional[typing.Literal["local", "global"]] = None) -> None:
        if not guilds:
            if spec == "local":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                fmt = await ctx.bot.tree.sync(guild=ctx.guild)
                await ctx.send(f"The command tree has been locally copied.")
            elif spec == "global":
                fmt = await ctx.bot.tree.sync(guild=ctx.guild)
                await ctx.send(f"The command tree has been globally copied.")
            else:
                await ctx.send(f"Kindly select if you wish to sync the command tree *locally* or *globally* when running the command.")

            return


# create command cogs
class Random(commands.GroupCog, name="random"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()  # this is now required in this context.

    @app_commands.command(name="coin")
    async def coin(self, ctx) -> None:
        await self.bot.wait_until_ready()
        """ Flip a coin. """
        sides = ["heads", "tails"]
        choice = random.choice(sides)
        await ctx.send(f"The coin landed on **{choice}**.")

    @app_commands.command(name="dice")
    async def dice(self, ctx) -> None:
        await self.bot.wait_until_ready()
        """ Roll a dice with six sides. """
        choice = random.randrange(6)
        await ctx.send(f"The dice landed on **{choice}**.")



class Translate(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  @app_commands.command(name="chinese")
  async def chinese(self, interaction: discord.Interaction, text: str) -> None:
    """ Translate english text into chinese. """
    translator= Translator(from_lang="english",to_lang="chinese")
    print(translation)
    translation = translator.translate("Guten Morgen")
    await interaction.response.send_message(translation, ephemeral=True)
    







      
# run the bot
bot.run(TOKEN)


# # initialization
# @bot.event
# async def on_ready():
#     print(f"""{pri}MotionLink is connected to:
# ----------------------------------------------------""", end=' ')
#     guild = discord.utils.get(bot.guilds)
#     print(f"""\n{sec}{guild.name} {acc}[{guild.id}]""")
#     print(f"""{pri}----------------------------------------------------""")


# # funcitons

# @bot.command(name='flip', help="Flip a coin!")
# async def flip(ctx):
#     sides = ["heads", "tails"]
#     choice = random.choice(sides)
#     await ctx.send(f"The coin landed on **{choice}**")


# @bot.command(name='setup', help="Easily setup your server by creating channels and roles!")
# @commands.has_role('admin')
# async def setup(ctx, channel_name):
#     guild = ctx.guild
#     if channel_name != '':
#         exists_channel = discord.utils.get(guild.channels, name=channel_name)
#         if not exists_channel:
#             channel_name = f"💬》{channel_name}"
#             print(f"{pri}New channel: {channel_name}")
#             await guild.create_text_channel(channel_name)


# # error handling

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send('You do not have the correct role for this command.')


# bot.run(TOKEN)
