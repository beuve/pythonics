"""
# Générateurs

L'inconvénient des listes en compréhensions est que l'ensemble des valeurs
doivent pouvoir être stockées simultanéments en mémoire. Si je souhaite 
itérer sur une très grande liste, je dois ainsi m'assurer que j'ai la place
en mémoire. 

Pour éviter ce problème, il est possible d'utiliser un `générateur`. Dans une
boucle for, les générateurs s'utilisent de la même façon qu'une liste,
mais chaque éléments n'est calculé que lorsque c'est son tour dans la boucle, 
évitant de charger tout les éléments simultanément.

L'inconvénient des générateur est qu'il est impossible d'acceder à un indice 
précis (d'ailleurs, la fonction `len` ne fonctionne pas sur eux).

Calculez, à l'aide d'un générateur, la somme des nombres divisibles par
3 ou 5 inférieur à 1000. Stockez le résultat dans `b`.

[Syntax: generator](https://docs.python.org/3/reference/expressions.html#generator-expressions)
[Wiki: Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
[Source: Euler project](https://projecteuler.net/problem=1)
"""

# TODO
b = ...

# Do not touch!
assert b == 233168
