# import neccesarey libraries for discord.py
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import discord

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
guild_cmg = 976586132391338054
guild_test = 978353904339288064


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# initialize bot
class Bot(commands.Bot):
    async def setup_hook(self):
        await bot.add_cog(Events(bot))  # Events
        await bot.add_cog(test(bot))    # test
        tree = self.tree
        # await tree.sync(guild=discord.Object(976586132391338054))
        await tree.sync()


bot = Bot(command_prefix=(), intents=discord.Intents(
    messages=True, guilds=True), application_id="977995844097802240")


# create event cog
class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"""{pri}MotionLink is connected to:""")
        print(f"""----------------------------------------------------""", end=' ')
        # guild = discord.utils.get(bot.guilds)
        for guild in bot.guilds:
            print(f"""\n{sec}{guild.name} {acc}[{guild.id}]""", end=' ')
        print(f"""\n{pri}----------------------------------------------------""")


# create command cogs
class test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="ping")
    async def ping_command(self, ctx: commands.Context) -> None:
        """
        This command is actuallyfg used as an app command AND
        """

        await ctx.send("Hello!")
        # we use ctx.send and this will handle both the message command and app command of sending.
        # added note: you can check if this command is invoked as an app command by checking the `ctx.interaction` attribute.

    @commands.hybrid_group(name="parent")
    async def parent_command(self, ctx: commands.Context) -> None:
        """
        We even have the use of parents. This will work as us
        """
        ...   # nothing we want to do in here, I guess!

    @parent_command.command(name="sub")
    async def sub_command(self, ctx: commands.Context, argument: str) -> None:
        """
        This subcommand can now be invoked 
        """

        await ctx.send(f"Hello, you sent {argument}!")

    @app_commands.command(name="command-1")
    async def my_command(self, interaction: discord.Interaction) -> None:
        """ djgasd ghasgd hasgd hagsd hags dhgas """
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)


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
