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

# Lijst omkeren
profielen.reverse()
print(profielen)

# Lijst sorteren (Tekst op aflabet A-Z en nummers oplopend 1-9)
nums = [2, 6, 3, 1, 5, 4]
profielen.sort()
nums.sort()
print(profielen)
print(nums)

# Lijst sorteren en omdraaien (Tekst op aflabet Z-A en nummers aflopend 9-1)
profielen.sort(reverse=True)
nums.sort(reverse=True)
print(profielen)
print(nums)

# functie sorted
gesorteerde_profielen = sorted(profielen)
print(gesorteerde_profielen)

# functie minimale waarde, in dit voorbeeld 1
print(min(nums))

# funtie som, in dit voorbeeld 21
print(sum(nums))

# print het index nummer van een waarde in een list/array, in dit voorbeeld Infrastructuur
print(profielen)
print(profielen.index('Infrastructuur'))

# True/False manrier om te controleren of zich iets in de lijst bevind
print('Test' in profielen)  # False
print('Media' in profielen) # True

# For loop print lijst
for item in profielen:
    print(item)

# For loop print lijst met numering startent met 1 ipv 0
for index, item in enumerate(profielen, start=1):
    print(index, item)

# Join alle waardes in de lijst in 1 string met een komma als scheidingsteken
profielen_str = ' - '.join(profielen)
print(profielen_str)

# Maak van 1 string met - gescheiden waardes een lijst.
nieuwe_lijst = profielen_str.split(' - ')
print(nieuwe_lijst)

#