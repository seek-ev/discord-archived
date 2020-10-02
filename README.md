### Sneaky-bot [![Discord](https://img.shields.io/discord/736597524256915478?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/GQ4ddQM)

<br />

Bot designed for [seek-ev](https://seek-ev.com/) community on discord.

## Requirements:

- [python 3](https://www.python.org/downloads/)

## Running project:

### (Optional) First create virtual env:

```
 python3 -m venv /path/to/new/virtual/environment
```
And enter to it.

### Install required depedencies:

```
 pip install -r requirements.txt
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
 python3 generate_database.py
```


### Run bot app:

```
 python3 main.py
```

If you have any issues join our [discord](https://discord.gg/GQ4ddQM) community.
