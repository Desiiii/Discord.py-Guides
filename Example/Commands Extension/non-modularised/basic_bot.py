# This will be a very basic bot using the commands.ext module of discord.py
# We start with the imports, which will be below.
import discord
from discord.ext import commands

description = """I am a basic bot made to show off what you can do with the commands.ext extension of discord.py."""

prefix = "?"  # any prefix you wish can be used
bot = commands.Bot(command_prefix=prefix,
                   description=description)  # Bot can be anything you want. Some people use client or whatever,


# so it'd be client = commands.Bot(command_prefix=prefix,description=description)
# Just make sure wherever I use "bot" in my code, you'd use what you defined.

@bot.event
async def on_ready():  # when the bot starts up
    print("Starting up bot user:\n{0.name}#{0.discriminator}\n{0.id}\n==========".format(bot.user))


@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)
        # Okay, so you may be confused.
        # Basically, what this does is it follows one other thing in the Discord Bot Best Practices
        # Which can be found here: https://github.com/meew0/discord-bot-best-practices
        # What this does is it ignores bots in the command execution. This means only non-bot accounts can use your bot.


# This command will be executed as so:
# Assuming the prefix is '?', you would do '?say memes'
# The result that the bot would send back is: 'memes'
@bot.command()
async def say(ctx, say_this: str):
    await ctx.send(say_this)  # This is a common way of doing it but throws an error with no args.


# This command will be executed as so:
# Assuming the prefix is '?', you would do '?hi @Desiree#3658' or '?hello @Desiree#3658'
# (replacing my mention with someone else's)
# The result that the bot would send back is: 'Hello there, @Desiree#3658!'
# If you did '?hi' or '?hello' with no mention
# The result would be: 'Hello there, @you!' (replacing @you with your mention)
@bot.command(aliases=["hello"])
async def hi(ctx, member: discord.Member = None):
    # This command shows off how to do aliases. Also, if you want to make an argument optional.
    if member is None:  # No argument passed
        u = ctx.author.mention  # Get the author of the message's mention
    else:
        u = member.mention  # If the member was provided, get theirs.
    await ctx.send(f"Hello there, {u}!")  # An 'f-string' is a way to format your string.
    # An alternative would be to do: "Hello there, {0}!".format(u)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
        # Basically, we do not want to send a message when an improper command is passed, as this is against the
        # Discord Bot Best Practices, which can be found here: https://github.com/meew0/discord-bot-best-practices
    else:
        # if the error is not handled above, we will send a message to the channel in which the command was executed.
        # Most of the time, if it is an error in arguments, it will tell what went wrong.
        await ctx.send(error)


# Now that is a couple basic commands I could think of.
# However, you will always have a help command unless you remove it.
# It has a space for a description. You can use that for commands like seen in this next command.

# This command will be executed as so:
# Assuming the prefix is '?', you would do '?test'
# The result that the bot would send back is: 'Test received'
@bot.command()
async def test():
    """OwO whats this?"""
    await bot.say("Test received!")


# Hey look at that. You have an extremely basic bot with very few features!... I know, you want more.
# But at least you have something to start with. Finally, you should run the bot.
# Replace token with your bot's actual token.
bot.run('token')
