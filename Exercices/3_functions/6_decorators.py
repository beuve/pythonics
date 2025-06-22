"""
# Decorators

Les décorateurs sont des fonctions spéciales permettant de modifier ou
d’étendre le comportement d’autres fonctions sans changer leur code source.

Un décorateur prend une fonction en argument, et retourne une nouvelle fonction,
souvent une fonction interne qui exécute du code avant et/ou après l’appel
de la fonction d’origine, ou modifie ses arguments ou son résultat.

Cette technique est très utilisée pour ajouter des fonctionnalités transversales
comme :  
- le logging  
- la gestion des droits d’accès  
- la mesure de performance  

Dans cet exercice, vous devez écrire un décorateur qui modifie le résultat
de la fonction décorée en l’augmentant de 1.

Modifiez la fonction `decorator` et appliquez-la à `f` jusqu'à ne plus avoir d'erreur.

[Syntax: Function definition](https://docs.python.org/3.10/reference/compound_stmts.html#function-definitions)
[Doc: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
"""

def decorator(func):
    ...

def f():
    return 2

assert f() == 3
