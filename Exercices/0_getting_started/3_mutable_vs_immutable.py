"""
# Types mutables vs immutables

- Les types immutables (ex : int, str, tuple) ne peuvent pas être modifiés après leur création.  
- Les types mutables (ex : list, dict, set) peuvent être modifiés en place.

Complétez ou modifiez le code ci-dessous pour que tous les `assert` passent,
en tenant compte de ces différences.

[Doc: id](https://docs.python.org/3/library/functions.html#id)
[Wiki: Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing#:~:text=In%20computer%20programming%2C%20variable%20shadowing,is%20known%20as%20name%20masking.)
"""

a = [1, 2]
assert a == ...
i_a = id(a)
a += [3] 
assert a == ...

