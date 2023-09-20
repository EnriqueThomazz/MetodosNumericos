
def Lagrange(vet_x, vet_y, x):
    n_polinomio = 0 # Numero do polinomio

    p = 0 # Inicializando o polinomio final
    for c in range(len(vet_x)): 
        L = 1 # Inicializando o polinomio parcial (L0, L1, L2, ...)

        for k in range(len(vet_x)):
            if k != c: # Se o index do x que eu to vendo for diferente do grau do polinomio
                L = L * (x - vet_x[k]) / (vet_x[c] - vet_x[k]) # Calculo o termo

        p = p + (L * vet_y[c]) # Atualizo o resultado

    print(p)