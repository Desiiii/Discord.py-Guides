# This will be a very basic bot using the commands.ext module of discord.py
# We start with the imports, which will be below.
import discord
from discord.ext import commands

description = """I am a basic bot made to show off what you can do with the commands.ext extension of discord.py."""

prefix = "?" # any prefix you wish can be used
bot = commands.Bot(command_prefix=prefix,description=description) # Bot can be anything you want. Some people use client or whatever, 
                                          # so it'd be client = commands.Bot(command_prefix=prefix,description=description)
                                          # Just make sure wherever I use "bot" in my code, you'd use what you defined.

@bot.event
async def on_ready(): # when the bot starts up
    print("Starting up bot user:\n{0.name}#{0.discriminator}\n{0.id}\n==========".format(bot.user))
    
# simple bot commands
@bot.command()
async def say(sayThis: str):
    await bot.say(sayThis) # This is a common way of doing it but throws an error with no args.
                           # The next command will be a better way of handling args.
                           
@bot.command(pass_context=True)
async def echo(ctx):
    args = ctx.message.content.replace(prefix+"echo", "")
    if args == "":
        await bot.say("Can't send an empty message.")
    else:
        await bot.say(args[1:])
        
# Now that is a couple basic commands I could think of. However, you will always have a help command unless you remove it. 
# It has a space for a description. You can use that for commands like seen in this next command.

@bot.command()
async def test():
    """OwO whats this?"""
    await bot.say("Test recieved!")
    
# Hey look at that. You have an extremely basic bot with very few features!... I know, you want more. 
# But at least you have something to start with. Finally, you should run the bot. Replace token with your bot's actual token.
bot.run('token')
