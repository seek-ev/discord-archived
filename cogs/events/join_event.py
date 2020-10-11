from discord import Member, Object
from discord.ext import commands

from modules.database import getVal


DEVROLEID = int(getVal("/config/roles", "dev/developer"))


class JoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        dev_guild = self.bot.get_guild(int(getVal("/config/guilds", "dev")))

        if member.guild != dev_guild:
            return

        application = getVal("/applications/developer", str(member.id))
        if application["status"] == "accepted":
            # TODO: Assign roles based on 'wherehelp'
            await member.add_roles(Object(DEVROLEID))


def setup(bot):
    bot.add_cog(JoinEvent(bot))
