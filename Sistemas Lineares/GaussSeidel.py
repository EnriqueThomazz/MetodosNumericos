def GaussSeidel(matriz, chute_inicial, precisao):
    # Verificar convergencia por Sassenfeld
    print("Verificando convergencia")
    for i in range(len(matriz)):
        alfa = 0

        for j in range(len(matriz)):
            if i != j:
                alfa += abs(matriz[i][j])
        try:
            alfa = alfa/abs(matriz[i][i])
        except:
            print("Elemento nulo na diagonal principal")
            return

        print("Alfa_{}: {}".format(i, alfa))

        if alfa > 1:
            print("Não converge!")
            return
        else:
            print("Converge!")

    # Executando o método
    parou = False
    while not parou:
        aprox_atual = [None] * len(matriz) # atencao
        for i in range(len(chute_inicial)):
            aprox_atual[i] = chute_inicial[i]

        for i in range(len(matriz)):
            b = matriz[i][len(matriz)]

            for j in range(len(matriz)):
                if j != i:
                    b -= matriz[i][j] * aprox_atual[j] # assim garantimos que pegamos sempre a mais recente

            b = b/matriz[i][i]
            aprox_atual[i] = b

        # Verificando parada
        print("Aproximação {}".format(aprox_atual))
        max_dif = 0
        max_x = aprox_atual[0]
        for i in range(len(matriz)):
            dif = abs(aprox_atual[i] - chute_inicial[i])
            if dif > max_dif:
                max_dif = dif

            if abs(aprox_atual[i]) > max_x:
                max_x = abs(aprox_atual[i])

        # erro absoluto, você pode descomentar esse e comentar o relativo se quiser.
        """
        if max_dif <= precisao:
            parou = True
            print("Resposta: {}".format(aprox_atual))
        """

        # erro relativo
        if max_dif/max_x <= precisao:
            parou = True
            print("Resposta: {}".format(aprox_atual))
        
        # caso nao tenha parado
        chute_inicial = aprox_atual
