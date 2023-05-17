from ElimGaussiana import ElimGaussiana
from GaussJacobi import GaussJacobi
from GaussSeidel import GaussSeidel

#Alguns exemplos de matrizes
matriz1 = [[6, -2, -0.5, 1.8, 5.93],
          [-1, 0.75, 4.7, -1, 5.595],
          [1, 3.9, -0.6, 2, -0.51],
          [2, -0.3, 1, -7.2, -2.97]]

matriz2 = [[0, 2, 2, 8],
          [1, 2, 1, 9],
          [1, 1, 1, 6]]

matriz3 = [[5, 1, 1, 50],
          [-1, 3, -1, 10],
          [1, 2, 10, -30]]

#Matrizes dos exercicios
matriz_ex1 = [[3, 1, -1, 4.7367],
              [-1, 3, 1, 2.1577],
              [2/5, -1, 3, 3.465]]

matriz_ex2 = [[0.8, -0.5, 3, 14.6],
              [-0.75, 2, -0.4, 5.725],
              [1, -1, -3, -17.3]]

matriz_ex3 = [[0.2, 3.8, -1, 18.8],
              [-9, 0, 2.7, -24.84],
              [0, -2, 1, -9.2]]

matriz_ex4 = [[4, -2, 1, 3.1],
              [1, -3, -1, 2.15],
              [2, 1, -5, -2.8]]

matriz_ex6 = [[5, 1, 1, 5],
              [3, 4, 1, 6],
              [3, 3, 6, 0]]

matriz_ex7 = [[5, 1, 2, 1],
              [1, 4, 2, 1],
              [2, 1, 4, 1]]

#Eliminação Gaussiana
#Não implementadas outras tecnicas de pivoteamento
#eg = ElimGaussiana(matriz_ex2, "parcial", truncar=4)
#eg.resolver()


#Gauss-Jacobi
#Criterio de parada "absoluto" ou "relativo"
gj = GaussJacobi(matriz_ex4, [0.1, 0.1, 0.1], 0.01, crit_parada="absoluto", truncar=4)
gj.resolver()


#Gauss-Seidel
#Criterio de parada "absoluto" ou "relativo"
#gs = GaussSeidel(matriz_ex6, [0, 0, 0], 0.01, crit_parada="absoluto", truncar=4)
#gs.resolver()