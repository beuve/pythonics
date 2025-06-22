"""
# Generators

Les generateurs sont des fonctions particulieres qui permettent de produire
une sequence de valeurs au fil du temps, au lieu de calculer et retourner
toutes les valeurs en une seule fois dans une liste.

Une fonction devient generateur lorsqu’elle utilise le mot-cle `yield` au lieu
de `return`. Chaque `yield` produit une valeur qui sera recuperee a l’iteration,
et la fonction suspend son execution, reprenant la où elle s’etait arrêtee
lors du prochain appel.

Les generateurs sont tres utiles pour :  
- traiter des sequences potentiellement tres longues ou infinies sans consommer trop de memoire  
- ecrire un code paresseux ((lazy evaluation)[https://en.wikipedia.org/wiki/Lazy_evaluation])  
- simplifier la generation de suites complexes.

Dans cet exercice, selon le booleen passe en parametre, le generateur produit
d'abord toujours le même entier, puis une chaînes de caracteres dont la valeur 
depend du booleen.

[Syntax: Yield](https://docs.python.org/3.10/reference/expressions.html#yield-expressions)
[Doc: Generators](https://wiki.python.org/moin/Generators)
"""

def f(b):
  ...

assert [a for a in f(True)] == [1, "hello"]
assert [a for a in f(False)] == [1, "world"]
