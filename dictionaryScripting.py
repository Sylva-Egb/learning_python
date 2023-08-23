import os

def cls():
    #to detect the system
    if os.name == 'nt':
        _ = os.system('cls') #This for windows
    else : 
        _ = os.system('clear') #This for Linux & MacOS

def menu():
    print(f"Hello! Here's the program dealing with my work on dictionary. It will consist to register yourself and manage with the informations you provide us.")
    print("Here's a little menu that we wrote to help you visit all the side of our script.")
    print("MENU : ")
    print("1- Provide some informations about yourself (eg name, age, sexe)\nIMPORTANT: If you're just starting the program we advice you to start by this")
    print("2- Show a summary of the information that you provide us")
    print("3- Show properly the information that you give us")
    print("4- Get the value of a specified information that you give us")
    print("5-")
    print("-")

personal_info = {}

while True:
    menu()

    choice = int(input("Enter your choice here : "))

    if choice == 1:
        while True:
            key = input("What information you want to provide? Just type the type (eg name)")
            print(f'Enter your {key} here : ')
            value = input()
            personal_info[key] = value
            confirmation = input("You want to provide another information? Tap y for yes and n for no")
            if confirmation == 'y' or confirmation == 'yes':
                break
        cls()
    
    if choice == 2:
        print(f"You  just provide your")
        for key in personal_info:
            print("- "+ key)
        print('Tap any key to continue')
        input()
        cls()
    
    if choice == 3:
        print("Your informations that we know are:")
        for key, value in personal_info.items():
            print(f"- {key} : {value}")
        print("Tap any key to continue")
        input()
        cls()