#STRINGS https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2

# Print Hello World
message = 'Hello World'
print(message)

# Hiermee print je de hoeveelheid karakters (getal) in de string
print(len(message))

# print de 7e karakter uit de string, beginnend bij 0
print(message[6])

# print de eerste 5e karakters uit de string, beginnend bij 0
print(message[0:5])

# print de string volledig in hoofdletters
print(message.upper())

# print het aantal (getal) maal een bepaalde letter voorkomt in de string
print(message.count('l'))

# print de index (getal) waar het gezochte woord in de string begint
print(message.find('World'))

# vervangt een woord in de string, de eerste parameter wordt vervangen voor de 2e parameter
message = message.replace('World', 'Universe')
print(message)

# plakt 2 strings aan elkaar voor een string met een komma en spatie er tussen + de tekst welcome!
greeting = 'Hello'
name = 'Bart'
welcome_message = greeting + ', ' + name + '. Welcome!'
print(welcome_message)

# Plakt een string aan elkaar maar blijft beter leesbaar. met de .format functie worden de {} placeholders doorgegeven als parameters
welcome_message2 = '{}, {}. Welcome!'.format(greeting, name)
print(welcome_message2)

# Python 3.6 F fortmating een string, de meest leesbare manier van een string samenstellen.
welcome_message3 = f'{greeting}, {name}. Welcome!'
print(welcome_message3)