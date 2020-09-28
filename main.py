from discord.ext import commands

from modules import config
from modules.database import initFirebase

cogs = [
    "cogs.commands.dev_apply",
    "cogs.events.command_event",
    "cogs.events.reaction_event",
]

client = commands.Bot(
    owner_ids=config.get_owners(),
    case_insensitive=1,
    command_prefix=config.get_prefix(),
)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    for cog in cogs:
        client.load_extension(cog)
    return


if __name__ == "__main__":
    initFirebase()
    client.run(config.get_token(), bot=True, reconnect=True)
