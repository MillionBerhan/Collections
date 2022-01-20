import random

kleuren = ["oranje", "blauw", "groen", "bruin"]

def zakjevullen(kleuren, minimum, maximum): 
    zak=[]  
    rng = random.randint(minimum, maximum)

    for rng in range(rng):
        print(random.choice(kleuren))
        zak.append(random.choice(kleuren))
    return zak
while True:

    antwoord = input('Hoeveel M&Ms wilt u hebben?')

    if antwoord.isdigit():
        break
    else:
        print('Alleen cijfers graag...')

zak=zakjevullen(kleuren, 1, int(antwoord))

print ("---------------------------")

print ("Bedankt voor het gebruiken van Milware!")

print ()
