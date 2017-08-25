# This is a bot that does not use the commands.ext extension, meaning all commands are manually made.
# It uses the on_message event to use these commands. First, start by importing discord.
import discord

client = discord.Client() # client can be replaced with anything, but this is commonly used as client, so it will be what I use.

@client.event
async def on_message(message):
    prefix = "$" # prefix can be replaced by anything you want.
    
    if message.content.startswith(prefix+"test"):
        await client.send_message(message.channel, "Test recieved!")
       
    # Here are a couple other ways to do stuff like this.
    
    args = message.content
    args = args.replace(prefix, "")
    args = args.split
    command = args[0]
    if message.content.startswith(prefix):
        if command == "hello":                                    # Just an example of how formats work, it replaces the number 
            if len(message.mentions) > 0:                         # of its position in the array.
                await client.send_message("{0.mention} says hello to {1.mention}".format(message.author, message.mentions[0]))
            else:
                await client.send_message("Hello, {0.mention}!".format(message.author))
                
                
        if command == "goodbye":
            if len(message.mentions) > 0:
                await client.send_message("{0.mention} says goodbye to {1.mention}".format(message.author, message.mentions[0]))
            else:
                await client.send_message("Goodbye, {0.mention}!".format(message.author))
                
                
@client.event
async def on_ready():
    print("Starting bot user.")
    
client.run('token')
