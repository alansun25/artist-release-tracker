import os
import firebase_admin
from firebase_admin import credentials, firestore


def initialize_firebase_db():
    cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    return db
