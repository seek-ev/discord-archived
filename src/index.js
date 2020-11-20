import * as bodyParser from 'body-parser'
const Discord = require('discord.js')
const express = require('express')
require('dotenv').config()

// Discord client
const client = new Discord.Client()

// Express client
const app = express()
app.use(bodyParser.json())

// Commands
import { commands } from './commands/index'

// API
import { addRole } from './api/role'

// Middleware
import { checkToken } from './middleware/checkToken'

// Few simple routes
app.get('/', (req, res) => {
    return res.status(200).json({
        "API_VERSION": "0.0.1",
        "DOCS": null
    })
})

app.post('/', [checkToken], (req, res) => addRole(req, res, client))

client.on('ready', () => {
    console.log('Bot ready and running')
})

client.on('message', msg => commands(msg, client))

app.listen(process.env.PORT || 3000, () => {
    console.log(`API ready and listening on port ${process.env.PORT || 3000}`)
})

client.login(process.env.BOT_TOKEN)
