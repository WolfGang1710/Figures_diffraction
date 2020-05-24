"""
Title: Projet IPT - Diffraction DI
Description: Ce programme permet de créer une série d'images
             de diffraction avec une fente voulue pour ensuite
             en faire un GIF.
"""

#=== Importation des modules ===

import matplotlib.pyplot as plt #Création d'image
import numpy as np #Création figure diffraction avec Transformée Fourrier
import modules.diffraction as diffraction #Diffraction par somme discrète
import modules.fentes as fentes #Création des fentes

def carree(taille_matrice, chemin_dossier, chemin_dossier_numpy):
    """
    Création de taille_matrice images et les sauvegarde dans
    chemin_dossier et chemin_dossier_numpy pour ensuite
    créer un GIF avec ces dernières.
    """

    fig = plt.figure() #Création de la figure

    for cote in range(taille_matrice): #Variation côté carré
        fente = fentes.carree(taille_matrice, cote) #Création fente
        #Création de la figure de diffraction par somme discrète
        diffrac = diffraction.diffraction(fente)
        #Idem avec Numpy
        diffrac_numpy = abs(np.fft.fftshift(np.fft.fft2(fente)))**2
        #Ajout texte sur image. Fond : Blanc, oppacité : 50%, police : noir/8
        plt.text(0, 2, "Côté du carré : "+str(cote), color='k', bbox=dict(facecolor='w', alpha=0.5), fontsize=8)

        #Configuation de l'image
        plt.imshow(diffrac, cmap='hot', interpolation='nearest')
        plt.axis('off') #Désactivation des axes
        #Enregistrement de l'image dans chemin_dossier, nom : photo_cote
        #cote est un numéro qui commece à 0 et fini à taille_matrice - 1
        #bbox_inches='tight' permet de réduit le contour blanc
        fig.savefig(str(chemin_dossier)+"/photo"+str(cote), bbox_inches='tight')

        plt.clf() #Remise à 0 de la fenêtre

        plt.imshow(diffrac_numpy, cmap='hot', interpolation='nearest')
        plt.axis('off')
        fig.savefig(str(chemin_dossier_numpy)+"/photo"+str(cote), bbox_inches='tight')
        plt.clf()

def circulaire(taille_matrice, chemin_dossier, chemin_dossier_numpy):
    """
    Création de taille_matrice images et les sauvegarde dans
    chemin_dossier et chemin_dossier_numpy pour ensuite
    créer un GIF avec ces dernières.
    """

    fig = plt.figure() #Création de la figure

    for rayon in range(taille_matrice): #Variaion rayon cercle
        fente = fentes.circulaire(taille_matrice, rayon) #Création fente
        #Création de la figure de diffraction par somme discrète
        diffrac = diffraction.diffraction(fente)
        #Création de la figure de diffraction avec Numpy
        diffrac_numpy = abs(np.fft.fftshift(np.fft.fft2(fente)))**2
        #Ajout texte sur image. Fond : Blanc, oppacité : 50%, police : noir/8
        plt.text(0, 2, "Rayon du cercle : "+str(rayon), color='k', bbox=dict(facecolor='w', alpha=0.5), fontsize=8)

        #Configuration de l'image
        plt.imshow(diffrac, cmap='hot', interpolation='nearest')
        plt.axis('off') #Désactivation des axes
        #Enregistrement de l'image dans chemin_dossier, nom : photo_cote
        #rayon est un numéro qui commece à 0 et fini à taille_matrice - 1
        #bbox_inches='tight' permet de réduire le contour blanc
        fig.savefig(str(chemin_dossier)+"/photo"+str(rayon), bbox_inches='tight')
        plt.clf() #Remise à zéro de la fenêtre

        plt.imshow(diffrac_numpy, cmap='hot', interpolation='nearest')
        plt.axis('off')
        fig.savefig(str(chemin_dossier_numpy)+"/photo"+str(rayon), bbox_inches='tight')
        plt.clf()

def rectangulaires(taille_matrice, chemin_dossier, chemin_dossier_numpy):
    """
    Création de taille_matrice^3 images et les sauvegarde dans
    chemin_dossier et chemin_dossier_numpy pour ensuite
    créer un GIF avec ces dernières.
    """

    index = 0 #Compteur
    fig = plt.figure() #Création de la figure

    for longueur in range(taille_matrice): #Variation longueur fente
        for largeur in range(taille_matrice): #Varaition largeur fente
            for ecart in range(taille_matrice): #Variation ecart entre fentes
                fente = fentes.rectangulaires(taille_matrice, longueur, largeur, ecart) #Création fente
                #Création de la figure de diffraction par somme discrète
                diffrac = diffraction.diffraction(fente)
                #Création figure diffraction avec Numpy
                diffrac_numpy = abs(np.fft.fftshift(np.fft.fft2(fente)))**2
        #Ajout texte sur image. Fond : Blanc, oppacité : 50%, police : noir/8
                plt.text(0, 2, "Longueur des rectangles : "+str(longueur)+"\nLargeur des rectangles : "+str(largeur)+"\nEcart entre les rectangles : "+str(ecart), color='k', bbox=dict(facecolor='w', alpha=0.5), fontsize=8)

                #Configuration de l'image
                plt.imshow(diffrac, cmap='hot', interpolation='nearest')
                plt.axis('off') #Désactivation des axes
                #Enregistrement de l'image dans chemin_dossier
                #nom : photo_cote_index
                #bbox_inches='tight' permet de réduire le contour blanc
                fig.savefig(str(chemin_dossier)+"/photo"+str(index), bbox_inches='tight')
                plt.clf() #Remise à zéro de la fenêtre

                plt.imshow(diffrac_numpy, cmap='hot', interpolation='nearest')
                plt.axis('off')
                fig.savefig(str(chemin_dossier_numpy)+"/photo"+str(index), bbox_inches='tight')
                plt.clf()

                index += 1 #On passe à l'image suivante

def carrees(taille_matrice, chemin_dossier, chemin_dossier_numpy):
    """
    Création de taille_matrice^2 images et les sauvegarde dans
    chemin_dossier et chemin_dossier_numpy pour ensuite
    créer un GIF avec ces dernières.
    """

    index = 0 #Compteur
    fig = plt.figure() #Création de la figure

    for cote in range(taille_matrice): #Variation côté des carrés
        for ecart in range(taille_matrice): #Variation écart entre carrés
            fente = fentes.quatre_carrees(taille_matrice, cote, ecart) #Création fente
            #Création de la figure de diffraction par somme discrète
            diffrac = diffraction.diffraction(fente)
            #Création de la figure de diffraciton avec Numpy
            diffrac_numpy = abs(np.fft.fftshift(np.fft.fft2(fente)))**2
        #Ajout texte sur image. Fond : Blanc, oppacité : 50%, police : noir/8
            plt.text(0, 2, "Taille du côté du carré : "+str(cote)+"\nEcart entre les carrés : "+str(ecart), color='k', bbox=dict(facecolor='white', alpha=0.5), fontsize=8)

            #Configuration de la figure
            plt.imshow(diffrac, cmap='hot', interpolation='nearest')
            plt.axis('off') #Désactivation des axes
            #Enregistrement de l'image dans chemin_dossier
            #nom : photo_cote_index
            #bbox_inches='tight' permet de réduire le contour blanc
            fig.savefig(str(chemin_dossier)+"/photo"+str(index), bbox_inches='tight')
            plt.clf() #Remise à zéro de la fenêtre

            plt.imshow(diffrac_numpy, cmap='hot', interpolation='nearest')
            plt.axis('off')
            fig.savefig(str(chemin_dossier_numpy)+"/photo"+str(index), bbox_inches='tight')
            plt.clf()

            index += 1 #On passe à l'image suivante
