import numpy
import pygame
class Engine():
	def __init__(self,m,ft,fg,x,v,dt,FU):			#Mass, Force of Thrust, Force of Gravity, Starting position, starting velocity, delta time, Fuel Usage
		self.m = m
		self.maxft = ft
		self.fg = fg
		self.x = x
		self.v = v
		self.fin = False
		self.dt = dt
		self.timepassed = 0
		self.FU = FU
		self.crashed = False
		self.ft = 0
	def _update_mass(self):							#Function updating mass by subtracting it's fuel usage multipied by delta time						
		self.mass = self.mass - self.FU*self.dt
		self.empty = 0
	def _update_position_and_speed(self):
		self.v = self.v + self.fg * self.dt + (self.ft/self.m)* self.dt
		self.x = self.x + self.v * self.dt 		    		  #Function updating position and speed form the formulas
		if self.x < 0:
			if self.v > 3:
				self.crashed = True
			self.v = 0 
			self.x = 0



	def _change_ft(self,newft):
		self.oldft = self.ft
		self.ft = self.ft + newft
		if self.ft >35000000:
			self.ft = 35000000
		elif self.ft < 0:
			self.ft = 0


	def _launch(self):
		while self.fin == False:
			self._update_position_and_speed()
			self.timepassed = self.timepassed + self.dt
			print("x -",self.x,"v - (",self.v,")t -",self.timepassed)
			if self.v > 60:
				self._change_ft(0)
			if self.timepassed > 50:
				self.fin = True														  #Testing function simulating rocket launch with maximal thrust until the rocket reaches 2000 m 

