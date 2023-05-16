from GaussJacobi import GaussJacobi

class GaussSeidel(GaussJacobi):

    def verif_sassenfeld(self):
        betas = [None] * self.dimensao

        for i in range(self.dimensao):
            soma = 0
            for j in range(self.dimensao):
                if i != j:
                    if betas[j] != None:
                        beta = betas[j]
                    else:
                        beta = 1

                    soma += abs(self.matriz[i][j]) * beta

            betas[i] = abs(soma/self.matriz[i][i])

            print("Beta {}: {}".format(i, betas[i]))
            
            if betas[i] > 1:
                return False
            
        return True

    def iterar(self):
        for i in range(self.dimensao):
            self.aprox_atual[i] = self.matriz[i][self.dimensao] #Recebe o b da linha

            for j in range(self.dimensao):
                if j!= i:

                    if self.aprox_atual[j] != None:
                        x = self.aprox_atual[j] #Se ja tivermos o xk da iteração atual usamos ele
                    else:
                        x = self.aprox_anterior[j] #Se nao, usamos a da anterior

                    self.aprox_atual[i] -= self.matriz[i][j] * x

            self.aprox_atual[i] = self.aprox_atual[i]/self.matriz[i][i]

            if self.truncar != None:
                self.aprox_atual[i] = self.truncar_num(self.aprox_atual[i])


    def resolver(self):
        if self.verif_convergencia():
            print("CONVERGE PELO CRITERIO DAS LINHAS!")
        else:
            print("NAO CONVERGE PELO CRITERIO DAS LINHAS, VERIFICANDO SASSENFELD...")

            if self.verif_sassenfeld():
                print("CONVERGE POR SASSENFELD!")
            else:
                print("NÃO SATISFAZ O CRITERIO DAS LINHAS E NEM DE SASSENFELD!")
                return
        
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
