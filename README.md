### Sneaky-bot [![Discord](https://img.shields.io/discord/736597524256915478?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/GQ4ddQM)

<br />

Bot designed for [seek-ev](https://seek-ev.com/) community on discord.

## Requirements:

- [python 3](https://www.python.org/downloads/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

## Running project:

### Install required depedencies:

```
pipenv install --python 3.8
```

### Set up .env file

```
token=discord bot token
prefix=pre-defined bot prefix
owners=discord user ids for bot owners
firebase=path to filebase key file
firebase-database-url=url to firebase realtime database
```

### (First time) Create Database:

```
pipenv run python generate_database.py
```

### Run bot app:

```
pipenv run start
```

If you have any issues join our [discord](https://discord.gg/GQ4ddQM) community.
