#!/usr/bin/env python3
from random import randint
from math import pi,sqrt
class Rettangolo:
	def __init__ (self,base,altezza):
		self.base = base
		self.altezza = altezza
		
	@property
	def area(self):
		return self.base * self.altezza
		
	def __str__(self):
		return f"Rettangolo:\nBase: {self.base}, Altezza: {self.altezza}, Area: {self.area}"
	
	def perimetro(self):
		return self.base * 2 + self.altezza *2
	
	def is_quadrato(self):
		return self.base == self.altezza
	
	def ridimensiona(self,fattore:int):
		self.base *= fattore
		self.altezza *= fattore
		
class Cerchio:
	def __init__(self,raggio):
		self.raggio = raggio
		self.circonferenza = 2*pi*self.raggio
		
	@property 
	def area(self):
		return self.raggio**2 * pi
		
	def visualizza(self):
		print(f"Cerchio:\nRaggio: {self.raggio}, Area:{self.area:.2f}, Circonferenza: {self.circonferenza:.2f} ")
	
	def ridimensiona(self,fattore:int):
		self.raggio *= fattore
	
rettangolo = Rettangolo(randint(0, 50),randint(0, 50))
cerchio = Cerchio(randint(0, 50))
print(rettangolo)
cerchio.visualizza()

if cerchio.area > rettangolo.area:
	print("Il cerchio ha un area maggiore rispetto al rettangolo")
	fattore = sqrt(cerchio.area/rettangolo.area)
	rettangolo.ridimensiona(fattore)
	print(f"La nuova area del rettangolo ridimensionata con fattore {fattore:.2f} è {rettangolo.area:.2f} ")
else:
	print("Il rettangolo ha un area maggiore rispetto al cerchio")
	fattore = sqrt(rettangolo.area / pi)/cerchio.raggio
	cerchio.ridimensiona(fattore)
	print(f"La nuova area del cerchio ridimensionata con fattore {fattore:.2f} è {cerchio.area:.2f} ")
	