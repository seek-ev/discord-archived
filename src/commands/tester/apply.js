export const applyTester = async (msg, client) => {
    if (msg.channel.type !== 'dm') return await msg.reply('Hey hey, try to dm me!')

    const guild = await client.guilds.fetch(process.env.GUILD_ID)
    const channel = guild.channels.cache.find(c => c.id === process.env.CHANNEL_ID)

    const foundMember = guild.members.cache.find(m => m.id === msg.author.id)

    if (foundMember.roles.cache.some(role => role.id === process.env.TESTER_ROLE)) return await msg.reply('You\'re already a tester! <:tester:760160378117292043> :tada:')

    const embed = {
        author: {
            name: msg.author.username,
            icon_url: `https://cdn.discordapp.com/avatars/${msg.author.id}/${msg.author.avatar}`,
        },
        title: `${msg.author.username}#${msg.author.discriminator} applied`,
        description: msg.author.id,
        footer: {
            icon_url:
                'https://seekev.s3.eu-central-1.amazonaws.com/b/32/discord.png',
            text: new Date(msg.createdTimestamp).toLocaleString(),
        },
    }

    try {
        await channel.send({ embed })
        await msg.author.send('You\'re application was sent and will be processed...')
    } catch (err) { console.log(err) }

    return
}