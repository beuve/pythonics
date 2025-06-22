"""
# Fonctions anonymes

Les fonctions anonymes, appelees aussi fonctions lambda, sont des fonctions
definies de maniere concise sans utiliser le mot-cle `def`. Elles sont particulierement
utiles pour ecrire des fonctions simples et temporaires, souvent utilisees en
parametres d’autres fonctions comme `map`, `filter` ou `reduce`.

Cela permet d'eviter la definition complete d’une fonction classique pour de petites
operations, rendant le code plus compact et lisible dans ces cas.

Dans cet exercice, on utilise des lambdas pour :  
- transformer chaque element d’une liste (`map`)  
- filtrer les elements selon une condition (`filter`)  
- reduire une liste a une seule valeur via un accumulateur (`reduce`).

Modifiez les `...` avec des lambdas jusqu'a ne plus avoir d'erreur.

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
