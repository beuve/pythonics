"""
# Opérateurs booléen

Les opérateurs booléen `and` et `or` sont _lazy_, ce qui signifie que dans l'exemple 
`False and a`, `a` ne sera jamais évalué, puisque quelque soit sa valeur, l'expression
sera fausse. 

De plus, les opérateurs booléen de python ne renvoi pas nécessairement `True` ou `False`, 
mais renvois la dernière valeur évaluée. Par exemple, `1 or a` renverra `1` et `0 or a`
renverra `a` (quelque soit sa valeur).

L'objectif de cet exercice est de déduire les valeurs de `a`, `b` et `c` à partir des
expressions `or` suivantes.

Modifiez les valeurs de `a`, `b` et `c` jusqu'à ne plus avoir d'erreur.

[Wiki: Evaluation paresseuse](https://fr.wikipedia.org/wiki/%C3%89valuation_paresseuse)
[Syntax: Opérateurs booléen](https://docs.python.org/3/reference/expressions.html#boolean-operations)
[Doc: Opérateurs booléen](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert (a or b) == 2
assert (b or c) == True
assert (False or c) == 0
