import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='속보', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_error(event, *args, **kwargs):
    print('An error occurred:', event)

@bot.command()
async def ping(ctx):
    await ctx.channel.send('pong')

@bot.command(aliases=[")"])
async def breakingNews(ctx, *, title):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    embed=discord.Embed(title=f"[속보] {title}", description=f"{date}({ctx.author.display_name} 기자)", color=0xE62D36)
    await ctx.channel.send(embed=embed)

bot.run('MTEzMjcwNjUwMjMxMDkwMzg3OA.G-q6vN.orFzK4td9cVEfED_vpRddObTavkVnB6vyUye5Q')