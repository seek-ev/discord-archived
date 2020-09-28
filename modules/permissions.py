from discord.ext import commands

from modules import config


def is_bot_owner():
    async def predicate(ctx):
        oid = config.get_owners()
        for o in oid:
            if o == str(ctx.author.id):
                return 1
        return 0

    return commands.check(predicate)
