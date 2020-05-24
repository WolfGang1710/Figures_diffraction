"""
Title: Projet IPT - Diffraction DI
Description: Ce programme permet de calculer la valeur (couleur)
             de chaque point de l'écran. On utlise une méthode
             de somme discrète.
"""

#pylint: disable=invalid-name

#=== Importation des modules ===

import numpy as np

def diffraction(Fente):
    """Renvoie une matrice représentant une figure de diffraction.
    Fente représentante une matrice également (la matrice de la fente).
    """

    n = np.shape(Fente)[0] #Dimension de la matrice de la fente
    ecran = np.zeros((n, n)) #Création matrice carrée de taille n
    lambdaN = 1/n #Longueur d'onde du faisceau
    for i in range(n):
        y = (-i + n/2)/n #Ordonnée sur l'écran
        for j in range(n):
            x = (j - n/2)/n #Abscisse sur l'écran
            somme = 0
            for iprime in range(n):
                yprime = (-iprime + n/2)/n #Ordonnée fente
                for jprime in range(n):
                    xprime = (jprime - n/2)/n #Abscisse fente
                    #Calcul double intégrale
                    somme += Fente[iprime][jprime]*np.exp(-(1j)*(2*np.pi*(xprime*x + yprime*y))/(lambdaN))
            ecran[i][j] = (np.abs(somme))**2 #Calcul du module au carrée
    return ecran
