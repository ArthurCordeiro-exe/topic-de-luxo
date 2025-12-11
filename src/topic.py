from src.passageiro import Passageiro
from src.IllegalArgumentException import IllegalArgumentException


class Topic:
    def __init__(self, capacidade: int, qtdprioritarios):
        self.capacidade = capacidade
        self.qtdprioritarios = qtdprioritarios
        self.qtdnormal = self.capacidade - self.qtdprioritarios
        self.assprio = ["@"] * self.qtdprioritarios
        self.assnorm = ["="] * self.qtdnormal

    def getNumeroAssentosPrioritarios(self):
        try:
            return self.qtdprioritarios
        except IllegalArgumentException as errorIae:
            print(errorIae)

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

    def procurarPassageiro(self, nome):
        for i in range(len(self.assnorm)):
            if self.assnorm[i] == nome:
                return True
        for e in range(len(self.assprio)):
            if self.assprio[e] == nome:
                return True
        return False

            # FAZER CHECAR SE TEM ESPAÇO LIVRE NA TOPIC
    def subir(self, passageiro: Passageiro):
        if passageiro.ePrioridade():
            if not self.procurarPassageiro(passageiro.getNome()):
                for i in range(len(self.assprio)):
                    if self.assprio[i] == "@":
                        self.assprio[i] = f"@{passageiro.getNome()}"
                        return True
                for i in range(len(self.assnorm)):
                    if self.assnorm[i] == "=":
                        self.assnorm[i] = f"={passageiro.getNome()}"
                        return True
                return False
            return False
        else:
            if not self.procurarPassageiro(passageiro.getNome()):
                for i in range(len(self.assnorm)):
                    if self.assnorm[i] == "=":
                        self.assnorm[i] = f"={passageiro.getNome()}"
                        return True
                for i in range(len(self.assprio)):
                    if self.assprio[i] == "@":
                        self.assprio[i] = f"@{passageiro.getNome()}"
                        return True
                return False
            else:
                return False



    def descer(self, nome):
        for i in range(len(self.assprio)):
            if self.assprio[i] == nome:
                self.assprio[i] = "="
                return True
        for e in range(len(self.assnorm)):
            if self.assnorm[e] == nome:
                self.assnorm[e] = "="
                return True
        return False


    def toString(self):
        prio = " ".join(self.assprio)
        normal = " ".join(self.assnorm)
        return f"[{prio} {normal} ]"
