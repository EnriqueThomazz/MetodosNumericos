from ElimGaussiana import ElimGaussiana
from GaussJacobi import GaussJacobi
from GaussSeidel import GaussSeidel

#Alguns exemplos de matrizes, comente as que nao for usar...
matriz = [[6, -2, -0.5, 1.8, 5.93],
          [-1, 0.75, 4.7, -1, 5.595],
          [1, 3.9, -0.6, 2, -0.51],
          [2, -0.3, 1, -7.2, -2.97]]
'''
matriz = [[0, 2, 2, 8],
          [1, 2, 1, 9],
          [1, 1, 1, 6]]

matriz = [[5, 1, 1, 50],
          [-1, 3, -1, 10],
          [1, 2, 10, -30]]
'''

#Eliminação Gaussiana
#eg = ElimGaussiana(matriz, "parcial", truncar=4)
#eg.resolver()


#matriz[1], matriz[2] = matriz[2], matriz[1] #Permutando linhas para que a matriz seja convergente, se voce mudar a matriz apague essa linha

#Gauss-Jacobi
#gj = GaussJacobi(matriz, [1, 1, 1, 1], 0.001, crit_parada="absoluto", truncar=4)
#gj.resolver()

#Gauss-Seidel
#gs = GaussSeidel(matriz, [1, 1, 1, 1], 0.001, crit_parada="absoluto", truncar=4)
#gs.resolver()