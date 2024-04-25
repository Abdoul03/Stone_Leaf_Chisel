import sys
import random

print("Pierre, Feuille, ciseau")

playerChoise = input("entrer...\n1 pour Piere,\n2 pour Feuille or \n3 pour ciseau:\n\n")

player = int(playerChoise)

if player < 1 | player > 3 :
    sys.exit("vous devez choisir un nom entre 1 2 3")

computerChoise = random.choice("123")

computer = int(computerChoise)

print("")
print("Votre choix est : " + playerChoise +".")
print("Le choix de Python est : " + computerChoise +".")
print("")

if player == 1 and computer == 3 :
    print("🎉 Vous avez Gangner !")
elif player == 2 and computer == 1 :
    print("🎉 Vous avez Gangner !")
elif player == 3 and computer == 2 :
    print("🎉 Vous avez Gangner !")
elif player == computer :
    print("😲 Egaliter !")
else:
    print("🐍 Python a Gangner !")

print("")