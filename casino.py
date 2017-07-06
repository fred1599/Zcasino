from random import randrange
from math import ceil

somme = 1000

while True:
    numero = int(input("Votre numéro ? "))
    if numero not in range(50):
        continue
    
    while True:
        mise = int(input("Votre mise ? "))
        if 0 < mise <= somme:
            break
    
    num_gagnant = randrange(50)
    
    if numero == num_gagnant:
        print("Bien joué !")
        somme += mise * 3
    
    elif numero % 2 == num_gagnant % 2:
        print("Bonne couleur !")
        somme += ceil(mise * 0.5)
    
    else:
        print("Perdu !")
        somme -= mise
    
    print("Votre nouvelle somme est: ", somme)
    
    if somme == 0:
        print("Plus d'argent ! Désolé...")
        break
    
    continuer = input("Voulez-vous continuer (o/n)? ") == "o"
    if not continuer:
        break

print("Vous repartez avec la somme: ", somme, "€")
