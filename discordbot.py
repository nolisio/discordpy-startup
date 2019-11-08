from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='めいどちゃん、')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))  
    
@bot.command()
async def how are you(ctx):
    await ctx.send('可もなく不可もなくといった平常運転です')
    
bot.run(token)

