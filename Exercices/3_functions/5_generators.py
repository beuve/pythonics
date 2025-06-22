"""
# Generators

Les générateurs sont des fonctions particulières qui permettent de produire
une séquence de valeurs au fil du temps, au lieu de calculer et retourner
toutes les valeurs en une seule fois dans une liste.

Une fonction devient générateur lorsqu’elle utilise le mot-clé `yield` au lieu
de `return`. Chaque `yield` produit une valeur qui sera récupérée à l’itération,
et la fonction suspend son exécution, reprenant là où elle s’était arrêtée
lors du prochain appel.

Les générateurs sont très utiles pour :  
- traiter des séquences potentiellement très longues ou infinies sans consommer trop de mémoire  
- écrire un code paresseux ((lazy evaluation)[https://en.wikipedia.org/wiki/Lazy_evaluation])  
- simplifier la génération de suites complexes.

Dans cet exercice, selon le booléen passé en paramètre, le générateur produit
d'abord toujours le même entier, puis une chaînes de caractères dont la valeur 
dépend du booléen.

[Syntax: Yield](https://docs.python.org/3.10/reference/expressions.html#yield-expressions)
[Doc: Generators](https://wiki.python.org/moin/Generators)
"""

def f(b):
  ...

assert [a for a in f(True)] == [1, "hello"]
assert [a for a in f(False)] == [1, "world"]
