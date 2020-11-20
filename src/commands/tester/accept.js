export const acceptTester = async (msg, client) => {
    if (msg.author.id !== process.env.MAINTAINER_ID) return
    const content = msg.content.split('!')[1]

    const guild = await client.guilds.fetch(process.env.GUILD_ID)

    if (content.split(' ').length <= 1) return await msg.reply('Missing user id')

    const userId = content.split(' ')[1]

    const foundMember = guild.members.cache.find(m => m.id === userId)

    if (!foundMember) return await msg.reply(`Member with id: **${userId}** wasn\'t found`)

    if (foundMember.roles.cache.some(role => role.id === process.env.TESTER_ROLE)) return await msg.reply('User already have a tester role!')

    try {
        await foundMember.roles.add(process.env.TESTER_ROLE, 'Accepted for a tester role')
        await foundMember.send('Yours application have been accepted! :tada:\n\nHit to <#740316267323457586> for more details <:partner:760160334844919889> ')
    } catch (err) { console.log(err) }

    return
}