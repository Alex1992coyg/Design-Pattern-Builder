#!/usr/bin/env python3

'''creating builder for ROBOT '''
class Robot:
	def __init__(self):
		self.bipedal = False
		self.quadrapedal = False
		self.wheeled = False
		self.flying = False
		self.movement = []
		self.detection_sm = []

	def __str__(self):
		string = " "
		if self.bipedal:
			string = string + ":BIPEDAL "
		if self.quadrapedal:
			string = string + "QUADRAPEDAL "
		if self.wheeled:
			string += "ROBOT ON WHEELS "
		if self.flying:
			string += "FLYING ROBOT \n"
		else:
			string +="ROBOT \n"

		if self.movement:
			string += "Movement Modules Installed:\n"
		for module in self.movement:
			string +="- " + str(module) + "\n"
		if self.detection_sm:
			string += "Detection System Installed: \n"
		for system in self.detection_sm:
			string +="- " + str(system) + "\n"
		return string
class BipedalLegs:
	def __str__(self):
		return "two legs"
class QuadrapedalLegs:
    def __str__(self):
        return "four legs"
class Arms:
    def __str__(self):
        return "four legs"
class Wings:
    def __str__(self):
        return "wings"
class Blades:
    def __str__(self):
        return "blades"
class FourWheels:
    def __str__(self):
        return "four wheels"
class TwoWheels:
    def __str__(self):
        return "two wheels"
class CameraDetectionSystem:
    def __str__(self):
        return "cameras"
class InfraredDetectionSystem:
    def __str__(self):
        return "infra-red"
class SonarWaveDetectionSystem:
	def __str__(self):
		return "Sonar-wave"
