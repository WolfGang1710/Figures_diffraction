"""
Title: Projet IPT - Diffraction DI
Description: Ce programme permet de créer différents types de fentes
             pour faire des figures de diffraction.
"""

#pylint: disable=invalid-name

#=== Importation des modules ===

import numpy as np

def creer_matrice_zeros(n):
    """Créée une matrice carrée de taille n remplie de zéros."""

    return np.zeros((n, n)) #Création matrice carrée de taille n

def carree(n, cote):
    """Renvoie une matrice de taille n contenant en son centre
    un carré de côté cote remplie de 1.
    """
    M = creer_matrice_zeros(n) #Création matrice carrée de 0 de taille n
    #Balayage de la matrice
    for i in range(n):
        for j in range(n):
            #On remplie de 1 tout sur qui est à l'intérieur du carré
            #Division par 2 afin d'être au "milieu" de la matrice
            if (n - cote) / 2 < i < (n + cote) / 2:
                if (n - cote) / 2 < j < (n + cote) / 2:
                    M[i][j] = 1
    return M

def circulaire(n, r):
    """Renvoie une matrice de taille n contenant en son centre
    un cercle de rayon r remplie de 1.
    """
    M = creer_matrice_zeros(n) #Création de la matrice de 0 de taille n
    x, y = n//2, n//2 #Coordonnées du "milieu" de la matrice
    #Balayage de la matrice
    for i in range(n):
        for j in range(n):
            #équation du cercle de centre (x, y) et de rayon r
            if (i - x)**2 + (j - y)**2 <= r**2:
                M[i][j] = 1 #Tout les 0 dans le cercle prennent la valeur 1
    return M

def rectangulaires(n, longueur, largeur, ecart):
    """Renvoie une matrice de taille n contenant en son centre deux
    rectangles de dimensions longueur x largeur remplie de 1 écarté de
    ecart du centre de la matrice.
    """
    M = creer_matrice_zeros(n) #Création de la matrice de 0 de taille n
    #Balayage de la matrice
    for i in range(n):
        for j in range(n):
            #On remplie de 1 tout ce qui est dans le périmètre de chaque
            #rectangle. Les rectangles se situent à ecart du centre de
            #la matrice.
            #Division par 2 afin d'être au "milieu" de la matrice.
            if (n - ecart - longueur) / 2 < j < (n + ecart + longueur) / 2:
                if (n - ecart - largeur) / 2 < i < (n - ecart + largeur) / 2 or (n + ecart - largeur) / 2 < i < (n + ecart + largeur) / 2:
                    M[i][j] = 1
    return M

def quatre_carrees(n, cote, ecart):
    """Renvoie une matrice de taille n contenant en son centre
    quatre carré de côté cote. Les carrés sont décalés les uns
    par rapport aux autre de ecart.
    """
    M = creer_matrice_zeros(n) #Création de la matrice de 0 de taille n
    #Balayage de la matrice
    for i in range(n):
        for j in range(n):
            #On remplie de 1 tout ce qui est dans le périmètre de chaque
            #carré. Les carré se situent à ecart du centre de
            #la matrice.
            #Division par 2 afin d'être au "milieu" de la matrice.
            if (n - ecart - cote) / 2 < i < (n - ecart + cote) / 2  or (n + ecart - cote) / 2 < i < (n + ecart + cote) / 2:
                if (n - ecart - cote) / 2 < j < (n - ecart + cote) / 2 or (n + ecart - cote) / 2 < j < (n + ecart + cote) / 2:
                    M[i][j] = 1
    return M
