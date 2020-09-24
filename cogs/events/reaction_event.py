import discord
from discord.ext import commands


class ReactionEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self: discord.client, payload):
        uid = payload.user_id
        gid = payload.guild_id
        emoji = payload.emoji
        msgid = payload.message_id
        guild: discord.Guild = discord.utils.get(self.bot.guilds, id=gid)
        member: discord.Member = discord.utils.get(guild.members, id=uid)
        if Member is not None:
            print(member)
        return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        uid = payload.user_id
        gid = payload.guild_id
        emoji = payload.emoji
        msgid = payload.message_id
        guild: discord.Guild = discord.utils.get(self.bot.guilds, id=gid)
        member: discord.Member = discord.utils.get(guild.members, id=uid)
        if Member is not None:
            print(member)
        return



def setup(bot):
    bot.add_cog(ReactionEvent(bot))
