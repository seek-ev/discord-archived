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

applicationExample = getVal("/config/application", "applicationExample")
DEVROLEID = int(getVal("/config/roles", "dev/developer"))


class DevApplyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="dev", invoke_without_command=True)
    async def dev_cmd(self, ctx):
        await ctx.send(applicationExample)
        return

    @dev_cmd.command(name="apply")
    async def dev_apply(self, ctx: Context, *, application_text):
        userid = ctx.author.id
        if checkExist("/applications/developer", "{0}".format(str(userid))):
            application = getVal("/applications/developer", "{0}".format(str(userid)))

            if application["status"] == "pending":
                return await ctx.send(
                    "Your application is being reviewed, please wait."
                )
            elif application["status"] == "banned":
                return await ctx.send("You cannot apply.")
            elif application["status"] == "accepted":
                return await ctx.send("You have already been accepted.")

        application_text = application_text.replace("`", "")
        lines = []
        for line in application_text.splitlines():
            if line != " " and line != "":
                lines.append(line)
        wherehelp = []
        for v in lines[0].split(","):
            v = v.split("#")[0]
            v = v.replace("[", "").replace("]", "").replace(" ", "", 1)
            wherehelp.append(v)
        username = lines[1].replace("username: ", "", 1).split("#")[0].strip()

        application = {
            "wherehelp": wherehelp,
            "username": username,
            "reason": lines[2].replace("reason: ", "", 1).split("#")[0],
            "status": "pending",
            "try": 1 if not application else application["try"] + 1,
        }

        setVal("/applications/developer", "{0}".format(str(userid)), application)
        return

    @dev_cmd.command(name="accept")
    @is_bot_owner()
    async def dev_accept(self, ctx: Context, user: discord.User):
        status = getVal(f"/applications/developer/{user.id}", "status")
        if status == "accepted":
            return await ctx.send("This user has already been accepted")
        setVal(f"/applications/developer/{user.id}", "status", "accepted")

        dev_guild = self.bot.get_guild(int(getVal("/config/guilds", "dev")))
        default_channel = dev_guild.get_channel(764854987217567765)
        invite = await default_channel.create_invite(
            max_uses=1, reason=f"User application for {user} accepted"
        )

        await user.send(
            f"Your application has been accepted. "
            f"Please join the dev server: {str(invite)}"
        )

        return

    @dev_cmd.command(name="list")
    @is_bot_owner()
    async def dev_list(self, ctx: Context):
        await ctx.trigger_typing()

        applications = getVal("/applications/developer")
        embed = discord.Embed(title="Applications")

        for user_id, i in applications.items():
            user = await ctx.bot.fetch_user(user_id)

            embed.add_field(
                name=f"**{str(user)} ({i['username']})**",
                value=f"**Help with**: {', '.join(i['wherehelp'])}\n**Reason**: {i['reason']}",
                inline=False,
            )

        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DevApplyCommands(bot))
