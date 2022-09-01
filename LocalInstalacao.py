import numpy as np

class LocalInstalacao:
    def __init__(self, roofAngle = np.array([]), area = np.array([])):
        self.roofAngle = roofAngle
        self.area = area

    # Funções para modificar   
    def setRoofAngle(self, roofAngle):
        self.roofAngle = roofAngle
    
    def setArea(self, area):
        self.area = area

    #Funções para chamar  
    def getRoofAngle(self):
        return self.roofAngle
    
    def getArea(self):
        return self.area