import os
import discord
from discord.ext import commands

intents = discord.Intents.all()  # Instantiate the Intents instance, enabling all events
bot = commands.Bot(command_prefix='!', intents=intents)  # Pass the intents

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


defaultDIR = "/var/www/html/AIWeb3FrontEnd/"   

@bot.command()
async def gitpush(ctx):
    if ctx.author.id != 759849173729148928 and ctx.author.id != 890528272536993832:
        await ctx.send("没有权限使用这个命令!")
        return 
    os.chdir(defaultDIR)
    os.system("git pull")
    await ctx.send("git已经更新")

@bot.command()
async def gitconfig(ctx):
    if ctx.author.id != 759849173729148928 and ctx.author.id != 890528272536993832:
        await ctx.send("没有权限使用这个命令!")
        return 
    pathfolder = ctx.message.content[len("gitconfig")+1:].strip()
    if os.path.isdir(pathfolder):
        defaultDIR = pathfolder 
        await ctx.send("设置成功") 
    else:
        await ctx.send("文件夹不存在,请重新设置!")

token = os.getenv('aiweb3dev')
bot.run(token)
