from discord.ext import commands
from modules import config

cogs = ['commands.devApply']

bot = commands.Bot(owner_ids=config.getOwners(), case_insensitive=1, command_prefix="!")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for cog in cogs:
        bot.load_extension(cog)
    return


if __name__ == '__main__':
    bot.run(config.getToken(), bot=True, reconnect=True)
