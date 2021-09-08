# python_ds_esiee
Repos des cours de python pour la datascience de E4 esiee paris


###########################

Info pertinante :
En pyhton les informations integré dans les 'docstrings' permettent après execution de 'help(fonction)' d'afficher les informations 
renseigné dans celui ci.
Pour afficher les message contenue dans les doctest il faut 'python -m code.py -v' si le '-v' n'est pas afficher alors rien ne s'affichera.

Lorsque l'on declare une liste 'l1' et qu'on l'assigne à une ligne 'l2' tel que 'l2 = l1' alors elle pointe sur la même zone en mémoire.
ainsi si une modification a lieu sur une liste elle a aussi lieu sur l'autre.
Il faut ajouter '[:]' pour copier la liste et pas ca reference, ou peut aussi utiliser la fonction 'deepcopy()' lorsque la liste a une
structure complexe.

Il vaut mieux utiliser les tuples que des list pour stoquer des structures complexes. Ils sont parfaitement adaptè pour créer des 
structures de données complexe.

Les dictionnaires sont sontconstitué d'une clée et d'une valeur => 'clée:valeur'

