'''
program, ktory poprosi uzytkowanika o slowo i wyliczy jego wartosc punktowa na podstawie wartosci
kazdej z liter. litera 'a' ma wartosc '1', b ma wartosc 2.do przechowania wartosci punktowej dla liter
nalezy wykorzystac slownik
'''
import string


word = input('Podaj wybrane przez siebie słowo:').rstrip()

letters = list((string.ascii_lowercase))

values = list(range(1, 27))

score = dict(zip(letters, values))

def scrable_score(word):
    return sum(score[x] for x in word)


print('Twój wynik to:', scrable_score(word))


