### "projetMer" est un dossier contenant trois programmes :
* **"abysse_v4"** : C'est un fichier Python qui est lié à une base de données SQLite du nom de "BDDabysses" créée par un collègue, **Jordan "Shijo" Lefrançois** aka **jordan0602**.
  * C’est un programme qui permet de créer une base de données à partir de rien, les informations entrées sont des valeurs utiles au programme telles que la profondeur, comment s’appelle la zone à cette profondeur, les espèces que nous pourrions y trouver ainsi que certaines spécificités liées à cette zone. Ses données pourront donc être lues par la programme final afin de renseigner au mieux l’utilisateur.

* **"merSQL"** : C'est un fichier Python, finalisé avec l'aide du même collègue, qui utilise les données d'une base de données créée par le fichier précédent.
  * Premièrement, le programme a pour but de calculer la pression théorique sous le niveau de la mer, selon la profondeur donnée et ensuite la pression réelle définie par l'addition de la pression atmosphérique et la pression calculée. 
Deuxièmement, des conditions viennent comparer la profondeur saisie et en fonction, affiche les données sous-marines en allant les chercher dans une base de données.
* **"merSimuSQL"** : C'est un fichier Python qui simule les données qu'une base de données fournirait.
  * Premièrement, le programme a pour but de calculer la pression théorique sous le niveau de la mer, selon la profondeur donnée et ensuite la pression réelle définie par l'addition de la pression atmosphérique et la pression calculée. 
Deuxièmement, des conditions viennent comparer la profondeur saisie et en fonction, affiche les données sous-marines.
