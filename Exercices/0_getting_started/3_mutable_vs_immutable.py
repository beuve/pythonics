"""
# Types mutables vs immutables

- Les types immutables (ex : int, str, tuple) ne peuvent pas être modifies apres leur creation.  
- Les types mutables (ex : list, dict, set) peuvent être modifies en place.

Modifiez les operateurs `@` par `==` (egal) ou `!=` (differents) pour que tous les `assert` passent.

[Doc: id](https://docs.python.org/3/library/functions.html#id)
[Wiki: Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing#:~:text=In%20computer%20programming%2C%20variable%20shadowing,is%20known%20as%20name%20masking.)
"""

a = [1, 2]      # Creez une liste 
b = a           # b pointe vers le même objet que a
a += [2]        # ajoute 2 a la fin de a
# Les lists sont des types mutables, donc l'objet pointe par 
# a a simplement ete modifie en memoire. a et b pointe donc 
# toujours vers le même objet.
assert id(a) @ id(b) 

a = (1, 2)      # Creez un tuple 
b = a           # b pointe vers le même objet que a
a += (2,)       # ajoute 2 a la fin de a
# Les tuples sont des types immutables, donc pour ajouter
# 2 a la fin de a il faut creer un nouveau tuple avec l'element
# en plus. a est un nouvel objet.
assert id(a) @ id(b)

