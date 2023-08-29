import os
books = []

class Book:

    def __init__(self,_title,_description,_author,_year):
        self._title = _title
        self._description = _description
        self._author = _author
        self._year = _year
        self._available = 'y'
    
    def set_title(self,_title):
        self._title = _title
    def get_title(self):
        return self._title

    def set_description(self,_description):
        self._description = _description    

    def set_author(self,_author):
        self._author = _author

    def set_year(self,_year):
        self._year = _year
    
    def set_available(self, _available):
        self._available = _available

def cls():
    #to detect the system
    if os.name == 'nt':
        _ = os.system('cls') #This for windows
    else : 
        _ = os.system('clear') #This for Linux & MacOS

def menu():
    print('Welcome to our library. Here\'s all the things you can do.')
    print("1- Get the books list")
    print("2- Add a book to the list")
    print("3- Get the details of a book")
    print('4- Borrow a book')
    print("5- delete a book")

i = 0

def showAllBooks():
    i = 1
    for book in books:
        print(f"{i}- {book._title}")
        i+=1

def addBook():
    global i
    i = i + 1
    print('To achieve your goal you should enter the book\'s details')
    newTitle = input("What's the book's title ? : ")
    newDescription = input("Give the book description : ")
    newAuthor = input("Who wrote it ? : ")
    newYear = input("Enter The edition year : ")
    newBook = Book(newTitle, newDescription, newAuthor, newYear)
    books.append(newBook)
    print('Successfully added ;)')

book1 = Book('Pourquoi le bouc sent mauvais', 'Une histoire d\'afrique', 'inconnu',2012)
books.append(book1)

while True:
    menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        if not books:
            print('You are broke haha empty library!')
        else:
            showAllBooks()
    if choice == 2:
        addBook()
        input("Tap any key to continue")
        cls()
        
    if choice == 3:
        print('Select in this list the book you want details')
        showAllBooks()
        choice = int(input())
        print(f"{books[choice-1]._title} is a book written by {books[choice-1]._author} in {books[choice-1]._year}.")
        print(f"Summary:\n{books[choice-1]._description}")
        if books[choice-1]._available == 'y':
            print("It's actually avalable in our library")
        else:
            print("Not actually available in our library")
        input("Tap any key to continue")
        cls()
    
    if choice == 4:
        borrowable_books = []
        i = 0
        print('List of the available books')
        for book in books:
            if book._available == 'y':
                print(f"{i+1}- {book._title}")
                borrowable_books.append(book)
                i+=1
        choice = int(input("Enter the number of the book you want to borrow : "))
        borrowable_books[choice-1]._available = 'n'
        print(f'{borrowable_books[choice-1]._title} had been borrowed successfully')
        input("Tap any key to continue")
        cls()

    if choice == 5:
        showAllBooks()
        choice = int(input())
        del books[choice-1]
        print('successfully deleted. \n\nHere is the new list ;)')
        showAllBooks()
        input("Tap any key to continue")
        cls()
    