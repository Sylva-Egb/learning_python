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
def insertElement(theIndex, theElement):
    myList.insert(theIndex,theElement)

while True:
    menu()
    choice = int(input('Enter your choice over there : '))
    if choice == 1:
        if myList ==[]:
            print('Empty List.\n')
            input('touch any key to return to the menu')
        else:
            for element in myList:
                print(f'{element}\n')
            input('touch any key to return to the menu')

    if choice == 2:
        newElement = input('Enter the element to add : ')
        myList.append(newElement)
        print('Well Done\n')
        input('touch any key to return to the menu')

    if choice == 3:
        newElement = input('Enter the element to add : ')
        indexOfElement = int(input('At which position you want to push it : '))
        insertElement(indexOfElement,newElement)
        print('Well done')
        input('touch any key to return to the menu')
    
    if choice == 4:
        if myList != []:
            print(f'You want to delete {myList[myList.len - 1]}. Are you really sure?')
            while True:
                agreement = input('y for yes and n for no')
                if agreement== 'y':
                    myList.pop()
                    break
                elif agreement == 'n':
                    print('The element will not be removed')
                    break
        input('touch any key to return to the menu')

    if choice == 7:
        break
