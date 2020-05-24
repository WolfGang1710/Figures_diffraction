"""
Title: Projet IPT - Diffraction DI
Description: Ce programme permet de créer les figures de diffraction
             de la lumière et de les enregistrer.
"""

#pylint: disable=invalid-name

#===Importation des modules ===

import matplotlib.pyplot as plt

def save(image, nom_figure, cmap, chemin_dossier, nom_fichier, extension='.png', affichage=False):
    """
    Génère une figure contenant une image
    grâce au module matplotlib et la sauvegarde dans le dossier
    chemin_dossier avec le nom_fichier.extension (extension vaut
    par défaut .png)

    - image est une matrice. (list)
    - nom_figure est le nom qui sera affiché sur la fenêtre si
    affichage = True (str)
     -cmap est la colormap à utiliser pour les couleurs. (str)
    - nom_fichier (str)
    - extension (str)
    - affichage (bool)
    """

    #Création de la figure, la fenêtre a pour titre 'nom_figure'
    figure = plt.figure(str(nom_figure))
    #Paramétrage de l'image
    plt.imshow(image, cmap=str(cmap), interpolation='nearest')
    plt.axis('off') #Désactivation des axes
    #Enregistrement de l'image ; paramètres tight permet d'avoir
    #peu de contour blanc
    figure.savefig(str(chemin_dossier)+str(nom_fichier)+str(extension), bbox_inches='tight')

    #Affichage de la photo ou non
    if affichage == True:
        print("Affichage.")
        plt.show() #Affichage

    plt.clf() #Remise à zéro de la fenêtre

def s_save(L_image, cmap, chemin_dossier, L_nom_fichier, L_titre='', L_figure='', extension='.png', affichage=False):
    """
    Génère autant de figure qu'il y d'élément dans L_image
    grâce au module matplotlib et les sauvegarde dans le dossier
    chemin_dossier avec le nom_fichier.extension
    (extension vaut par défaut .png).

    - L_image est une liste de matrices d'image. (list)
    - cmap est la colormap à utiliser pour les couleurs. (str)
    - chemin_dossier (str).
    - L_nom_fichier est la liste contenant les différents noms utilisés
    pour enregistrer les photos générées
    - L_titres est optionnel, liste contenant le titre à afficher
    au-dessous de chaque image.
    - L_figure est optionnel, liste contenant les différents noms à
    afficher en titre de fenêtre si affichage = True
    - affichage, optionnel - booléan

    /! on considère que les liste sont correctement ordonnées :
        L_nom_fichier[i] est le nom de l'image L_image[i] etc.
    """

    #Si l'argument L_titre n'est pas donné, on le transforme en liste
    if L_titre == '':
        L_titre = []
        for _ in range(len(L_image)):
            L_titre.append('')

    #Si l'argument L_figure n'est pas donné, on le transforme en liste
    if L_figure == '':
        L_figure = []
        for _ in range(len(L_image)):
            L_figure.append('')

    index = 0

    for image in L_image: #On boucle sur toutes les images de la liste
        #On créé une fenêtre pour cjauqe image ayant pour titre
        #"L_figure[index]"
        figure = plt.figure(str(L_figure[index]))
        #Paramétrage de l'image
        plt.imshow(image, cmap=str(cmap), interpolation='nearest')
        plt.axis('off') #Désactivation des axes
        plt.title(str(L_titre[index])) #Titre de l'image "L_titre[index]"
        #Enregistrement de l'image ; paramètres tight permet d'avoir
        #peu de contour blanc
        figure.savefig(str(chemin_dossier)+"/"+str(L_nom_fichier[index])+str(extension), bbox_inches='tight')
        index += 1 #On passage à l'image suivante

    #Affichage ou non
    if affichage == True:
        print("Affichage.")
        plt.show() #Affichage

    plt.clf() #Remise à zéro de la fenêtre

def subplot_save(L_image, nb_ligne, nb_colonne, cmap, chemin_dossier, nom_fichier, nom_figure='', L_titre='', extension='.png', affichage=False):
    """
    Génère une image contenant tout les images de la liste L_image
    grâce au module matplotlib et les sauvegarde dans chemin_dossier
    avec le nom nom_fichier.extension (extension ='.png' par défaut)

    - L_image est une liste de matrices d'image. (list)
    - nb_ligne (int). On divise la fenêtre en nb_lignes lignes.
    - nb_colonne (int). On divise la fenêtre en nb_colonne colonne.
    - cmap est la colormap à utiliser pour les couleurs. (str)
    - chemin_dossier (str).
    - nom_fichier est le nom pour enregistrer les photos générées dans
    la même fenêtre.
    - nom_figure (str). Nom affiché sur la fenêtre.
    - L_titres est optionnel, liste contenant le titre à afficher
    au-dessous de chaque image.
    - L_figure est optionnel, liste contenant les différents noms à
    afficher en titre de fenêtre si affichage = True
    - affichage, optionnel - booléan

    /! on considère que les liste sont correctement ordonnées :
        L_nom_fichier[i] est le nom de l'image L_image[i] etc.
    """

    index = 1 #Position de l'image sur la figure (qui ne peut valoir 0)
    figure = plt.figure(str(nom_figure)) #Création de la figure

    #Si l'argument L_titre n'est pas donné, on le transforme en liste
    if L_titre == '':
        L_titre = []
        for _ in range(len(L_image)):
            L_titre.append('')

    #Chaque image dans L_image se voit attribuer une place sur la figure
    for image in L_image:
        #On défini cette place dans la fenêtre
        figure.add_subplot(int(str(nb_ligne)+str(nb_colonne)+str(index)))
        #Paramétrage de la figure
        plt.imshow(image, cmap=str(cmap), interpolation='nearest')
        plt.axis('off') #Désactivation des axes
        plt.title(str(L_titre[index-1])) #Titre image "L_titre[index-1]"
        index += 1 #On passe à la figure suivante

    #Enregistrement de l'image ; paramètres tight permet d'avoir
    #peu de contour blanc
    figure.savefig(str(chemin_dossier)+"/"+str(nom_fichier)+str(extension), bbox_inches='tight')

    if affichage == True:
        print("Affichage.")
        plt.show() #Affichage

    plt.clf() #Remise à zéro de la fenêtre
