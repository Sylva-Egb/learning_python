age= int(input('Entrez votre age : '))

if(age<18):
   print (f'Vous avez {age} ans. VOUS ETES MINEUR(E)!')
elif(age>=18 and age<40):
    print(f'Vous avez {age} ans. Vous êtes majeur avec plein d\'avenir')
else:
    print(f'Vous avez {age} ans et vous etes moribond')
