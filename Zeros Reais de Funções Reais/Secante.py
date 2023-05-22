
class Secante():
    def __init__(self, func, chute1, chute2, precisao):
        self.func = func
        
        self.x_ant1 = chute1
        self.x_ant2 = chute2

        self.precisao = precisao

        self.iteracoes = 2

    
    def calc_prox(self): # Retorna se é para parar ou não
        self.x = (self.x_ant1 * self.func(self.x_ant2) - self.x_ant2 * self.func(self.x_ant1)) / (self.func(self.x_ant2) - self.func(self.x_ant1))

        if abs(self.x - self.x_ant2) <= self.precisao:
            return True


        self.x_ant1, self.x_ant2 = self.x_ant2, self.x
        
        return False


    def resolver(self):

        while True:
            opt = self.calc_prox()

            print("x({}) = {}".format(self.iteracoes, self.x))

            self.iteracoes += 1

            if opt:
                break

        print("Resultado = {}".format(self.x))
