"""
# Comprendre assert

L’instruction `assert` permet de vérifier qu’une condition est vraie.  
Si la condition est fausse, Python lève une exception `AssertionError`.  
Cela est très utile pour valider que votre code fonctionne comme prévu.

Complétez ou modifiez les variables ci-dessous pour que tous les `assert` passent.

[Syntax: assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
[Doc: isinstance](https://docs.python.org/3/library/functions.html#isinstance)
"""

a = ...
b = ...

assert a == b
assert a + b == 20
assert isinstance(a, int)
assert a != 0
assert b > 0
