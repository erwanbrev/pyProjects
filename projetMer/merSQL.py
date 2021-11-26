import sqlite3
pATM = 1.013  # pression atmosphérique en bar
# saisie d'une question
# rajout du \n voulu pour un choix decoratif
profondeur = int(input("Saisie de la profondeur en mètres souhaitée :\n"))
# pression en bar avec la profondeur souhaitée
pBar = profondeur / 10
# pression totale exercée par l'eau à la profondeur souhaitée
pTOT = pATM + pBar


# definition du chemin vers la base de donnée
dbfile = 'BDDabysses.db'
# creer une connexion SQL vers notre BDD SQLite
con = sqlite3.connect(dbfile)
# creer un curseur
cur = con.cursor()

# 5 morceaux de code SI la boucle ne fonctionne pas
# partie profondeur 0 à 200
table_zone0 = [a for a in cur.execute(
    "SELECT zone FROM ABYSSE WHERE id=1;")]
res0 = table_zone0
table_spe0 = [b for b in cur.execute(
    "SELECT spe FROM ABYSSE WHERE id=1;")]
res1 = table_spe0
table_espece0 = [c for c in cur.execute(
    "SELECT espece FROM ABYSSE WHERE id=1;")]
res2 = table_espece0

# partie profondeur 200 à 700
table_zone1 = [a for a in cur.execute(
    "SELECT zone FROM ABYSSE WHERE id=2;")]
res3 = table_zone1
table_spe1 = [b for b in cur.execute(
    "SELECT spe FROM ABYSSE WHERE id=2;")]
res4 = table_spe1
table_espece1 = [c for c in cur.execute(
    "SELECT espece FROM ABYSSE WHERE id=2;")]
res5 = table_espece1

# partie profondeur 700 à 2000
table_zone2 = [a for a in cur.execute(
    "SELECT zone FROM ABYSSE WHERE id=3;")]
res6 = table_zone2
table_spe2 = [b for b in cur.execute(
    "SELECT spe FROM ABYSSE WHERE id=3;")]
res7 = table_spe2
table_espece2 = [c for c in cur.execute(
    "SELECT espece FROM ABYSSE WHERE id=3;")]
res8 = table_espece2

# partie profondeur 2000 à 4000
table_zone3 = [a for a in cur.execute(
    "SELECT zone FROM ABYSSE WHERE id=4;")]
res9 = table_zone3
table_spe3 = [b for b in cur.execute(
    "SELECT spe FROM ABYSSE WHERE id=4;")]
res10 = table_spe3
table_espece3 = [c for c in cur.execute(
    "SELECT espece FROM ABYSSE WHERE id=4;")]
res11 = table_espece3

# partie profondeur 4000 à 6000
table_zone4 = [a for a in cur.execute(
    "SELECT zone FROM ABYSSE WHERE id=5;")]
res12 = table_zone4
table_spe4 = [b for b in cur.execute(
    "SELECT spe FROM ABYSSE WHERE id=5;")]
res13 = table_spe4
table_espece4 = [c for c in cur.execute(
    "SELECT espece FROM ABYSSE WHERE id=5;")]
res14 = table_espece4

# reduction du nombre de chiffres apres la virgule, à 3
print(f"\nLa pression totale exercée par l'eau à la profondeur souhaitée est de {pTOT:.3f} bar.")
if (profondeur >= 0 and profondeur < 200):
    # zone Épipélagique
    # rajout du \n dans le code pour un choix decoratif
    for row in res0:
        print(f"Vous êtes en zone ", row[0], ".\n")
    for row in res1:
        print(f"- Quelques spécifications :\n  - ", row[0], ".")
    for row in res2:
        print(f"- Les animaux marins les plus courants sont :\n  - ", row[0], ".\n")
elif (profondeur >= 200 and profondeur < 700):
    # zone Mésopélagique
    # rajout du \n dans le code pour un choix decoratif
    for row in res3:
        print(f"Vous êtes en zone ", row[0], "\n")
    for row in res4:
        print(f"- Quelques spécifications :\n  - ", row[0])
    for row in res5:
        print(f"- Les animaux marins les plus courants sont :\n  - ", row[0], ".\n")
elif (profondeur >= 700 and profondeur < 2000):
    # zone Bathypélagique
    for row in res6:
        print(f"Vous êtes en zone", row[0], ".\n")
    for row in res7:
        print(f"- Quelques spécifications :\n  - ", row[0])
    for row in res8:
        print(f"- Les animaux marins les plus courants sont :\n  - ", row[0], ".\n")
elif (profondeur >= 2000 and profondeur < 6000):
    # zone Abyssopélagique
    for row in res9:
        print(f"Vous êtes en zone ", row[0], ".\n")
    for row in res10:
        print(f"- Quelques spécifications :\n  - ", row[0])
    for row in res11:
        print(f"- Les animaux marins les plus courants sont :\n  - ", row[0], ".\n")
elif (profondeur >= 6000 and profondeur <= 10000):
    # zone Hadopélagique
    for row in res12:
        print(f"Vous êtes en zone ", row[0], ".\n")
    for row in res13:
        print(f"- Quelques spécifications :\n  - ", row[0])
    for row in res14:
        print(f"- Les animaux marins les plus courants sont :\n  - ", row[0], ".\n")
elif (profondeur > 10000 and profondeur <= 11000):
    print("La zone concernée est la fosse des Mariannes, puisque c'est la seule connue qui est aussi profonde.\n")
    print("- Les animaux marins les plus courants sont du même type que ceux de la zone précédente ( Hadopélagique ) : ")
    for row in res14:
        print(f"- C'est à dire :\n  - ", row[0], ".\n")
# si la profondeur saisie ne correspond à aucune valeur déclarée précédemment alors afficher
else:
    print("Aucune telle profondeur n'est encore connue de l'humain.\n")


# Être sûr de bien fermer la connexion
con.close()
