from discord.ext import commands
from discord.ext.commands import command, Context

applicationExample = 'Example application:' \
                     '```[discord, dev-api, website] # what do you want to help with \n'\
    'username: SerekKiri # github username\n' \
    'reason: I love this project! # reason why do you want to join us (nullable)```'\
    '**Please use ``` wrapped around application**'


class DevApplyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='dev', rest_is_raw=True)
    async def dev(self, ctx: Context, *, arg):
        if len(arg) <= 0:
            await ctx.send(applicationExample)
            return
        arg = arg.replace('`', '')
        lines = []
        for line in arg.splitlines():
            if line != ' ' and line != '':
                lines.append(line)
        wherehelp = []
        for v in lines[0].split(','):
            v = v.split('#')[0]
            v = v.replace('[', '').replace(']', '').replace(' ', '', 1)
            wherehelp.append(v)
        application = {
            'wherehelp': wherehelp,
            'username': lines[1].replace('username: ', '', 1).split('#')[0],
            'reason': lines[2].replace('reason: ', '', 1).split('#')[0],
        }
        print(application)
        return


def setup(bot):
    bot.add_cog(DevApplyCommands(bot))
