CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

approved_apps = [
    "Coding App"
    "Math App"
    "Reading App"
    "Science App"
]
student_name = input("Please Enter Your Name:")
requested_app = input ("Please Enter The App You Want To Access:").lower()

print("/n--- Identity Operator Check ---")
if type (student_name) is str:
    print("The Student Name Is Stored As Text")

if type (requested_app) is not int:
    print("The Requested App Is Not Stored As A Number.")

print("/n--- Membership Operator Check ---")

if requested_app in approved_apps:
    print("requested_app is an approved student app ")
else:
        print ("requested_app is not an approved student app")

resticted_apps= [
     "Gaming App"
     "Shopping App"
    "Social Media App"
]

if requested_app not in restricted_apps:
     print("The App Is Not In The Restricted List")
else:
    print("Acess Denied Beacause App Is Restricted")

print("/n--- App Permission Settings ---")

student_permissions= CAMERA 