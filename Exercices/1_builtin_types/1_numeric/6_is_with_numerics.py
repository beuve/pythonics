"""
# Cached int

L'implémentation actuelle de python utilise un cache pour les entiers de -5 à 256. 
Quand vous créez un int, si il est dans cette interval, une reference vers cet
objet est renvoyée. 

Ajoutez ou non un `not` à chaque `assert` jusqu'à ne plus avoir d'erreur.

[Doc: cached int(https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong)
"""

a = 2
assert a is 2

a = 1000
assert a is 1000
