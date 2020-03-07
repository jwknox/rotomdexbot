# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
import gen1
import gen5

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")

@bot.command(name='stat')
async def stat(ctx):
    cmdargs = ctx.content.split()
    pokemon = cmdargs[1]
    gen = 0
    if (len(cmdargs) > 2):
        gen = cmdargs[2].lstrip('gen')
    print("Stat called for " + pokemon + ", Gen ", end = '')
    if (gen):
        print(gen)
    else:
        print("unspecified")
    stats = 0
    if pokemon in gen1.gen1 and gen in (0, "1"):
        stats = gen1.gen1[pokemon]
    elif pokemon in gen5.gen5 and gen in (0, "2", "3", "4", "5"):
        stats = gen5.gen5[pokemon]
    if (stats):
        print("Returning " + stats)
        await ctx.send(stats)

if __name__ == "__main__":
    bot.run()
