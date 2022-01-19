from typing import Dict
import random

print ("2.rekenen met lists")

listOne = [q for q in range(1,11,1)]
listTwo = [q for q in range(2, 21, 2)]

def geforceerde_input(vraag: str, toegestaan: list[str],
        niet_goed_bericht: str = 'Sorry, probeer het nog eens') -> str:  # hier wordt er gecontroleerd op een bug
    while not ((antwoord := input(vraag).lower()) in toegestaan):
        print(niet_goed_bericht)

def plussommen():  # hier worden de plussommen getoont
    for q in range(min(len(listOne), len(listTwo))):
        print("{:<2} + {:<2} = {:<5}".format(listOne[q], listTwo[q], listOne[q] + listTwo[q]))
plussommen()

print ("---------------------")

def minsommen(): # hier worden de minsommen getoont
    for q in range(min(len(listOne), len(listTwo))):
        print("{:<2} - {:<2} = {:<5}".format(listOne[q], listTwo[q], listOne[q] - listTwo[q]))
minsommen()

print ("----------------------")

def keersommen(): # hier worden de keersommen getoont
    for q in range(min(len(listOne), len(listTwo))):
        print("{:<2} * {:<2} = {:<5}".format(listOne[q], listTwo[q], listOne[q] * listTwo[q]))
keersommen()

print ("----------------------")

def delendoor():# hier worden de delendoor sommen getoont
    for q in range(min(len(listOne), len(listTwo))):
        print("{:<2} / {:<2} = {:<5}".format(listOne[q], listTwo[q], listOne[q] / listTwo[q]))
delendoor()

print ("----------------------")
# hier komt er een randomlist van 3 t/m 10 
spelList= ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']

def spelProgramma(spelList, minimum, maximum):
    rng=random.choice(range(minimum, maximum))
    for x in range(rng):
        print(random.choice(spelList))

spelProgramma(spelList, 3, 10)

print ("----------------------")

print ("Bedankt voor het gebruiken van Milware!")

    


    