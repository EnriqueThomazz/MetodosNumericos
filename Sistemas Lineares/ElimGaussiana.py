class ElimGaussiana():
    matriz = []
    dimensao = 0
    n_rodada = 0

    tec_pivoteamento = None

    truncar = None

    x = []

    escalas = []

    def __init__(self, matriz, tec_pivoteamento, truncar=None):
        self.matriz = matriz
        self.dimensao = len(matriz)

        self.tec_pivoteamento = tec_pivoteamento

        self.x = [None] * self.dimensao 

        self.truncar = truncar

        if tec_pivoteamento == "escala":
            self.escalas = [None] * self.dimensao

    def pivo_parcial(self):
        index_max = self.n_rodada

        for i in range(self.n_rodada, self.dimensao): #Iterando da linha n_rodada até o fim da matriz
            if self.matriz[i][self.n_rodada] > self.matriz[index_max][self.n_rodada]: #Se o elemento for maior do que o da diagonal principal
                index_max = i

        self.matriz[self.n_rodada], self.matriz[index_max] = self.matriz[index_max], self.matriz[self.n_rodada] #Troca as linhas

    def pivo_escala(self):
        if self.escalas[0] == None: #preenchendo a lista de escalas
            for i in range(self.dimensao):
                max = abs(self.matriz[i][0])
                for j in range(self.dimensao):
                    if abs(self.matriz[i][j]) > max: #Buscando o maior, em módulo
                        max = abs(self.matriz[i][j])

                self.escalas[i] = max


        index_max = self.n_rodada

        for i in range(self.n_rodada, self.dimensao): #Iterando da linha n_rodada até o fim da matriz
            dif = self.matriz[i][self.n_rodada] / self.escalas[i]
            
            if abs(dif) > abs(self.matriz[index_max][self.n_rodada] / self.escalas[index_max]): #Se o elemento for maior do que o da diagonal principal dividido pela escala da linha
                index_max = i

        self.matriz[self.n_rodada], self.matriz[index_max] = self.matriz[index_max], self.matriz[self.n_rodada] #Troca as linhas



        

    def truncar_num(self, num): #Função feia que só jesus, deve ter um modo mais inteligente de fazer isso
        d = 2

        num = str(num)
        num = list(num)

        if(num[0] == "-"):
            d+=1

        num = num[:self.truncar+d]
        num = ''.join(num)

        return float(num)


    def eliminar(self):
        #Pivoteamento
        if self.tec_pivoteamento == "parcial":
            self.pivo_parcial()
        elif self.tec_pivoteamento == "escala":
            self.pivo_escala()

        for i in range(self.n_rodada+1, self.dimensao): #Iterando pelas linhas a serem eliminadas
            m = self.matriz[i][self.n_rodada] / self.matriz[self.n_rodada][self.n_rodada] #Definindo nosso m

            for j in range(self.dimensao+1): #Iterando pelos elementos da linha           
                self.matriz[i][j] = self.matriz[i][j] - m * self.matriz[self.n_rodada][j] #Executando a operação

                if self.truncar != None:
                    self.matriz[i][j] = self.truncar_num(self.matriz[i][j])


    def subst_regressiva(self):
        for i in range(self.dimensao-1, -1, -1): #Iterando de tras pra frente por todas as linhas
            soma = self.matriz[i][self.dimensao] #Pegando o valor do b

            for j in range(self.dimensao): #Iterando na linha
                if j!=i: #Ignorando o elemento da diagonal principal
                    x = self.x[j]
                    if x == None:
                        x = 1

                    soma -= self.matriz[i][j] * x#Subtraindo pois jogamos para o outro lado

            soma = soma/self.matriz[i][i] #Dividindo pelo valor que estava multiplicando xk

            if self.truncar != None:
                soma = self.truncar_num(soma)

            self.x[i] = soma #Adicionando ao vetor resultado


    def resolver(self):
        for c in range(self.dimensao-1): # Se temos n variaveis teremos n-1 rodadas.

            self.eliminar() #Zerando a coluna
            self.n_rodada += 1

            #Exibindo resultado
            print("{}RODADA {}{}".format("="*40, self.n_rodada, "="*40))
            for linha in self.matriz:
                for elem in linha:
                    print(str(elem) + "\t\t", end="")

                print("\n")

            print("\n\n")

        self.subst_regressiva() #Executando a substituição regressiva

        print("Resultado: {}".format(self.x)) #Exibindo resultado
  
