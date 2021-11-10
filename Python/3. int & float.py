# INT EN FLOAT https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3

# print het type van de variabele (INT voor num1 en FLOAT voor num2)
num_1 = 3
num_2 = 3.14
print(f'num 1 = {type(num_1)}')
print(f'num 2 = {type(num_2)}')

# Arithmetic Operators:
# Optellen                          3 + 2
# Aftrekken                         3 - 2
# Maal                              3 * 2
# Delen                             3 / 2
# Modulus                           3 % 2
# Machtsverheffen                   3 ** 2
# Delen en afronden naar beneden    3 // 2

print(f'Optellen: 3 + 2 = {3 + 2}')
print(f'Aftrekken: 3 - 2 = {3 - 2}')
print(f'Maal: 3 * 2 = {3 * 2}')
print(f'Delen: 3 / 2 = {3 / 2}')
print(f'Machtsverheffen: 3 ** 2 = {3 ** 2}')
print(f'Modulus: 3 % 2 = {3 % 2}')
print(f'Rond af naar beneden: 3 // 2 = {3 // 2}')

# haakjes kunnen ook worden gebruikt in python om iets eerst te berekenen
print(f'De som 3 x 2 + 1 = {3 * 2 + 1}') # zonder haakjes
print(f'De som 3 x (2 + 1) = {3 * (2 + 1)}') # met haakjes

# gebruik maken van korte notatie
num = 1
print(f'num = {num}')
num += 1 # Telt +1 op bij num
print(f'Num +1 = {num}')
num *= 10 # vermenigvuldigd num met 10
print(f'Num x 10 = {num}')

# absolute waarde
print(f'De absolute waarde van -3 = {abs(-3)}')

# afronden heel gedal
print(f'De afronding van 3.75 = {round(3.75)}')

# afronden met 1 cijfer achter de komma
print(f'De afronding van 3.75 met 1 cijfer achter de komma = {round(3.75, 1)}')

# Vergelijkingen:
# gelijk aan                3 == 2
# niet gelijk aan           3 != 2
# Groter dan                3 > 2
# Kleiner dan               3 < 2
# Groter of gelijk aan      3 >= 2
# Kleiner of gelijk aan     3 <= 2

num_3 = 3
num_4 = 2

print(f'True or False: {num_3} == {num_4}, {num_3 == num_4}')
print(f'True or False: {num_3} != {num_4}, {num_3 != num_4}')
print(f'True or False: {num_3} > {num_4}, {num_3 > num_4}')
print(f'True or False: {num_3} < {num_4}, {num_3 < num_4}')
print(f'True or False: {num_3} >= {num_4}, {num_3 >= num_4}')
print(f'True or False: {num_3} <= {num_4}, {num_3 <= num_4}')


# String omzetten naar Int
num_5 = '100'       # String
num_6 = '200'       # String
print(f'voor conversie: {num_5}{num_6}')
num_5 = int(num_5)  # Int
num_6 = int(num_6)  # Int
print(f'na conversie: {num_5 + num_6}')