import numpy as np

class Local:
    def __init__(self, street, city, state, medTemp, medRad, lat, long, angle, radiation = np.array([])):
        self.street = street
        self.city = city
        self.state = state
        self.medTemp = medTemp
        self.medRad = medRad
        self.lat = lat
        self.long = long
        self.angle = angle
        self.radiation = radiation 

    # Funções para modificar
    def setStreet(self, street):
        self.street = street
    
    def setCity(self, city):
        self.city = city
    
    def setState(self, state):
        self.state = state

    def setMedTemp(self, medTemp):
        self.medTemp= medTemp
    
    def setMedRad(self, medRad):
        self.medRad = medRad

    def setLat(self, lat):
        self.lat = lat

    def setLong(self, long):
        self.long = long

    def setAngle(self, angle):
        self.angle = angle

    #Funções para chamar   
    def getStreet(self):
        return self.street
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state

    def getMedTemp(self):
        return self.medTemp
    
    def getMedRad(self):
        return self.medRad

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getAngle(self):
        return self.angle
    