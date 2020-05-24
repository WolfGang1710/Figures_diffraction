"""
Title: Projet IPT - Diffraction DI
Description: Ce programme permet de mesurer et comparer le temps
             d'exécution d'une figure de diffraction entre la méthode
             par somme discrète et la fonction fft de Numpy en fonction
             de la taille de la matrice.
             Retourne des graphiques (enregistré dans le dossier indiqué).
"""

#pylint: disable=invalid-name

#=== Importation des modules ===

import time #Mesure du temps
import matplotlib.pyplot as plt #Graphiques
import numpy as np #Calcul mathématiques
import modules.fentes as fentes #Création fentes de diffraction
import modules.diffraction as diffraction #Réalisation figures de diffraction

def fente_carre(taille_matrice_max, cote_carre, chemin_dossier, nom_fichier, extension='.png', affichage=False):
    """
    Mesure le temps d'execution pour créer une figure de
    diffraction avec notre fonction \"diffraction\" et avec
    les fonctions de Numpy, en fonction de la taille de la matrice,
    avec la fente carrée et affiche le graphique correspondant.
    """

    Lt = [] #Liste des temps
    Lt_Numpy = [] #Liste des temps avec Numpy
    L_taille_matrice = [] #Liste taille matrice

    #On commence par 1 pour éviter division par 0 ds fonction diffraction
    for n in range(1, taille_matrice_max):
        L_taille_matrice.append(n) #Ajout de la taille de la matrice à la liste
        fente = fentes.carree(n, cote_carre) #Création de la fente
        debut = time.perf_counter() #Mesure du temps d'éxécution
        diffraction.diffraction(fente) #Création de la figure de diffraction
        Lt.append(time.perf_counter() - debut)

        debut = time.perf_counter() #Mesure du temps d'éxécution
        abs(np.fft.fftshift(np.fft.fft2(fente)))**2 #Création de la figure de diffraction avec Numpy
        Lt_Numpy.append(time.perf_counter() - debut)

    #Création de la figure
    fig = plt.figure("Comparaison des temps de calcul entre notre fonction et celle de Numpy pour n variant entre 0"+str(taille_matrice_max))
    #Division de l'image en 2 parties
    plt.subplot(211) #Le graphique occupe l'emplacement 1
    #Ajout d'un titre
    plt.title("Temps de calcul des figures de diffraction avec la fente carrée en fonction de la taille de la matrice")
    #Création de la courbe verte
    plt.plot(L_taille_matrice, Lt, '-g', label='Temps de calcul par somme discrète')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    plt.subplot(212) #Le graphique occupe l'emplacement 2
    #Création de la courbe rouge
    plt.plot(L_taille_matrice, Lt_Numpy, '-r', label=r'Temps de calcul avec Numpy')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    #Enregistrement de l'image
    fig.savefig(str(chemin_dossier)+"/"+str(nom_fichier)+str(extension), bbox_inches='tight')

    if affichage == True:
        plt.show() #Affichage des graphiques
    plt.clf() #Remise à zéro de la fenêtre

def fente_circulaire(taille_matrice_max, rayon_cercle, chemin_dossier, nom_fichier, extension='.png', affichage=False):
    """
    Mesure le temps d'execution pour créer une figure de
    diffraction avec notre fonction "diffraction" et avec
    les fonctions de Numpy, en fonction de la taille de la matrice,
    avec la fente carrée et affiche le graphique correspondant.
    """

    Lt = [] #Liste des temps
    Lt_Numpy = [] #Liste des temps avec Numpy
    L_taille_matrice = [] #Liste taille matrice

    for n in range(1, taille_matrice_max): #On commence par de 1 pour éviter la division par 0
        L_taille_matrice.append(n) #Ajout de la taille de la matrice à la liste
        fente = fentes.circulaire(n, rayon_cercle) #Création de la fente
        debut = time.perf_counter() #Mesure du temps d'éxécution
        diffraction.diffraction(fente) #Création de la figure de diffraction
        Lt.append(time.perf_counter() - debut)

        debut = time.perf_counter() #Mesure du temps d'éxécution
        abs(np.fft.fftshift(np.fft.fft2(fente)))**2 #Création de la figure de diffraction avec Numpy
        Lt_Numpy.append(time.perf_counter() - debut)

    #Création de la figure
    fig = plt.figure("Comparaison des temps de calcul entre notre fonction et celle de Numpy pour n variant entre 0"+str(taille_matrice_max))
    #Division de l'image en 2 parties
    plt.subplot(211) #Le graphique occupe l'emplacement 1
    #Ajout d'un titre
    plt.title("Temps de calcul des figures de diffraction avec la fente circulaire en fonction de la taille de la matrice")
    #Création de la courbe verte
    plt.plot(L_taille_matrice, Lt, '-g', label='Temps de calcul par somme discrète')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    plt.subplot(212) #Le graphique occupe l'emplacement 2
    #Création de la courbe rouge
    plt.plot(L_taille_matrice, Lt_Numpy, '-r', label=r'Temps de calcul avec Numpy')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    #Enregistrement de l'image
    fig.savefig(str(chemin_dossier)+"/"+str(nom_fichier)+str(extension), bbox_inches='tight')

    if affichage == True:
        plt.show() #Affichage des graphiques
    plt.clf() #Remise à zéro de la fenêtre

def fentes_rectangulaires(taille_matrice_max, longueur, largeur, ecart, chemin_dossier, nom_fichier, extension='.png', affichage=False):
    """
    Mesure le temps d'execution pour créer une figure de
    diffraction avec notre fonction "diffraction" et avec
    les fonctions de Numpy, en fonction de la taille de la matrice,
    avec la fente carrée et affiche le graphique correspondant.
    """

    Lt = [] #Liste des temps
    Lt_Numpy = [] #Liste des temps avec Numpy
    L_taille_matrice = [] #Liste taille matrice

    for n in range(1, taille_matrice_max): #On commence par de 1 pour éviter la division par 0
        L_taille_matrice.append(n) #Ajout de la taille de la matrice à la liste
        fente = fentes.rectangulaires(n, longueur, largeur, ecart) #Création de la fente
        debut = time.perf_counter() #Mesure du temps d'éxécution
        diffraction.diffraction(fente) #Création de la figure de diffraction
        Lt.append(time.perf_counter() - debut)

        debut = time.perf_counter() #Mesure du temps d'éxécution
        abs(np.fft.fftshift(np.fft.fft2(fente)))**2 #Création de la figure de diffraction avec Numpy
        Lt_Numpy.append(time.perf_counter() - debut)

    #Création de la figure
    fig = plt.figure("Comparaison des temps de calcul entre notre fonction et celle de Numpy pour n variant entre 0"+str(taille_matrice_max))
    #Division de l'image en 2 parties
    plt.subplot(211) #Le graphique occupe l'emplacement 1
    #Ajout d'un titre
    plt.title("Temps de calcul des figures de diffraction avec les fentes rectangulaire en fonction de la taille de la matrice")
    #Création de la courbe verte
    plt.plot(L_taille_matrice, Lt, '-g', label='Temps de calcul par somme discrète')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    plt.subplot(212) #Le graphique occupe l'emplacement 2
    #Création de la courbe rouge
    plt.plot(L_taille_matrice, Lt_Numpy, '-r', label=r'Temps de calcul avec Numpy')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    #Enregistrement de l'image
    fig.savefig(str(chemin_dossier)+"/"+str(nom_fichier)+str(extension), bbox_inches='tight')

    if affichage == True:
        plt.show() #Affichage des graphiques
    plt.clf() #Remise à zéro de la fenêtre

def fentes_carrees(taille_matrice_max, cote, ecart, chemin_dossier, nom_fichier, extension='.png', affichage=False):
    """
    Mesure le temps d'execution pour créer une figure de
    diffraction avec notre fonction "diffraction" et avec
    les fonctions de Numpy, en fonction de la taille de la matrice,
    avec la fente carrée et affiche le graphique correspondant.
    """

    Lt = [] #Liste des temps
    Lt_Numpy = [] #Liste des temps avec Numpy
    L_taille_matrice = [] #Liste taille matrice

    for n in range(1, taille_matrice_max): #On commence par de 1 pour éviter la division par 0
        L_taille_matrice.append(n) #Ajout de la taille de la matrice à la liste
        fente = fentes.quatre_carrees(n, cote, ecart) #Création de la fente
        debut = time.perf_counter() #Mesure du temps d'éxécution
        diffraction.diffraction(fente) #Création de la figure de diffraction
        Lt.append(time.perf_counter() - debut)

        debut = time.perf_counter() #Mesure du temps d'éxécution
        abs(np.fft.fftshift(np.fft.fft2(fente)))**2 #Création de la figure de diffraction avec Numpy
        Lt_Numpy.append(time.perf_counter() - debut)

    #Création de la figure
    fig = plt.figure("Comparaison des temps de calcul entre notre fonction et celle de Numpy pour n variant entre 0"+str(taille_matrice_max))
    #Division de l'image en 2 parties
    plt.subplot(211) #Le graphique occupe l'emplacement 1
    #Ajout d'un titre
    plt.title("Temps de calcul des figures de diffraction avec les 4 fentes carrées en fonction de la taille de la matrice")
    #Création de la courbe verte
    plt.plot(L_taille_matrice, Lt, '-g', label='Temps de calcul par somme discrète')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    plt.subplot(212) #Le graphique occupe l'emplacement 2
    #Création de la courbe rouge
    plt.plot(L_taille_matrice, Lt_Numpy, '-r', label=r'Temps de calcul avec Numpy')
    plt.legend(loc='best') #Emplacement de la légende
    plt.xlabel("Taille de la matrice") #Titre de l'axe des abscisses
    plt.ylabel("Temps (s)") #Titre de l'axe des ordonnées
    plt.grid() #Affichage de la grille

    #Enregistrement de l'image
    fig.savefig(str(chemin_dossier)+"/"+str(nom_fichier)+str(extension), bbox_inches='tight')

    if affichage == True:
        plt.show() #Affichage des graphiques
    plt.clf() #Remise à zéro de la fenêtre
