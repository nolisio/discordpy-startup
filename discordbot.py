
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='めいどちゃん、')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def おはよう(ctx):
    await ctx.send('おはようございます')

@bot.command()
async def 調子はどう？(ctx):
    await ctx.send('可もなく不可もなくといった感じですね')

@bot.command()
async def 好き(ctx):
    await ctx.send('変なこと言わないでくださいよ、もう')

bot.run(token)
