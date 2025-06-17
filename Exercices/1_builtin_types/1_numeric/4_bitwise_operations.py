"""
# Bitwise operations

Python intègre également des opérateurs bits à bits. 

Il est également possible de déclarer des nombres en utilisant leur représentation binaries (e.g., `0b10 == 2`) 
ou hexadécimale (e.g., `0xD == 13`). 

Modifiez les valeurs de `a` et `b`, ainsi que les opérateurs `@` (en respectant les commentaires) jusqu'à ne plus avoir d'erreur.
Vous pouvez utiliser la représentation de votre choix pour initialiser `a` et `b`.

[Wiki: Bitwise operations](https://en.wikipedia.org/wiki/Bitwise_operation)
[Doc: Bitwise operations](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
"""

a = ...
b = ...

#        OP       BITS      HEX     DEC
assert a @ b ==  0b1101 ==  0xD  == 13  # Bitwise Or
assert a @ b ==  0b0100 ==  0x4  ==  4  # Bitwise And
assert a @ b ==  0b1001 ==  0x9  ==  9  # Bitwise Xor
assert   + a == -0b0110 == -0x6  == -6  # Bitwise Not 
assert a @ 2 ==  0b0001 ==  0x1  ==  1  # Right shift
assert a @ 2 == 0b10100 ==  0x14 == 20  # Left shift   
