#import the os library
import os

#define the variables
contacts = []
path_to_file = "contacts.csv"
to_continue = True

#function to clean up the cmd 
def cls():
    #to detect the system
    if os.name == 'nt':
        _ = os.system('cls') #This for windows
    else : 
        _ = os.system('clear') #This for Linux & MacOS

#function to fill the contacts list
def add_contact(name, email, phone):
    contacts.append({"name": name, "email": email, "phone": phone})

#function to show the file contents
def show_file_contents():
    with open(path_to_file, "r") as file:
        print(file.read())

#where the main function starts
print('Hello! Here\'s my toy project dealing with creating a contact list.')
print(" I invite your to enjoy yourself while using it.\n Let's start!")
print("PS: Make a feedback if you think there's any problem with my code or if you think the code can be written better.")
print("Personnal information : ")
print("LinkedIn : https://www.linkedin.com/in/sylvanus-egbewole-680941231/")
print("Email : romaricegbewole@gmail.com")
input("Press any key to continue")
while to_continue:
    name = input('Enter the contact name : ')
    email = input('Enter the contact email : ')
    phone = input('Enter the contact phone : ')
    add_contact(name, email, phone)
    confirmation = input("You want to add another contact? Tap y for yes and n for no")
    if confirmation == 'y' or confirmation == 'yes':
        to_continue = True
        cls()
    else:
        to_continue = False

#the registration in the file
if not os.path.exists(path_to_file):
    with open(path_to_file, "w") as file:
        file.write("Name,Email,Phone\n")
else:
    with open(path_to_file,"a") as file:
        if file.tell() == 0:
            file.write("Name,Email,Phone\n")
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']}\n")

showContact = input("Do you want to see your contacts? Tap y for yes and n for no")
if showContact == 'y' or showContact == 'yes':
    show_file_contents()

#the end
print("Thank you for using my program. Have a nice day!")