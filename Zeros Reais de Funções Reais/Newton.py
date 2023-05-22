
class Newton():
    def __init__(self, func, derivada, chute_inicial, precisao):
        self.func = func
        self.derivada = derivada
        
        self.x_ant = chute_inicial
        
        self.precisao = precisao

        self.iteracoes = 1


    def calc_prox(self): #Retorna se é para parar ou não
        self.x = self.x_ant - self.func(self.x_ant)/self.derivada(self.x_ant)

        if (abs(self.x - self.x_ant) <= self.precisao):
            return True

        self.x_ant = self.x

        return False


    def resolver(self):

        while True:
            para = self.calc_prox()

            print("x({}) = {}".format(self.iteracoes, self.x))

            self.iteracoes += 1

            if para:
                break

        print("Resultado = {}".format(self.x))
        