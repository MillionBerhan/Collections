import random


randomNummer = 0
kleurenDictionary = dict()

antwoord = input('Hoeveel M&Ms wilt u hebben? invoer:')

if not antwoord.isdigit():
    print('Alleen cijfers graag...')
elif int(antwoord) <1:
    print ("Getal groter dan 0 graag...")
else:
    antwoord = int(antwoord)

def hulpje(kleur):
    global randomNummer, antwoord 
    randomNummer = random.randint(1, antwoord)
    antwoord = antwoord - randomNummer
    kleurenDictionary[f"{kleur}"] = randomNummer

def zakjevullen(): 
    global antwoord
    hulpje("rood")
    randomNummer = random.randint(1, antwoord)
    antwoord = antwoord - randomNummer
    kleurenDictionary["blauw"] = randomNummer
    randomNummer = random.randint(1, antwoord)
    antwoord = antwoord - randomNummer
    kleurenDictionary["oranje"] = randomNummer
    kleurenDictionary["bruin"] = antwoord
zak=zakjevullen()

def formule():
    for x in kleurenDictionary:
        print(repr(x), ":", kleurenDictionary[x])  
formule()


print ("Bedankt voor het gebruiken van Milware!")
















































