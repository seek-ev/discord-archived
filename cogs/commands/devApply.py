from discord.ext import commands
from discord.ext.commands import Context

from modules.database import getVal, setVal
from modules.permissions import is_bot_owner

# applicationExample = 'Example application:' \
#                      '```[discord, dev-api, website] # what do you want to help with \n' \
#                      'username: SerekKiri # github username\n' \
#                      'reason: I love this project! # reason why do you want to join us (nullable)```' \
#                      '**Please use ``` wrapped around application**'

applicationExample = getVal('/config/application', 'applicationExample')
devRoleId = int(getVal('/config/roles', 'developer'))


class DevApplyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='dev', invoke_without_command=True)
    async def devcmd(self, ctx):
        await ctx.send(applicationExample)
        return

    @devcmd.command(name='apply')
    async def dev_apply(self, ctx, *, application):
        application = application.replace('`', '')
        lines = []
        for line in application.splitlines():
            if line != ' ' and line != '':
                lines.append(line)
        wherehelp = []
        for v in lines[0].split(','):
            v = v.split('#')[0]
            v = v.replace('[', '').replace(']', '').replace(' ', '', 1)
            wherehelp.append(v)
        username = lines[1].replace('username: ', '', 1).split('#')[0],
        userid = ctx.author.id
        application = {
            'wherehelp': wherehelp,
            'username': username,
            'reason': lines[2].replace('reason: ', '', 1).split('#')[0],
        }
        setVal('/applications/developer', '{0}'.format(userid), application)
        return

    @devcmd.command(name="accept")
    @is_bot_owner()
    async def devAccept(self, ctx: Context, userMentionOrId):
        userid = int(userMentionOrId.replace('<@!', '').replace('>', ''))
        guild = ctx.guild
        role = guild.get_role(devRoleId)
        user = guild.get_member(userid)
        if role and user is not None:
            await user.add_roles(role)
        return


def setup(bot):
    bot.add_cog(DevApplyCommands(bot))
