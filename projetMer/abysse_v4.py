import sqlite3  # Importation de la bibliothèque sqlite3

# Permet d'ouvrir ou de créer la base de données "BDDabysses"
conn = sqlite3.connect('BDDabysses.db')
cur = conn.cursor()  # Nous créons un objet de type "connection" (conn) qui va nous permettre d'interagir avec la base de données
# Nous créons ensuite un objet de type "cursor" à partir de l'objet de type "connection". Cet objet de type "cursor" va nous permettre de manipuler la base de données et d'obtenir des résultats lorsque nous effectuerons des requêtes.
datas = [
    (0, 'Épipélagique', 'Poissons communs et habituels',
     'C est ce qu on appelle la haute mer, la lumière qui y pénètre rend l activité de photosynthèse possible'),
    (200, 'Mésopélagique', 'Haches d argents, Gonostomatidés, Poissons Lanternes',
     'Seule la longueur d onde bleue de la lumière arrive à pénétrer ces profondeurs, ce qui est insuffisant pour la photosynthèse'),
    (700, 'Bathypélagique', 'Poissons-Football, Cétomimidés, Alépocéphalidés, Grand-Gousiers',
     'Le milieu bathypélagique abrite de nombreux organismes qui ne dépendent plus forcément de la lumière notamment les organismes bioluminescents. L océan est presque entièrement sombre'),
    (2000, 'Abyssopélagique', 'Donzelles, Grenadiers',
     'Aucune lumière n est en capacité de pénétrer à cette profondeur. La plupart des êtres vivants sont aveugles et albinos parmis ceux qui n ont pas encore disparus'),
    (6000, 'Hadopélagique', 'Donzelles, Grenadiers',
     'Limités aux fosses océaniques on y trouve quelques poissons benthique. Cette zone est en très grande partie inconnue et très peu d espèces y ont été répertoriées'),

]  # On remplit la table avec les données dont nous avons besoin

# La méthode "execute" de notre objet de type "cursor" nous permet d'effectuer une requête SQL
cur.execute("CREATE TABLE IF NOT EXISTS ABYSSE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, profondeur INT, zone TXT, espece TXT, spe TXT)")
cur.executemany(
    "INSERT INTO ABYSSE(profondeur,zone,espece,spe) VALUES(?, ?, ?, ?)", datas)
# Pour véritablement exécuter les requêtes, il est nécessaire d'appliquer la méthode "commit" à l'objet de type "connection".
conn.commit()

# Permet de "fermer" l'objet de type "cursor" et l'objet de type "connection".
cur.close()
conn.close()
