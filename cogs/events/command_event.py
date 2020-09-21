from discord.ext import commands


class ReactionEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass


def setup(bot):
    bot.add_cog(ReactionEvent(bot))
