# Hey there!
This is a bit more complicated of a feature, but it does allow you to create commands like `urban`, `cat`, `dog`, `ytsearch`, and more. 
This uses the `requests` module, which I will assume you already have. If not, I will not be able to help you with that.

# Random Cat Command
For this command, I use the http://random.cat/meow api. At the top of your code, `import requests` and `import json`. Here is an example.
```py
import requests
import json
```
Just add that in with your other imports and you then should be able to get started. 
When you go to the http://random.cat/meow page, you should see something ***similar*** to this (not exactly like it).
```json
{"file":"http:\/\/random.cat\/i\/smPafU3.jpg"}
```
Use the requests module to get the link, which should look something like this:
```py
r = requests.get('http://random.cat/meow')
```
Now, if you have it say this, it might say something like `<Response [200]>`. Here's where the `json` module comes in. 
Simply do something like this to make the program read the JSON of the webpage.
```py
r = requests.get('http://random.cat/meow')
js = r.json()
```
The `js` variable is now subscriptable. Use this to send the file part of the json. Here is a very basic example for a command using this api.
```py
@bot.command()
async def cat(ctx):
    r = requests.get('http://random.cat/meow')
    js = r.json()
    await ctx.say(js['file'])
```
Now that you have this, you should be able to use this method with any **JSON** APIs that don't require authorization keys. 
I will do another guide with using authorization keys and with other methods (like xml APIs). 

~**Desii** ♥
