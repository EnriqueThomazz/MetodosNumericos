def ElimGaussiana(matriz):
    n_rodadas = len(matriz)-1

    # Triangularização
    for i in range(n_rodadas):
        print("Rodada {}".format(i+1))
        # Selecionar pivo pra rodada
        # Pivoteamento parcial
        index_maior = i
        for j in range(i, len(matriz)):
            if abs(matriz[j][i]) > abs(matriz[index_maior][i]): # Vendo quem é maior em módulo
                index_maior = j

        matriz[i], matriz[index_maior] = matriz[index_maior], matriz[i]

        print("Executou o pivoteamento, matriz resultante: ")
        for linha in matriz: print(linha)

        # Executando a eliminacao
        for j in range(i+1, len(matriz)):
            m = matriz[j][i]/matriz[i][i] # m <- a_kr / a_rr

            for k in range(len(matriz[j])):
                matriz[j][k] = matriz[j][k] - m * matriz[i][k] # L_k <- L_k + m * a_rk

        print("Matriz resultante após {} rodada".format(i+1))
        for linha in matriz: print(linha)

    # Substituição Regressiva
    print("Executando substituição regressiva")
    resposta = [0] * len(matriz) # inicializando vetor resposta

    for i in range(len(matriz)-1, -1, -1): # caminhando com passo negativo
        b = matriz[i][len(matriz)]

        for j in range(len(matriz)):
            if j != i:
                b -= resposta[j] * matriz[i][j]

        resposta[i] = b / matriz[i][i]

    print("Resposta: {}".format(resposta))
