import discord
import random
import time
def get_bot_token():
    with open("/usr/share/bot/token.txt", "r") as f:
         return f.read()
print("Foxbot is starting up...")
bot_token = get_bot_token()
print("Your bot token is: ", bot_token)
print("Starting server in 5 seconds...")
time.sleep(5)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'pic':
            img = random.randrange(1,123)
            await message.channel.send('https://randomfox.ca/?i={}'.format(img))
        if message.content == 'picbomb':
            my_msg = 'https://randomfox.ca/?i={}'.format(random.randrange(1,123))
            for i in range(5):
              my_msg += '\n https://randomfox.ca/?i={}'.format(random.randrange(1,123))
            await message.channel.send(my_msg)
        if message.content == 'credits':
            await message.channel.send('Bot with images "loaned" from xinitrc - randomfox.ca, bot run and hosted by Jonte')
        if message.content == 'source':
            await message.channel.send('Click here for source code: https://github.com/Jontes-Tech/fox-bot/')

client = MyClient()
client.run(bot_token)