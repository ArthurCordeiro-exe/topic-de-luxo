from src.passageiro import Passageiro
from src.IllegalArgumentException import IllegalArgumentException


class Topic:
    def __init__(self, capacidade: int, qtdprioritarios):
        self.capacidade = capacidade
        self.qtdprioritarios = qtdprioritarios
        self.qtdnormal = self.capacidade - self.qtdprioritarios
        self.assprio = [None] * self.qtdprioritarios
        self.assnorm = [None] * self.qtdnormal

    def getNumeroAssentosPrioritarios(self):
        try:
            return len(self.assprio)
        except IllegalArgumentException as errorIae:
            print(errorIae)

    def getNumeroAssentosNormais(self):
        return len(self.assnorm)

    def getPassageiroAssentoNormal(self, lugar):
        if self.assnorm[lugar] is not None:
            return self.assnorm[lugar]
        return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if self.assprio[lugar] is not None:
            return self.assprio[lugar]
        return None

    def getVagas(self):
        vgs = 0
        for i in range(len(self.assnorm)):
            if self.assnorm[i] is None:
                vgs += 1
        for i in range(len(self.assprio)):
            if self.assprio[i] is None:
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
        for p in self.assprio + self.assnorm:
            if p is not None and p.getNome() == passageiro.getNome():
                return False

        if self.getVagas() == 0:
            return False

        if passageiro.ePrioridade():

            for i in range(len(self.assprio)):
                if self.assprio[i] is None:
                    self.assprio[i] = passageiro
                    return True

            for i in range(len(self.assnorm)):
                if self.assnorm[i] is None:
                    self.assnorm[i] = passageiro
                    return True
            return False

        else:

            for i in range(len(self.assnorm)):
                if self.assnorm[i] is None:
                    self.assnorm[i] = passageiro
                    return True

            for i in range(len(self.assprio)):
                if self.assprio[i] is None:
                    self.assprio[i] = passageiro
                    return True
            return False


    def descer(self, nome):
        for i in range(len(self.assprio)):
            if self.assprio[i] is not None and self.assprio[i].getNome() == nome:
                self.assprio[i] = None
                return True
        for i in range(len(self.assnorm)):
            if self.assnorm[i] is not None and self.assnorm[i].getNome() == nome:
                self.assnorm[i] = None
                return True
        return False


    def toString(self):
        s = "["

        for p in self.assprio:
            if p is None:
                s += "@ "
            else:
                s += "@" + p.getNome() + " "

        for p in self.assnorm:
            if p is None:
                s += "= "
            else:
                s += "=" + p.getNome() + " "

        s += "]"
        return s
