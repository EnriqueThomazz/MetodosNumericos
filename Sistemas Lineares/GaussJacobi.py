
class GaussJacobi():
    matriz = []
    dimensao = 0

    truncar = None

    aprox_anterior = []
    aprox_atual = []

    n_iter = 0

    precisao = 10

    crit_parada = "absoluto"

    def __init__(self, matriz, chute_inicial, precisao, crit_parada="absoluto", truncar=None):
        self.matriz = matriz
        self.dimensao = len(matriz)

        self.truncar = truncar

        self.aprox_anterior = chute_inicial
        self.aprox_atual = [None] * self.dimensao

        self.precisao = precisao

        self.crit_parada = crit_parada

    def truncar_num(self, num): #Função feia que só jesus, deve ter um modo mais inteligente de fazer isso
        d = 2

        num = str(num)
        num = list(num)

        if(num[0] == "-"):
            d+=1

        num = num[:self.truncar+d]
        num = ''.join(num)

        return float(num)


    def verif_parada(self):
        max = self.precisao
        max_x = 1
        for i in range(self.dimensao):
            d = self.aprox_atual[i] - self.aprox_anterior[i]

            if d > max:
                max = d

        if self.crit_parada != "absoluto": #Se for erro relativo
            for i in range(self.dimensao):
                if self.aprox_atual[i] > max_x:
                    max_x = self.aprox_atual[i]

        if max/max_x <= self.precisao:
            return True #Para

        return False #Não para


    def verif_convergencia(self):
        #Criterio das linhas
        for i in range(self.dimensao):
            alfa = 0

            for j in range(self.dimensao):
                if i != j:
                    alfa += abs(self.matriz[i][j])

            alfa = alfa/abs(self.matriz[i][i])

            print("Alfa {}: {}".format(i+1, alfa))

            if alfa > 1:
                return False
            
        return True



    def iterar(self):
        for i in range(self.dimensao):
            self.aprox_atual[i] = self.matriz[i][self.dimensao] #Recebe o b da linha

            for j in range(self.dimensao):
                if j!= i:
                    self.aprox_atual[i] -= self.matriz[i][j] * self.aprox_anterior[j]

            self.aprox_atual[i] = self.aprox_atual[i]/self.matriz[i][i]

            if self.truncar != None:
                self.aprox_atual[i] = self.truncar_num(self.aprox_atual[i])





    def resolver(self):
        if self.verif_convergencia():
            print("CONVERGE!")
            while True:
                self.iterar()
                self.n_iter += 1

                #Exibindo na tela
                print("{}ITERAÇÃO {}{}".format("="*40, self.n_iter, "="*40))
                print(self.aprox_atual)
                print()


                if(self.verif_parada()):
                    break

                self.aprox_anterior = self.aprox_atual
                self.aprox_atual = [None]*self.dimensao

        else:
            print("NÃO SATISFAZ O CRITÉRIO DAS LINHAS!")