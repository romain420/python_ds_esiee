# Vos import ici

def read_file(filename)
    
    filename  nom du fichier csv

    Retourne une liste de dictionnaires dont les clÃ©s sont dÃ©finies par
    la 1ere ligne du fichier
     data = read_file(communes.csv)
     type(data)
    class 'list'
     len(data)
    36683
     type(data[0])
    class 'collections.OrderedDict'
     len(data[0])
    10
     data[0][Nom de la rÃ©gion]
    'RhÃ´ne-Alpes'
     data[0][Code dÃ©partement]
    '01'
     data[0][Code canton]
    '08'
     data[0][Nom de la commune]
    L' Abergement-ClÃ©menciat
     data[0][Population totale]
    '780'
     data[34878][Nom de la rÃ©gion]
    'Limousin'
     data[34878][Code dÃ©partement]
    '87'
     data[34878][Code canton]
    '99'
     data[34878][Nom de la commune]
    'Limoges'
     data[34878][Population totale]
    '137 473'
    
    # votre code ici
    
    return []

def build_set_departements(data)
    
    data  la liste de dictionnaires retournÃ©e par read_file()

    Retourne l'ensemble des dÃ©partements (set)
    
     data = read_file(communes.csv)
     sd = build_set_departements(data)
     type(sd)
    class 'set'
     len(sd)
    100
     '15' in sd
    True
     15 in sd
    False
     'Cantal' in sd
    False
     '2A' in sd
    True
     '2B' in sd
    True
     'Corse' in sd
    False
     '20' in sd
    False
    
    # votre code ici
    
    return set()
    
def build_list_communes(data)
    
    data  la liste de dictionnaires retournÃ©e par read_file()

    Retourne la liste des tuples (commune, dÃ©partement, population)
    
     data = read_file(communes.csv)
     lc = build_list_communes(data)
     type(lc)
    class 'list'
     len(lc)
    36683
     type(lc[999])
    class 'tuple'
     len(lc[999])
    3
     lc[999]
    ('Pargny-les-Bois', '02', 131)
     type(lc[999][0])
    class 'str'
     type(lc[999][1])
    class 'str'
     type(lc[999][2])
    class 'int'
     lc[100102]
    [('Cize', '01', 181), ('Cleyzieu', '01', 140)]
     lc[34878]
    ('Limoges', '87', 137473)
    
    # votre code ici
    
    return []

def build_dict_departements(lc, sd)
    
    lc  la liste des communes retournÃ©e par build_list_communes()
    sd  l'ensemble des dÃ©partements retournÃ© par build_set_departements()

    Retourne un dictionnaire dont la clÃ© est le dÃ©partement, et la valeur une liste [nombre de communes, population totale]
    
     data = read_file(communes.csv)
     sd = build_set_departements(data)
     lc = build_list_communes(data)
     dd = build_dict_departements(lc, sd)
     type(dd)
    class 'dict'
     len(dd)
    100
     dd['18']
    [290, 319693]
     dd['21']
    [706, 543648]
     dd['27']
    [675, 612518]
     dd['53']
    [261, 318095]
    
    # votre code ici
    
    return dict()
    
def stat_by_dpt(dd, dpt)
    
    dd  le dictionnaire retournÃ© par build_dict_departements()
    dpt  le dÃ©partement concernÃ© (str)

    Retourne une liste [nombre de communes, population totale]
     data = read_file(communes.csv)
     sd = build_set_departements(data)
     lc = build_list_communes(data)
     dd = build_dict_departements(lc, sd)
     sbd = stat_by_dpt(dd, '87')
     type(sbd)
    class 'list'
     len(sbd)
    2
     sbd[1]
    384411
     sbd[0]
    201
     sbd = stat_by_dpt(dd, '77')
     sbd[1]
    1387830
     sbd[0]
    513
     sbd = stat_by_dpt(dd, 'Corse')
     sbd is None
    True
    
    # votre code ici
    
    return []

def main()
    # votre code de test ici
    # le code ci dessous est exÃ©cutÃ© avec la commande 
    #   python communes.py
    
    pass
    
# Ne pas modifier le code ci-dessous
if __name__ == '__main__'
    main()