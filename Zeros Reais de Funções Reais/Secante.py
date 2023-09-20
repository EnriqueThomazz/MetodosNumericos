def Secante(funcao, chute_inicial1, chute_inicial2, precisao):

    parou = False
    x_anterior_1 = chute_inicial1
    x_anterior_2 = chute_inicial2
    while not parou:
        x_atual = (x_anterior_1 * funcao(x_anterior_2) - x_anterior_2 * funcao(x_anterior_1)) / (funcao(x_anterior_2) - funcao(x_anterior_1))

        if abs(x_atual - x_anterior_2) <= precisao:
            parou = True

        x_anterior_1, x_anterior_2 = x_anterior_2, x_atual

    print(x_atual)