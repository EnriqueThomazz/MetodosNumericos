def FalsaPosicao(func, a, b, precisao):
    c = 0
    while (b - a > precisao):
        print("Intervalo {}: [{}, {}]".format(c, a, b))
        c += 1

        func_a = func(a) # Calculando f(a)
        func_b = func(b) # Calculando f(b)

        x_medio = (a * func_b - b * func_a) / (func_b - func_a) # Calculando ponto medio
        print("x_medio = {}".format(x_medio))
        
        func_xm = func(x_medio) # Calculando f(x_medio)
        if (func_xm > 0 and func_a > 0) or (func_xm <= 0 and func_a <= 0): # Se tiver o mesmo sinal que f(a)
            a = x_medio
            print("Jogando fora o a...")
        elif (func_xm > 0 and func_b > 0) or (func_xm <= 0 and func_b <= 0): # Se tiver o mesmo sinal que f(b)
            b = x_medio
            print("Jogando fora o b...")

    print("Resposta: {}".format((a+b)/2)) # Retorna o ponto médio do intervalo de saída