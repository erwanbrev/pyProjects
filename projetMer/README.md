### "projetMer" est un projet, en français, permettant d'obtenir des informations sous-marines en fonction de la profondeur souhaitée.
 Les codes ont été créés par Jordan et moi dans le cadre d'un projet de groupe, contenant les membres suivants :
 * @Jordan0602
 * @Antoine-M-9
 * @Bubamara0
 * @corsairecypri

### "projetMer" est un dossier contenant trois programmes en langage Python :
* **abysse_v4** : C'est un fichier qui est lié à une base de données SQLite du nom de BDDabysses créée par un collègue, **Jordan Shijo Lefrançois** aka **@jordan0602**.
  
  * C’est un programme qui permet de créer une base de données à partir de rien, les informations entrées sont des valeurs utiles au programme telles que la profondeur, comment s’appelle la zone à cette profondeur, les espèces que nous pourrions y trouver ainsi que certaines spécificités liées à cette zone. Ses données pourront donc être lues par le programme final afin de renseigner au mieux l’utilisateur.

* **merSQL** : C'est un fichier, finalisé avec l'aide du même collègue, qui utilise les données de BDDabysses.
  
  * Premièrement, le programme a pour but de calculer la pression théorique sous le niveau de la mer, selon la profondeur donnée et ensuite la pression réelle définie par l'addition de la pression atmosphérique et la pression calculée. 
Deuxièmement, des conditions viennent comparer la profondeur saisie et en fonction, affiche les données sous-marines en allant les chercher dans une base de données.
* **merSimuSQL** : C'est un fichier Python qui simule les données qu'une base de données pourrait fournir.

  * Premièrement, le programme a pour but de calculer la pression théorique sous le niveau de la mer, selon la profondeur donnée et ensuite la pression réelle définie par l'addition de la pression atmosphérique et la pression calculée. 
Deuxièmement, des conditions viennent comparer la profondeur saisie et en fonction, affiche les données sous-marines.
