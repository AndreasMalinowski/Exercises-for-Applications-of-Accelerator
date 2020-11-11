import math


class Rigidity:
    c = 299792458
    e = 1.6021E-19

    def __init__(self, m0u, Ekin, type, Q):
        m0u = m0u
        self.m0kg = m0u * 1.66054E-27                              
        EkininJ = self.getEkinV(Ekin, type) * 1.6E-13                
        Erest = self.m0kg * (self.c ** 2)                         
        Etot = EkininJ + Erest                            
        Q = Q
        self.q = Q * self.e
        self.gamma = (EkininJ / Erest) + 1
        beta = math.sqrt(1 - ((1 / self.gamma) ** 2))
        self.v = beta * self.c

    def getEkinV(self, Ekin, type):
        if type == "MeV":
            return Ekin
        elif type == "AMeV":
            return Ekin * 238
        elif type == "MeV/u":
            return Ekin * 196.9665701
        elif type == "TeV":
            return Ekin * 1.0E+6
        elif type== "GeV":
            return Ekin * 1.0E+3

    def get(self):
        return (self.m0kg * self.gamma * self.v) / self.q


Uranium = Rigidity(238.050787, 90, "AMeV", 28).get()
Gold = Rigidity(196.9665701, 330, "MeV/u", 77).get()
Proton = Rigidity(1.00782503224, 7, "TeV", 1).get()
Electron = Rigidity(5.5E-4, 10, "GeV", 1).get()

print(Uranium)
print(Gold)
print(Proton)
print(Electron)