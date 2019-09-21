import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import collections
import time

cred = credentials.Certificate('C:/Python27/wally-97049-firebase-adminsdk-dfd5r-ddf4fc63d3.json')

firebase_admin.initialize_app(cred, {'databaseURL' : 'https://wally-97049.firebaseio.com/'})

ref  = db.reference('/users')


# query consists of two components
# 1) ordering constraint i.e. 'order by child'
# 2) filtering constraint i.e. 'limit, range'

data0 = {'Janice': {'date_of_birth': 'Oct 13, 1952','full_name': 'Janice Miller'}}
data1 = {'alanisawesome': {'date_of_birth': 'June 23, 1912','full_name': 'Alan Turing'}}
data2 = {'gracehop': {'date_of_birth':'December 9, 1906','full_name': 'Grace Hopper'}}
data3 = {'Wally': {'date_of_birth': 'Sep 22, 2014','full_name': 'Wally Miller'}}
data4 = {'Mikey': {'date_of_birth': 'Aug 14, 1958','full_name': 'Michael D Corbridge'}}

ref.update(data0)
ref.update(data1)
ref.update(data2)
ref.update(data3)
ref.update(data4)


query = ref.order_by_key().limit_to_first(1)


result = query.get()
print result

print ""
print "---------------------------------------------"

user = result.items()[0]
print type(user)
print user
print user[0]
print user[1]
print type(user[1])
print user[1]['date_of_birth']



print ""
print "---------------------------------------------"

wallyRef = ref.child('Wally')
wallyRef.update({'full_name': 'Foxwood Walking the Walk'})

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
   time.sleep(5)
   
print "Good bye!"





