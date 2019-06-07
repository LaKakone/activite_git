#! /usr/bin/env pyton3
# coding : utf-8

# Importation de calc
from mes_fonctions import calc

def main():
	while True:
		calc()
		reponse = ""
		while reponse not in ["O", "N"]:
			reponse = input("Voulez-vous continuer? (O/N)\nRéponse: ").upper()

		if reponse == "N":
			break

	print("Merci d'utilser CALCULATRICE SCIENTIFIQUE")

if __name__ == "__main__":
	main()