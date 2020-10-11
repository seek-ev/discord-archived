import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")
apiAuth = os.getenv("auth")
api = os.getenv("api")
owners_id = os.getenv("owners")
firebasesdk = os.getenv("firebase")
firebasedatabaseurl = os.getenv("firebase-database-url")
prefix = os.getenv("prefix")


def get_token():
    return token


def get_api_auth():
    return apiAuth


def get_api_url():
    return api


def get_owners():
    oid = owners_id.replace(" ", "").split(",")
    return oid


def get_firebase_sdk():
    return firebasesdk


def get_firebase_database_url():
    return firebasedatabaseurl


def get_prefix():
    return prefix
