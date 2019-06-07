#! /usr/bin/env pyton3
# coding : utf-8

# Importation de mes foctions
from mes_fonctions import *
from geometrie import *
def main():
	"""Cette fonction contient les instructions principales"""
	nom = input("Votre nom: ") # saisie du nom
	salutation(nom)

	# Saisie d'un nombre par l'utilisateur
	nombre = input("Donnez un entier: ")

	try:
		nombre = int(nombre) # Conversion

		assert nombre >= 0

		# Affichage de la table du nombre entré
		table(nombre)

		print("{}! = {}".format(nombre, fact(nombre)))
	except ValueError:
		print("Erreur! Entrée Invalide")
	except AssertionError:
		print("Erreur ! Le nombre entré est négatif")
	
	print("----Calcul géométrique-----")
	lg = float(input("Longueur du rectangle: "))
	larg = float(input("Largeur du rectangle: "))
	print("Le périmètre du rectangle est " + str(perimetreR(lg, larg)))
	print("L'aire du rectangle est " + str(aireR(lg, larg)))

	rayon = float(input("Rayon du cercle: "))
	print("Le périmètre du cercle est " + str(perimetreC(rayon)))
	print("L'aire du cercle est " + str(aireC(rayon)))
	print("Au revoir " + nom)

if __name__ == "__main__":
	main()