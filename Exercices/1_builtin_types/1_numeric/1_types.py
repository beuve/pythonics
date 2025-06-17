"""
# Types numériques

Python utilise 3 types numériques différents : `int`, `float`, et `complex`.

Ces types sont immuables, ce qui signifie que les opérateurs ne modifient 
pas les valeurs des variables, mais plutôt les créer de nouvelles.

Modifiez les valeurs de `a` et `b`, ainsi que l'opérateur `@` (en respectant 
les commentaires) jusqu'à ne plus avoir d'erreur.

[Doc: Types numériques](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
"""

# TODO
a = ...
b = ...
c = ...

# Do not touch!
assert isinstance(a, int) 
assert isinstance(b, float)
assert isinstance(c, complex)

assert a + b == 3.2
assert b + c == 5.2 + 2j
assert a + c == 4 + 2j
  
