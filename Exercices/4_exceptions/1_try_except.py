"""
# `try` - `except`

Comme beaucoup d'autres languages, python utilise un [système de gestion des exceptions](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions)
pour gérer les erreurs. Le principe de fonctionnement est simple: Lorsque une exception
est levée, python remonte la chaine d'appèle afin de trouver une instruction `except`
gerant cette erreur. Si aucune instruction de ce genre n'est trouvé, le programme 
s'arrète.

Dans cet example, l'objectif est de faire la somme des éléments de `a` divisés
par les éléments de `b`. Cependant, un des élément de `b` est 0 est cause donc 
une erreur. Nous souhaitons compter les divisions par 0 comme des divisions par
1 pour eviter l'erreur.

[Syntax: try statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)
[Doc: try / except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
[Doc: zip](https://docs.python.org/3.3/library/functions.html#zip)
[Doc: ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)
"""

# Do not touch!
a = [1, 2, 3]
b = [2, 0, 6]
s = 0

# TODO
for (n,d) in zip(a,b):
  s += n / d

# Do not touch!
assert s == 3
