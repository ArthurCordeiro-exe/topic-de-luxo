from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdprioritarios):
        self.capacidade = capacidade
        self.qtdprioritarios = qtdprioritarios
        self.qtdnormal = self.capacidade - self.qtdprioritarios
        self.assprio = ["@"] * self.qtdprioritarios
        self.assnorm = ["="] * self.qtdnormal

    def getNumeroAssentosPrioritarios(self):
        return self.qtdprioritarios

    def getNumeroAssentosNormais(self):
        return self.qtdnormal

    def getPassageiroAssentoNormal(self, lugar):
        for i in range(len(self.assnorm)):
            if self.assnorm[i] == lugar and self.assnorm[i] != "=":
                return self.assnorm[i]
            return None
        return None

    def getPassageiroAssentoPrioritario(self, lugar):
        for i in range(len(self.assnorm)):
            if self.assprio[i] == lugar and self.assprio[i] != "@":
                return self.assprio[i]
            return None
        return None

    def getVagas(self):
        vgs = 0
        for i in range(len(self.assnorm)):
            if self.assnorm[i] == "=":
                vgs += 1
        for i in range(len(self.assprio)):
            if self.assprio[i] == "@":
                vgs += 1
        return vgs

    def subir(self, passageiro: Passageiro):
        return False

    def descer(self, nome):
        return True

    def toString(self):
        return str(self.assprio + self.assnorm)
