# This is the setup for the memberPlay file

# The user will enter thier memberID
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import firebase_admin
import json

# Path to json file that stores my credentials
cred = credentials.Certificate('/Users/simonehill/Desktop/PYTHON FILES/gymMembers/bobsrealKey.json')
# Project ID
project_id = 'bobsburgers-5d057'
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})
uid = "KYPC041rbdcucKgSvPID8d5BJj83"
user = auth.get_user(uid)
print('Successfully fetched user data: {0}'.format(user.email))



