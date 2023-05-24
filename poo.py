class Human:
    #the methods
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
        self.gender = ""
        self.profession = ""
    def showInfo(self):
        print('Your name\'s ' + self.firstname + " " + self.lastname + '. You\'re ' + str(self.age) + " years old.\n"
        + 'Great to see that you\'re ' + self.gender + ' person and you are register as: '+ self.profession )
    

person1 = Human()

person1.firstname = input('Enter you firstname please: ')
person1.lastname = input('\nEnter you lastname please: ')
person1.age = int(input('\nEnter you age please: '))

while True:
    person1.gender  = input('\nEnter your gender (M or F ): ')
    if person1.gender.lower() == 'm' or person1.gender.lower() == 'f':
        break

person1.profession = input('\nEnter your profession: ')

person1.showInfo()