# Exercice 3 : écrire un programme qui
# affiche le plus grand de trois entiers saisis.
number1 = int(input("Saisie du 1er nombre : "))
number2 = int(input("Saisie du 2eme nombre : "))
number3 = int(input("Saisie du 2eme nombre : "))
if (number1 > number2):
    MAX = number1
elif (number2 > number3):
    MAX = number2
else:
    MAX = number3
print(f"Le nombre le plus grand est : {MAX}")

# --------------------------------------------------------

# Exercice 2 : écrire un programme qui échange
# deux entiers saisis.
# afficher les entiers avant et après l'échange.
a = int(input("Saisie 1 :"))  # on saisie le premier entier
b = int(input("Saisie 2 :"))  # on saisie le deuxieme entier
print(f"a vaut {a} and b vaut {b}")
tmp = a
a = b
b = tmp
print(f"maintenant a vaut {a} et b vaut {b}")

/*--------------------------------------------------------*/

# Exercice 1 : écrire un programme qui saisit deux entiers
# et affiche leur produit.

a = int(input("Saisie 1 : "))
b = int(input("Saisie 2 : "))
res = a * b
print(f"Produit : {res}")