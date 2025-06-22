"""
# Generateurs

L'inconvenient des listes en comprehensions est que l'ensemble des valeurs
doivent pouvoir être stockees simultanements en memoire. Si je souhaite 
iterer sur une tres grande liste, je dois ainsi m'assurer que j'ai la place
en memoire. 

Pour eviter ce probleme, il est possible d'utiliser un `generateur`. Dans une
boucle for, les generateurs s'utilisent de la même façon qu'une liste,
mais chaque elements n'est calcule que lorsque c'est son tour dans la boucle, 
evitant de charger tout les elements simultanement.

L'inconvenient des generateur est qu'il est impossible d'acceder a un indice 
precis (d'ailleurs, la fonction `len` ne fonctionne pas sur eux).

Calculez, a l'aide d'un generateur, la somme des nombres divisibles par
3 ou 5 inferieur a 1000. Stockez le resultat dans `b`.

[Syntax: generator](https://docs.python.org/3/reference/expressions.html#generator-expressions)
[Wiki: Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation)
[Source: Euler project](https://projecteuler.net/problem=1)
"""

# TODO
b = ...

# Do not touch!
assert b == 233168
