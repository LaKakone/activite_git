#! /usr/bin/env python3
# coding : utf-8

from math import pi

def perimetreR(longueur, largeur):
	return 2 * (longueur + largeur)

def aireR(longueur, largeur):
	return longueur * largeur

def perimetreC(rayon):
	return 2 * rayon * pi

def aireC(rayon):
	return rayon * rayon * pi