def Newton(funcao, derivada, chute_inicial, precisao):

    parou = False
    x_anterior = chute_inicial

    c = 1
    while not parou:
        x_atual = x_anterior - funcao(x_anterior)/derivada(x_anterior)

        print("Aproximação {}: {}".format(c, x_atual))
        c += 1

        if abs(x_atual - x_anterior) <= precisao:
            parou = True

        x_anterior = x_atual

    print(x_atual)