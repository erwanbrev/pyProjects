pATM = 1.013  # pression atmosphérique en bar
# saisie d'une question
# rajout du \n voulu pour un choix decoratif
profondeur = int(input("Saisie de la profondeur en mètres souhaitée :\n"))
# pression en bar avec la profondeur souhaitée
pBar = profondeur / 10
# pression totale exercée par l'eau à la profondeur souhaitée
pTOT = pATM + pBar

# reduction du nombre de chiffres apres la virgule, à 3
# resultat de la pression totale en mer en bar
print(f"\nLa pression totale exercée par l'eau à la profondeur souhaitée est de {pTOT:.3f} bar.")
# si la profondeur saisie est entre 0 et 200 mètres alors afficher infos
if (profondeur >= 0 and profondeur < 200):
    # rajout du \n dans le code pour un choix decoratif
    print("Vous êtes en zone Épipélagique nommée aussi Euphotique.")
    print("\n- La lumière qui y pénètre rend l’activité de photosynthèse possible.")
    print("- Les animaux marins présents sont :\n  - les poissons communs et habituels.\n")
elif (profondeur >= 200 and profondeur < 700):
    print("Vous êtes en zone Mésopélagique.")
    print("\n- Seule la longueur d'onde bleue de la lumière arrive à pénétrer ces profondeurs, ce qui est insuffisant pour la photosynthèse.")
    print("- Les animaux marins présents sont :\n  - Haches d'argents\n  - Gonostomatidés\n  - Poissons Lanternes\n")
    # rajout du \n dans le code pour un choix decoratif
# si la profondeur saisie est entre 700 et 2000 mètres alors afficher infos
elif (profondeur >= 700 and profondeur < 2000):
    print("Vous êtes en zone Bathypélagique nommée aussi Bathyale.")
    print("\n- Le milieu bathypélagique abrite de nombreux organismes qui ne dépendent plus forcément de la lumière notamment les organismes bioluminescents.\nL'océan est presque entièrement sombre, il n'y a pas de plantes vivantes et la plupart des animaux survivent en consommant la neige marine des détritus tombant des zones au-dessus, ou par la chasse d'autres organismes.")
    print("- Les animaux marins présents sont :\n  - Poissons-Football\n  - Cétomimidés\n  - Alépocéphalidés\n  - Grand-Gousiers\n")
elif (profondeur >= 2000 and profondeur < 6000):
    print("Vous êtes en zone Abyssopélagique nommée aussi Abyssale")
    print("\n- Aucune lumière n'est en capacité de pénétrer à cette profondeur. La plupart des êtres vivants sont aveugles et albinos.")
    print("- Les animaux marins présents sont :\n  - Donzelles\n  - Grenadiers\n")
elif (profondeur >= 6000 and profondeur <= 10000):
    print("Vous êtes en zone Hadopélagique nommée aussi Hadale")
    print("\n- Cette zone est en très grande partie inconnue et très peu d'espèces y ont été répertoriées.")
    print("- Les animaux marins présents sont :\n  - Donzelles\n  - Grenadiers\n")
elif (profondeur > 10000 and profondeur <= 11000):
    print("La zone concernée est la profondeur de la fosse des Mariannes, puisque c'est la seule connue qui l'est autant.\n")
# si la profondeur saisie ne correspond à aucune valeur déclarée précédemment alors afficher
else:
    print("Cette profondeur n'a pas encore été ni atteinte ni explorée.\n")
