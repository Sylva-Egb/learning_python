def menu():
    print('Hello! Welcome to my program about working on list in Python\nWhat you wanna do?')
    print('1- Show the list items')
    print('2- Add an element (to the end) of the list')
    print('3- Insert an element at a position in the list')
    print('4- Delete the last element of the list')
    print('5- Reverse the list')
    print('6- Clear the list')
    print('7- Quit')

myList = []
def insertElement(theList : list, theIndex : int, theElement):
    theList.insert(theIndex,theElement)

while True:
    menu()
    choice = int(input('Enter your choice over there : '))
    if choice == 1:
        if not myList:
            print('Empty List.\n')
            input('touch any key to return to the menu')
        else:
            for element in myList:
                print(f'*{element}\n')
            input('touch any key to return to the menu')

    elif choice == 2:
        if not myList:
            newElement = input('Enter the first element to add : ')
            myList.append(newElement)
            print('Well Done\n')
            input('touch any key to return to the menu')
        else:
            newElement = input('Enter the element to add : ')
            myList.append(newElement)
            print('Well Done\n')
            input('touch any key to return to the menu')

    elif choice == 3:
        if not myList:
            print('This list is empty. We gonna push your element to the first position')
            newElement = input('Enter the first element to add : ')
            myList.append(newElement)
            print('Well Done\n')
            input('touch any key to return to the menu')
        else:
            newElement = input('Enter the element to add : ')
            indexOfElement = int(input('At which position you want to push it : '))
            insertElement(myList,indexOfElement,newElement)
            print('Well done')
            input('touch any key to return to the menu')
        
    elif choice == 4:
        if myList:
            print(f'You want to delete. Are you really sure?')
            while True:
                agreement = input('y for yes and n for no : ')
                if agreement== 'y' or agreement =='yes':
                    myList.pop()
                    print('Successfully removed')
                    break
                elif agreement == 'n' or agreement == 'no':
                    print('The element will not be removed')
                    break
        else:
            print('Your list is empty. Nothing to remove') 
        input('touch any key to return to the menu')
    elif choice == 5:
        if myList != []:
            myList.reverse()
            print('Now the order of your list has changed') 

    elif choice == 6:
        if myList: 
            myList.clear()
            print('Successfully clean up')
        input('touch any key to return to the menu')

    elif choice == 7:
        break
    else:
        print('Your choice should be between 1 and 7')