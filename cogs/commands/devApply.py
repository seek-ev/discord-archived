from discord.ext import commands

from modules.database import getVal
from modules.permissions import is_bot_owner

# applicationExample = 'Example application:' \
#                      '```[discord, dev-api, website] # what do you want to help with \n' \
#                      'username: SerekKiri # github username\n' \
#                      'reason: I love this project! # reason why do you want to join us (nullable)```' \
#                      '**Please use ``` wrapped around application**'

applicationExample = getVal('/config/application', 'applicationExample')


class DevApplyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='dev', invoke_without_command=True)
    async def devcmd(self, ctx):
        await ctx.send(applicationExample)
        return

    @devcmd.command(name='apply')
    async def dev_apply(self, ctx, *, arg):
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

    # @command(name="dev accept")
    # @is_bot_owner()
    # async def devAccept(self, ctx: Context):
    #     return


def setup(bot):
    bot.add_cog(DevApplyCommands(bot))
