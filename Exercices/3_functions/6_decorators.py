"""
# Decorators

Les decorateurs sont des fonctions speciales permettant de modifier ou
d’etendre le comportement d’autres fonctions sans changer leur code source.

Un decorateur prend une fonction en argument, et retourne une nouvelle fonction,
souvent une fonction interne qui execute du code avant et/ou apres l’appel
de la fonction d’origine, ou modifie ses arguments ou son resultat.

Cette technique est tres utilisee pour ajouter des fonctionnalites transversales
comme :  
- le logging  
- la gestion des droits d’acces  
- la mesure de performance  

Dans cet exercice, vous devez ecrire un decorateur qui modifie le resultat
de la fonction decoree en l’augmentant de 1.

Modifiez la fonction `decorator` et appliquez-la a `f` jusqu'a ne plus avoir d'erreur.

[Syntax: Function definition](https://docs.python.org/3.10/reference/compound_stmts.html#function-definitions)
[Doc: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
"""

def decorator(func):
    ...

def f():
    return 2

assert f() == 3
