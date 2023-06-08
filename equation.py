import math

print('----------------------------BIENVENU(E) DANS LE PROGRAMME DE CALCUL D\'EQUATION AU SECOND DEGRE!--------------------------')
print('Petite explication : \nUne équation de second degré est sous la forme de Ax²+Bx +C (x étant une variable aléatoire)`\n')
print("La règle est tout bonnement simple:\n- A ne doit pas être égale à 0\n- B et C peuvent être égale à 0")
print("Bien commençons par s'amuser.\n")

while True:
    A = int(input('Entrez A : '))
    if A > 0:
        break
#print(f'Vous avez entré pour A la valeur: {A}')
B = int(input('Entrez B : '))
C = int(input('Entrez C : '))

delta = (B * B) - (4 * A * C)

#print(f'delta a pour valeur: {delta}')

if(delta < 0):
    print("L'équation n'admet pas de solution dans R")
elif delta == 0:
    print(f"L'équation admet une solution double qui est : x0={-B / (2 * A)} ")
else:
    print(f"{A}x²+{B}x+{C} admet deux solutions distinctes dans R\n")
    print(f"x1={(-B - math.sqrt(delta)) / (2 * A)} et x2={(-B + math.sqrt(delta)) / (2 * A)}\n")

input('ENTREZ UNE TOUCHE POUR ARRETER LE PROGRAMME ')
