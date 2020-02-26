import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class User:

    def __init__(self, Member_ID,):
        self.member_ID = Member_ID
        print('Creating object')

    def __str__(self):
        return "My Member Id number is %s"%(self.member_ID)
    
    # This is how I will find each individual user
    def findUser(self):
        cred = credentials.Certificate('Path to credential file.json')
        project_id = 'project_id'
        firebase_admin.initialize_app(cred, {
          'projectId': project_id,
        })
        db = firestore.client()
        doc_ref = db.collection('members').document(self.member_ID)
        try:
            doc = doc_ref.get()
            userDict = eval('{}'.format(doc.to_dict()))
        except google.cloud.exceptions.NotFound:
            print(u'No such document!')
     
        # This is how I will print the user in my desired format       
        member_ID = "Member ID# : %s" %(userDict.get('Member ID#'))
        name = "Name : %s" %(userDict.get('Name'))
        age = "Age : %s" %(userDict.get('Age'))
        sex = "Gender : %s" %(userDict.get('Sex'))
        birthday = "Birthday : %s" %(userDict.get('Birthday'))
        membership_plan = "Membership Plan : %s" %(userDict.get('Membership Plan'))
        address = "Address : %s" %(userDict.get('Address'))
        interests = "Interests : %s" %(userDict.get('Interests'))
        nu_of_kids = "Nu of kids : %s" %(userDict.get('Nu of kids'))
        name_of_users_on_account = "Name of users on account : %s" %(userDict.get('Name of users on account'))
        key_card_holder = "Key card holder : %s" %(userDict.get('Key card holder'))
        additional_card_members = "Additional card members : %s" %(userDict.get('Additional card members'))
        email_address = "Email Address : %s" %(userDict.get('Email Address'))
        primary_phone = "Primary Phone : %s" %(userDict.get('Primary Phone'))
        secondary_phone = "Secondary Phone : %s" %(userDict.get('Secondary Phone'))
        user_login_type = "User Login Type : %s" %(userDict.get('User Login Type'))
        communication_preference = "Communication Preference : %s" %(userDict.get('Communication Preference'))
        print(member_ID)
        print(name)
        print(age)
        print(sex)
        print(birthday)
        print(membership_plan)
        print(address)
        print(interests)
        print(nu_of_kids)
        print(name_of_users_on_account)
        print(key_card_holder)
        print(additional_card_members)
        print(email_address)
        print(primary_phone)
        print(secondary_phone)
        print(user_login_type)
        print(communication_preference)

    # This function will allow me to add users to the FS database
    def addUser():
        name = input("Please enter the New Member's, Name:")
        age = input("\nPlease enter the New Member's, Age:")
        while age.isdigit() == False:
            print('This is not a valid entry.\nTry again!\nPlease enter a number')
            age = input("\nPlease enter the New Member's, Age:")
        theSex = int(input('''
These are the Sex Options:
1.) => Female
2.) => Male
3.) => Other
Please enter the New Member's, Sex: ''')
)
        while theSex != 1 and theSex != 2 and theSex != 3:
            print('This is not a valid entry.\nTry again!\nPlease enter number assigned to choice')
            theSex = int(input('''
These are the Sex Options:
1.) => Female
2.) => Male
3.) => Other
Please enter the New Member's, Sex: '''))   
        birthday = input('''
Please use this format to enter the Member's Birthday
(month)/(day)/(year)
Example : 09/04/1991
Please enter the New Member's, Birthday: ''')
        theMem_plan = int(input('''
These are the 4 Membership Plans:
1.) => Single Basic
2.) => Single Gold
3.) => Family Basic
4.) => Family Gold
Please enter the New Member's, Membership Plan:'''))
        while theMem_plan != 1 and theMem_plan != 2 and theMem_plan != 3 and theMem_plan != 4:
            print('This is not a valid entry.\nTry Again!. Please enter number assigned to choice.')
            theMem_plan = int(input('''
These are the 4 Membership Plans:
1.) => Single Basic
2.) => Single Gold
3.) => Family Basic
4.) => Family Gold
Please enter the New Member's, Membership Plan:'''))
        address = input("\nPlease enter the New Member's, Address:")
        interests = input("\nPlease enter the New Member's, Interests:")
        nu_of_kids = input("\nPlease enter the New Member's, Nu of kids:")
        while nu_of_kids.isdigit() == False:
            print('This is not a valid entry.\nTry Again!. Please enter a number.')
            nu_of_kids = input("\nPlease enter the New Member's, Nu of kids:")
        names_of_users_on_account = input('''
If there will be only 1 user
on this user account please type (same)
Please enter the New Member's, Name of users on account: ''')
        # I will skip userInput if no other users are on the account
        if names_of_users_on_account == "same":
            names_of_users_on_account = name
            key_card_holder = name
            additional_card_members = name
        else:
            key_card_holder = input("\nPlease enter the New Member's, Key card holder:")
            additional_card_members  = input("\nPlease enter the New Member's, Additional card members:")
        email_address  = input("\nPlease enter the New Member's, Email Address:")
        thePrimary_phone = input('''
Please use enter New Members Primary Phone Number
By following this criteria:
1.) Start with the area code
2.) Enter No spaces
Please enter the New Member's, Primary Phone:''')
        while thePrimary_phone.isdigit() == False:
            print('This is not a valid entry.\nTry Again!. Please enter all numbers.')
            thePrimary_phone = input('''
Please use enter New Members Primary Phone Number
By following this criteria:
1.) Start with the area code
2.) Enter no spaces
Please enter the New Member's, Primary Phone:''')
        theSecondary_phone = input('''
Please use enter New Members Secondary Phone Number
By following this criteria:
1.) Start with the area code
2.) Enter no spaces
Please enter the New Member's, Secondary Phone:''')
        while theSecondary_phone.isdigit() == False:
            print('This is not a valid entry.\nTry Again!. Please enter all numbers.')
            theSecondary_phone = input('''
Please use enter New Members Secondary Phone Number
By following this criteria:
1.) Start with the area code
2.) Enter no spaces
Please enter the New Member's, Secondary Phone:''')
            
        theUser_login_type = int(input('''
These are the 2 Login Types
1.) => Basic
2.) => Master
Please enter the New Member's, User Login Type:'''))
        while theUser_login_type != 1 and theUser_login_type != 2:
            print('This is not a valid entry.\nTry Again!. Please enter number assigned to choice.')
            theUser_login_type = int(input('''
These are the 2 Login Types
1.) => Basic
2.) => Master
Please enter the New Member's, User Login Type: '''))
        communication_preference = input("\nPlease enter the New Member's, Communication Preference:")
        # This Is where I will find that last user on account
        db = firestore.client()
        doc_ref = db.collection('members')
        docs = doc_ref.stream()
        for doc in docs:
            member_IDCount = []
            member_IDCount.append(doc.id)
            lastElement = member_IDCount[-1]
        
            lastElement = member_IDCount[0:4]
            lastString = str(lastElement)
            lastNumbers = int(lastString[10:13])
            newNumber = str(lastNumbers + 1)
            newMemberID = "memberID%s"%(newNumber)

        # Determine Sex
        theSex = int(theSex)
        if theSex == 1:
            sex = 'Female'
        else:
            if theSex == 2:
                sex = 'Male'
            else:
                if theSex == 3:
                    sex = 'Other'
        # Determine Membership plan
        theMem_plan = int(theMem_plan)
        if theMem_plan == 1:
            membership_plan = 'Single Basic'
        else:
            if theMem_plan == 2:
                membership_plan = 'Single Gold'
            else:
                if theMem_plan == 3:
                    membership_plan = 'Family Basic'
                else:
                    if theMem_plan == 4:
                        membership_plan = 'Family Gold'
        # Determine User Member Login Type
        theUser_login_type = int(theUser_login_type)
        if theUser_login_type == 1:
            user_login_type = 'Basic'
        else:
            if theUser_login_type == 2:
                user_login_type = 'Master'
        # I will format the Primary Phone Number
        primePhone = format(int(thePrimary_phone[:-1]), ",").replace(",", "-") + thePrimary_phone[-1]
        primary_phone = '({})-{}'.format(primePhone[0:3],primePhone[4:])
        # I will format the Secondary Phone Number
        secondPhone = format(int(theSecondary_phone[:-1]), ",").replace(",", "-") + theSecondary_phone[-1]
        secondary_phone = '({})-{}'.format(secondPhone[0:3],secondPhone[4:])
        # This is where the program will enter the iformation for me
        user_ref = db.collection(u'members').document(u'%s'%(newMemberID))
        user_ref.set({
        u'Name': u'{}'.format(name),
        u'Age': u'{}'.format(age),
        u'Sex': u'{}'.format(sex),
        u'Birthday': u'{}'.format(birthday),
        u'Plan': u'{}'.format(membership_plan),
        u'Address': u'{}'.format(address),
        u'Interests': u'{}'.format(interests),
        u'Nu of kids': u'{}'.format(nu_of_kids),
        u'Name of users on account': u'{}'.format(names_of_users_on_account),
        u'Key card holder': u'{}'.format(key_card_holder),
        u'Additional card members': u'{}'.format(additional_card_members),
        u'Email Address': u'{}'.format(email_address),
        u'Primary Phone': u'{}'.format(primary_phone),
        u'Secondary Phone': u'{}'.format(secondary_phone),
        u'User Login Type': u'{}'.format(user_login_type),
        u'Communication Preference': u'{}'.format(communication_preference)
        })

        # This is how I will send the New Member a verification email
        user = auth.create_user(
        email = '%s' %(email_address),
        email_verified = False,
        phone_number = '+1%s' %(primary_phone),
        password = 'password11',
        display_name = '%s' %(name),
        disabled = False)

        print('Sucessfully created new user: {0}'.format(user.uid)))

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



    def updateUser(member_ID):
        # This is how I will update the user#
        cred = credentials.Certificate('/Users/simonehill/Desktop/PYTHON FILES/gymMembers/bobsrealKey.json')
        project_id = 'bobsburgers-5d057'
        firebase_admin.initialize_app(cred, {
          'projectId': project_id,
        })
        db = firestore.client()
        doc_ref = db.collection('members').document(member_ID)
        try:
            doc = doc_ref.get()
            userDict = eval('{}'.format(doc.to_dict()))
        except google.cloud.exceptions.NotFound:
            print(u'No such document!')

        theMember_ID = "1.) => Member ID# : %s" %(userDict.get('Member ID#'))
        name = "2.) => Name : %s" %(userDict.get('Name'))
        age = "3.) => Age : %s" %(userDict.get('Age'))
        sex = "4.) => Gender : %s" %(userDict.get('Sex'))
        birthday = "5.) => Birthday : %s" %(userDict.get('Birthday'))
        membership_plan = "6.) => Membership Plan : %s" %(userDict.get('Membership Plan'))
        address = "7.) => Address : %s" %(userDict.get('Address'))
        interests = "8.) => Interests : %s" %(userDict.get('Interests'))
        nu_of_kids = "9.) => Nu of kids : %s" %(userDict.get('Nu of kids'))
        name_of_users_on_account = "10.) => Name of users on account : %s" %(userDict.get('Name of users on account'))
        key_card_holder = "11.) => Key card holder : %s" %(userDict.get('Key card holder'))
        additional_card_members = "12.) => Additional card members : %s" %(userDict.get('Additional card members'))
        email_address = "13.) => Email Address : %s" %(userDict.get('Email Address'))
        primary_phone = "14.) => Primary Phone : %s" %(userDict.get('Primary Phone'))
        secondary_phone = "15.) => Secondary Phone : %s" %(userDict.get('Secondary Phone'))
        user_login_type = "16.) => User Login Type : %s" %(userDict.get('User Login Type'))
        communication_preference = "17.) => Communication Preference : %s" %(userDict.get('Communication Preference'))
        print(theMember_ID)
        print(name)
        print(age)
        print(sex)
        print(birthday)
        print(membership_plan)
        print(address)
        print(interests)
        print(nu_of_kids)
        print(name_of_users_on_account)
        print(key_card_holder)
        print(additional_card_members)
        print(email_address)
        print(primary_phone)
        print(secondary_phone)
        print(user_login_type)
        print(communication_preference)


        updateInput = int(input("Please enter the number assigned to attribute: "))

        if updateInput == 1:
            attribute = 'Member ID#'
        if updateInput == 2:
            attribute = 'Name'
        if updateInput == 3:
            attribute = 'Age'
        if updateInput == 4:
            attribute = 'Sex'
        if updateInput == 5:
            attribute = 'Birthday'
        if updateInput == 6:
            attribute = 'Membership Plan'
        if updateInput == 7:
            attribute = 'Address'
        if updateInput == 8:
            attribute = 'Interests'
        if updateInput == 9:
            attribute = 'Nu of kids'
        if updateInput == 10:
            attribute = 'Name of users on account'
        if updateInput == 11:
            attribute = 'Key card holder'
        if updateInput == 12:
            attribute = 'Additional card members'
        if updateInput == 13:
            attribute = 'Email Address'
        if updateInput == 14:
            attribute = 'Primary Phone'
        if updateInput == 15:
            attribute = 'Primary Phone'
        if updateInput == 16:
            attribute = 'User Login Type'
        if updateInput == 17:
            attribute = 'Communication Preference'

        attributeInput = input('Please input the attribute info: ')
        doc_ref.update({
        u'%s' %(attribute): '%s' %(attributeInput),
        })

        docs = doc_ref.get()
        usersDict = eval('{}'.format(docs.to_dict()))
        
        theUpdateAttribute = usersDict.get(attribute)
        print('This is the updated user info : %s' %(theUpdateAttribute))

