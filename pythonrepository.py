students={
    "SANTOSH":785994848,"TAMMANAH YADAV":657858494,"MUHAMAD RISHAN":675586969,"AYUSH KUMAR JHA":657588969,"SAHIL GAUTAM":6575758585,
    "BASHALA RAHUL PRASANTH":755859590,"MANOJ":7586969070,"DEEPANSHU":755869696,"PRIYANSHU":647484949,"ADITYA":758589960,"SURANDRA":65755885,
    "RAVISHANKAR":768869699,"SOURAV":474895050,"VIKASH":75758960,"VINAY":748595500,"GAGANDEEP":75858599,"ABHIJEET":748595950,"AMIN":774748849,
    "ASHISH":747585959,"KRISHNA":747585599,"NITESH":675895950,"RUDRA":758595959,"SHUBHAM":647588559,"LOKESH":75899559,"SASHANK":7647484,
    "FAISAL":47884949,"AMSHU":7474848,"KARAN":6474848,"NITIKA":747484849,"ROHIT":474849994,"YASH":7474849,"VEENA":647484894,"SARVJEET":7588585,
    "LALIT":849440400,"ASHISH2":7474848848,"HIMANSHU":74858959,"PRAJWAL":7585895,"SAYAN MANDAL":758859595,"UBED ALI":74848499,"AVISHI":7485858,
    "ARJAV":748484,"KESHAV":648488
}

#search and print one contact

def single_student():
    name=input("Enter the name you want to search his/her contact:").upper()
    if name in students:
        print(f"{name}: {students[name]}")

    else:
        b=input("No this contact is not in our list \n if you want to add then,type 'yes' else type 'No'").lower()
        if b=="yes":
            new_contact(name)
            print(f"{name}: {students[name]}")

        else:
            pass

#search and print multiple contacts detail
def multiple_student():
    name=list(map(str,input("Enter the name you want to search his/her contact:").split()))

    for i in name:
        if i.upper() in students:
            print(f"{i.upper()}: {students[i.upper()]}")
        else:
            b=input("No this contact is not in our list \n if you want to add then,type 'yes' else type 'No'").lower()
            if b=="yes":
                new_contact(i)
                print(f"{i}: {students[i]}")

            else:
                pass

def new_contact(student_name):
    print()
    contact_number=int(input("Enter his/her contact number you want to add: "))
    students[student_name]=contact_number




choice=int(input(
    "you want to search:\n 1. searchfor a single contact \n 2.search for multiple contact \n 3.view all students contact\n select one option from these given options:"

))
if choice==1:
    single_student()
elif choice==2:
    multiple_student()
elif choice==3:
    print(students)
else:
    print("choose from given options:1,2,3")
