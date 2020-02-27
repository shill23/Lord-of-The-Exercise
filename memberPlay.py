# This is the setup for the memberPlay file

# The user will enter thier memberID
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import firebase_admin
import json

# Path to json file that stores my credentials
cred = credentials.Certificate('the_path_to_your_cred_file.json')
# Project ID
project_id = 'your_project_id'
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})
# The userID
theUID = input("Please enter the users ID")
uid = theUID
user = auth.get_user(uid)
print('Successfully fetched user data: {0}'.format(user.email))



