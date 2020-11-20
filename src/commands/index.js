// Commands
import { help } from './help'
import { applyTester } from './tester/apply'
import { acceptTester } from './tester/accept'

export const commands = (msg, client) => {
    const content = msg.content.split('!')[1]

    // Check if message includes prefix if not just omit it
    if (!msg.content.toLowerCase().startsWith('!')) return

    if (content === 'apply') return applyTester(msg, client)

    if (content.startsWith('accept')) return acceptTester(msg, client)

    if (content === 'help') return help(msg)

    return
}
