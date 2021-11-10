# LISTS, TUPLES, and SETS https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4

# Maak een lijst aan "Profielen" met als inhoud de profielen van Fontys-ICT
profielen = ['Infrastructuur', 'Media', 'Software', 'Buisiness']

# Print lijst met profielen
print(profielen)

# Print hoeveelheid profielen in de lijst profielen
print(len(profielen))

# Print het eerste profiel uit de lijst profielen
print(profielen[0])

# Print de profielen 0 tot 2 uit de lijst profielen
print(profielen[0:2])

# Profiel toevoegen achteraan de lijst profielen
profielen.append('Technology')
print(profielen)

# Profiel toevoegen - in dit voorbeeld op de 1e positie, 0 - in de lijst profielen
profielen.insert(0, 'Proftaak')
print(profielen)

# 2 lijsten samenvoegen, lijst 2 wordt ahteraan in lijst 1 gezet
profielen_2 = ['Startsemster', 'Verdieping']
profielen.extend(profielen_2)
print(profielen)

# Items verwijderen uit de lijst
profielen.remove('Proftaak')
print(profielen)

# Items verwijderen uit de lijst met pop() - verwijderd altijd de laaste uit een lijst -
popped = profielen.pop()
print(popped)
print(profielen)

# 