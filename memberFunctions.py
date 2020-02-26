from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from getpass import getpass
import firebase_admin
import pyrebase

# User Login
def userLogin(email):
    cred = credentials.Certificate('Path to credential file.json')
    project_id = 'project_id'
    firebase_admin.initialize_app(cred, {
    'projectId': project_id,
    })
    firebaseConfig = {
    
    "apiKey": "apiKey",
    "authDomain": "authDomain",
    "databaseURL": "databaseURL",
    "projectId": "projectId",
    "storageBucket": "storageBucket",
    "messagingSenderId": "messagingSenderId",
    "appId": "appId",
    "measurementId": "measurementId"
    }
    # This will be wrapped inside of pyrebase
    firebase = pyrebase.initialize_app(firebaseConfig)
    theAuth = firebase.auth()
    # Check to see if user is verified
    import sys
    user = auth.get_user_by_email(email)
    ruVerified = '{}'.format(user.email_verified)
    if ruVerified == 'True':
        theName = '{}'.format(user.display_name)
        theMaster = theName[12:18]
        welcomeMessage = ('Welcome %s.' %(theName)+'\nPlease sign in.')
        print(welcomeMessage)
    else:
        print('''Your email has not been verified.\n
Please verify your email first.
''')
        sys.exit()
    email = input('Please enter your email: ')
    password = input('Please enter your password: ')
    login = theAuth.sign_in_with_email_and_password(email, password)

    if theMaster =! 'Master':

        bUserMenu = '''
1.) => Pay Bill
2.) => Change Plan
3.) => Class Schedule
'''
        print(bUserMenu)

        userMenuChoice = input('What would you like to do today: ')
        while userMenuChoice != '1' and userMenuChoice != '2' and userMenuChoice != '3':
            menuMessage = "That is not a valid choice."
            print(menuMessage)
            userMenuChoice = input('What would you like to do today: ')

        billPay = '''
Bill Pay Menu
1.) => Lerom Ipsum
2.) => Occaecat Cupidatat
3.) => Excepteur Sint
'''
        changePlan = '''
Change Plan Menu
1.) => Lerom Ipsum
2.) => Occaecat Cupidatat
3.) => Excepteur Sint
'''
        classSchedule = '''
Class Schedule Menu
1.) => Lerom Ipsum
2.) => Occaecat Cupidatat
3.) => Excepteur Sint
'''
        if userMenuChoice == '1':
        print(billPay)
        if userMenuChoice == '2':
        print(changePlan)
        if userMenuChoice == '3':
        print(classSchedule)
     else:

         masterMenu = '''
1.) => Add Member
2.) => Find Member
3.) => Update Member
'''
         print(masterMenu)
        masterChoice = input('What would you like to do today: ')
        while masterChoice != '1' and masterChoice != '2' and masterChoice != '3':
             print('That is not a valid entry.\nPlease try again.')
             masterChoice = input('What would you like to do today: ')

        if masterChoice == '1':
            theAdd = Class.addUser()
        if masterChoice == '2':
            theFind = Class.findUser()
        if masterChoice == '3':
            theUpdate = Class.updateUser()
    

# I will make the master user enter thier username and password
    else:
        print('''Your email has not been verified.\n
Please verify your email first.
''')
        sys.exit()
    email = input('Please enter your email: ')
    password = input('Please enter your password: ')
    login = theAuth.sign_in_with_email_and_password(email, password)

    bUserMenu = '''
1.) => Pay Bill
2.) => Change Plan
3.) => Class Schedule
'''
    print(bUserMenu)
    

