"""
# Fonctions anonymes

Les fonctions anonymes, appelées aussi fonctions lambda, sont des fonctions
définies de manière concise sans utiliser le mot-clé `def`. Elles sont particulièrement
utiles pour écrire des fonctions simples et temporaires, souvent utilisées en
paramètres d’autres fonctions comme `map`, `filter` ou `reduce`.

Cela permet d'éviter la définition complète d’une fonction classique pour de petites
opérations, rendant le code plus compact et lisible dans ces cas.

Dans cet exercice, on utilise des lambdas pour :  
- transformer chaque élément d’une liste (`map`)  
- filtrer les éléments selon une condition (`filter`)  
- réduire une liste à une seule valeur via un accumulateur (`reduce`).

Modifiez les `...` avec des lambdas jusqu'à ne plus avoir d'erreur.

[Syntax: Lambda](https://docs.python.org/3.10/reference/expressions.html#lambda)
[Doc: lambda expressions](https://docs.python.org/3.13/tutorial/controlflow.html#lambda-expressions)
[Doc: map](https://docs.python.org/3/library/functions.html#map)
[Doc: filter](https://docs.python.org/3/library/functions.html#filter)
[Doc: reduce](https://docs.python.org/fr/3.13/library/functools.html#functools.reduce)
"""

# Do not touch!
from functools import reduce
a = [1, 2, 3, 4, 5]

# TODO
assert list(map(..., a)) == [2, 4, 6, 8, 10] 
assert list(filter(..., a)) == [1, 3, 5] 
assert reduce(..., a) == 15
