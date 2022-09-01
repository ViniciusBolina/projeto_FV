from Local import Local
from LocalInstalacao import LocalInstalacao
import numpy as np

class UC(Local, LocalInstalacao):

    def __init__(self,street, city, state, nameResp, numUC,tusd, te, dealership, typePhase, typeClass, roofAngle, area, consumption = np.array([])):

        super().__init__(street, city, state, roofAngle, area)
        self.nameResp = nameResp
        self.numUC = numUC
        self.tusd = tusd
        self.te = te
        self.dealership = dealership
        self.typePhase = typePhase
        self.typeClass = typeClass
        self.consumption = consumption

    # Funções para modificar   
    def setNameResp(self, nameResp):
        self.nameResp = nameResp
    
    def setNumUC(self, numUC):
        self.numUC = numUC

    def setTusd(self, tusd):
        self.tusd = tusd

    def setTe(self, te):
        self.te = te

    def setDealership(self, dealership):
        self.dealership = dealership
    
    def setTypePhase(self, typePhase):
        self.typePhase = typePhase
    
    def setTypeClass(self, typeClass):
        self.typeClass = typeClass

    def setConsumption(self, consumption):
        self.consumption = consumption

    #Funções para chamar    
    def getNameResp(self):
        return self.nameResp
    
    def getNumUC(self):
        return self.numUC

    def getTusd(self):
        return self.tusd

    def getTe(self):
        return self.te

    def getDealership(self):
        return self.dealership
    
    def getTypePhase(self):
        return self.typePhase
    
    def getTypeClass(self):
        return self.typeClass
            
    def getConsumption(self):
        return self.consumption