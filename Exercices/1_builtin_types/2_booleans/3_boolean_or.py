"""
# Operateurs booleen

Les operateurs booleen `and` et `or` sont _lazy_, ce qui signifie que dans l'exemple 
`False and a`, `a` ne sera jamais evalue, puisque quelque soit sa valeur, l'expression
sera fausse. 

De plus, les operateurs booleen de python ne renvoi pas necessairement `True` ou `False`, 
mais renvois la derniere valeur evaluee. Par exemple, `1 or a` renverra `1` et `0 or a`
renverra `a` (quelque soit sa valeur).

L'objectif de cet exercice est de deduire les valeurs de `a`, `b` et `c` a partir des
expressions `or` suivantes.

Modifiez les valeurs de `a`, `b` et `c` jusqu'a ne plus avoir d'erreur.

[Wiki: Evaluation paresseuse](https://fr.wikipedia.org/wiki/%C3%89valuation_paresseuse)
[Syntax: Operateurs booleen](https://docs.python.org/3/reference/expressions.html#boolean-operations)
[Doc: Operateurs booleen](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert (a or b) == 2
assert (b or c) == True
assert (False or c) == 0
