import json
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


def initFirebase():
    cred = credentials.Certificate(os.environ.get('firebase'))
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.environ.get('firebase-database-url'),
    })


def getVal(path='/', child=''):
    ref = db.reference(path)
    if child != '':
        ch = ref.child(child)
        return ch.get()
    return ref.get()


def setVal(path, child, data):
    ref = db.reference(path)
    ch = ref.child(child)
    ch.set(data)


def checkExist(path='/', child=''):
    check = getVal(path, child)
    if check is not None:
        return True
    return False
