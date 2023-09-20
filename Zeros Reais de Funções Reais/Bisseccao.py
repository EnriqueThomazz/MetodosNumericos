def Bisseccao(func, a, b, precisao):

    c = 0 # Apenas para proposito de exibicao dos resultados
    while (b - a >= precisao):
        print("\nIntervalo {}: [{}, {}]".format(c, a, b))
        c += 1

        x_medio = (a+b)/2 # Calculando ponto medio

        print("Ponto médio: {}".format(x_medio))
        
        func_a = func(a) # Calculando f(a)
        func_b = func(b) # Calculando f(b)

        func_xm = func(x_medio) # Calculando f(x_medio)

        if (func_xm > 0 and func_a > 0) or (func_xm <= 0 and func_a <= 0): # Se tiver o mesmo sinal que f(a)
            a = x_medio
            print("Descartando o a...")
        elif (func_xm > 0 and func_b > 0) or (func_xm <= 0 and func_b <= 0): # Se tiver o mesmo sinal que f(b)
            b = x_medio
            print("Descartando o b...")

    print("\nResposta: {}".format((a+b)/2)) # Retorna o ponto médio do intervalo de saída
