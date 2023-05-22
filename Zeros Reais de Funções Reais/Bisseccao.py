
class Bisseccao():
    def __init__(self, func, intervalo, precisao):
        self.func = func
        self.intervalo = intervalo
        self.precisao = precisao

        self.iteracoes = 1


    def calc_intervalo(self):
        f_a = self.func(self.intervalo[0])
        f_b = self.func(self.intervalo[1])

        meio = (self.intervalo[0] + self.intervalo[1]) / 2

        f_meio = self.func(meio)

        #Substituindo no novo intervalo
        if (f_meio < 0 and f_b < 0) or (f_meio >= 0 and f_b >= 0):
            self.intervalo[1] = meio
        
        elif (f_meio < 0 and f_a < 0) or (f_meio >= 0 and f_a >= 0):
            self.intervalo[0] = meio


    def verif_parada(self):
        if(self.intervalo[1] - self.intervalo[0] <= self.precisao): #Se o tamanho do intervalo é menor do que a precisao
            return True
        
        return False


    def resolver(self):
        print(self.verif_parada)
        while not self.verif_parada():
            self.calc_intervalo()
            print("Intervalo {} = {}".format(self.iteracoes, self.intervalo))

            self.iteracoes += 1

        print("Resultado: {}".format((self.intervalo[0] + self.intervalo[1])/2))
        return (self.intervalo[0] + self.intervalo[1])/2

