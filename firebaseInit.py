import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class FireBaseInit:
	def init(self):
		cred = credentials.Certificate('C:/Python27/wally-97049-firebase-adminsdk-dfd5r-ddf4fc63d3.json')
		firebase_admin.initialize_app(cred, {'databaseURL' : 'https://wally-97049.firebaseio.com/'})
		firebaseReference  = db.reference('/users')
		return firebaseReference