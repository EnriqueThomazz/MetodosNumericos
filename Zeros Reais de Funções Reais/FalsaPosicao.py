
class FalsaPosicao():
    def __init__(self, func, intervalo, precisao):
        self.func = func
        self.intervalo = intervalo
        self.precisao = precisao

        self.iteracoes = 1


    def verif_parada(self):
        if self.func(self.meio) <= self.precisao:
            return True
        
        return False
    
    def calc_prox(self):
        f_a = self.func(self.intervalo[0])
        f_b = self.func(self.intervalo[1])

        self.meio = (self.intervalo[0] * f_b - self.intervalo[1] * f_a) / (f_b - f_a)

        f_meio = self.func(self.meio)

        #Substituindo no novo intervalo
        if (f_meio < 0 and f_b < 0) or (f_meio >= 0 and f_b >= 0):
            self.intervalo[1] = self.meio
        
        elif (f_meio < 0 and f_a < 0) or (f_meio >= 0 and f_a >= 0):
            self.intervalo[0] = self.meio


    def resolver(self):

        while True:
            self.calc_prox()
            print("Intervalo {} = {}".format(self.iteracoes, self.intervalo))

            self.iteracoes += 1

            if self.verif_parada():
                break

        print("Resultado: {}".format(self.meio))
        return self.meio
