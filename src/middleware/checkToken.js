export const checkToken = (req, res, next) => {
    const authHeader = req.headers['authorization']

    if (!authHeader) return res.status(401).send()

    const token = authHeader.split(' ')
    if (token.length < 2 || token[0] !== 'API')
        return res.status(401).json({ error: 'Wrong formatted header' })

    if (token[1] !== process.env.TOKEN) return res.status(401).send()

    next()
}