import firebase_admin
from firebase_admin import firestore

def initialize_firebase_db():
  firebase_admin.initialize_app()
  db = firestore.client()
  
  return db