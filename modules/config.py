import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
apiAuth = os.getenv('auth')
api = os.getenv('api')
owners_id = os.getenv('owners')
firebasesdk = os.getenv('firebase')
firebasedatabaseurl = os.getenv('firebase-database-url')


def getToken():
    return token


def getApiAuth():
    return apiAuth


def getApiUrl():
    return api


def getOwners():
    oid = owners_id.replace(" ", "").split(",")
    return oid


def getFirebaseSDK():
    return firebasesdk


def getFirebaseDatabaseUrl():
    return firebasedatabaseurl
