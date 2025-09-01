#!/usr/bin/python3
"""
Ce script calcule la factorielle d'un nombre entier donné en argument
lors de l'exécution du programme.

Exemple :
    $ python script.py 5
    120

Le script utilise une fonction récursive pour faire le calcul.
"""

import sys

def factorial(n):
    """
    Retourne la factorielle de n (n!).

    Utilise une approche récursive.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
