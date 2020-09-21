import json
import io

import discord
from discord.ext import commands
from discord.ext.commands import Context

from modules.database import getVal, setVal, checkExist
from modules.permissions import is_bot_owner

# applicationExample = 'Example application:' \
#                      '```[discord, dev-api, website] # what do you want to help with \n' \
#                      'username: SerekKiri # github username\n' \
#                      'reason: I love this project! # reason why do you want to join us (nullable)```' \
#                      '**Please use ``` wrapped around application**'

applicationExample = getVal('/config/application', 'applicationExample')
DEVROLEID = int(getVal('/config/roles', 'developer'))


class DevApplyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='dev', invoke_without_command=True)
    async def dev_cmd(self, ctx):
        await ctx.send(applicationExample)
        return

    @dev_cmd.command(name='apply')
    async def dev_apply(self, ctx: Context, *, application):
        userid = ctx.author.id
        if checkExist('/applications/developer', '{0}'.format(userid)):
            await ctx.send('Your application is reviewing, please wait.')
            return
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
        username = lines[1].replace('username: ', '', 1).split('#')[0].strip()
        application = {
            'wherehelp': wherehelp,
            'username': username,
            'reason': lines[2].replace('reason: ', '', 1).split('#')[0],
        }
        if not checkExist('/applications/developer', '{0}'.format(userid)):
            setVal('/applications/developer', '{0}'.format(userid), application)
        return

    @dev_cmd.command(name="accept")
    @is_bot_owner()
    async def dev_accept(self, ctx: Context, user_mention_or_id):
        userid = int(user_mention_or_id.replace('<@!', '').replace('>', ''))
        guild = ctx.guild
        role = guild.get_role(DEVROLEID)
        user = guild.get_member(userid)
        if role and user is not None:
            await user.add_roles(role)
        return

    @dev_cmd.command(name="list")
    @is_bot_owner()
    async def dev_list(self, ctx: Context):
        applications = getVal('/applications/developer')
        message = json.dumps(applications, indent=1)
        if not len(message) > 1950:
            message = '```json\n' + json.dumps(applications, indent=1) + '```'
            await ctx.send(message)
        else:
            f_msg = io.StringIO(message)
            f: discord.File = discord.File(fp=f_msg, filename='applications.json')
            await ctx.send(file=f)
        return


def setup(bot):
    bot.add_cog(DevApplyCommands(bot))
