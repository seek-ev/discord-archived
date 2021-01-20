export const removeRole = async (req, res, client) => {
    const { userId } = req.body

    if (!userId) return res.status(400).json({ error: { message: 'Missing userId in request body' } })

    const guild = await client.guilds.fetch(process.env.GUILD_ID)

    const foundMember = guild.members.cache.find(m => m.id === userId)

    if (!foundMember) return res.status(404).json({ error: { message: `User with id: ${userId} was not found` } })

    if (foundMember.roles.cache.some(role => role.id === process.env.DISCORD_ROLE)) {
        try {
            await foundMember.roles.remove(process.env.DISCORD_ROLE, `${foundMember.user.username} disconnected his/hers discord to Seek EV`)
        } catch (err) {
            return res.status(500).json({ error: err })
        }
    }

    return res.status(200).send()
}