#! /usr/bin/env python3
# coding : utf-8


############################
## Table de mutiplication ##
############################
def table(n):
	"""Cette fonction affiche la table de mutimplication 
	de l'entier qu'il reçoit en paramètre"""
	for i in range(0,12):
		print("{} * {} = {}".format(n, i + 1, n * (i + 1)))

#############################
## Factorielle d'un entier ##
#############################
def fact(n):
	"""Elle renvoie le factorille de l'entier n"""
	if n in [0, 1]:
		return n
	else:
		return n * fact(n - 1)

#############################
## Salutation et Bienvenue ##
#############################
def salutation(nom):
	"""Elle souhaite la bienvenue"""
	print("Salut Mr/Mme {} !\nSoyez la bienvenue dans le programme de calcul !".format(nom))

#########################
## Calculatrice simple ##
#########################
def calc():
	"""Cette fonction calc peut effectuer les opérations de base"""
	print("--- CALCULATRICE SIMPLE ---")
	operation = input("Votre opération: ")
	try:
		resultat = eval(operation)

		print(operation + " = " + str(resultat))
	except:
		print("Erreur! Entrée Invalide")
