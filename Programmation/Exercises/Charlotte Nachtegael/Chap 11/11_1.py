def wc(NomdeFichier):
    fd = open(NomdeFichier, 'r')
    fichier = fd.readlines()
    fd.close()

    #nombre de lignes
    nb_line = len(fichier)

    #nombre de caractères
    nb_cara = 0
    for i in range(nb_line):
        nb_cara += len(fichier[i])

    #nombre de mots
    nb_mot = 0
    for line in fichier:
        mot = ""
        for letter in line:
            if letter.isalnum():
                mot += letter
            elif len(mot) != 0 and not letter.isalnum():
                nb_mot += 1
                mot = ""
            else:
                mot = ""

    return nb_cara, nb_mot, nb_line