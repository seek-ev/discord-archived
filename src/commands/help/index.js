export const help = async (msg) => {
    const embed = {
        title: 'Available commands:',
        author: {
            name: 'seek-ev.com',
            url: 'https://seek-ev.com',
            icon_url:
                'https://seekev.s3.eu-central-1.amazonaws.com/b/256/se.png',
        },
        description: `
            - tester apply (use to apply for a tester role)
        `,
        color: 1947988,
        footer: {
            icon_url:
                'https://seekev.s3.eu-central-1.amazonaws.com/b/32/discord.png',
            text: 'Seek EV',
        },
    }

    return await msg.channel.send({ embed })
}