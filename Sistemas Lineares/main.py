from ElimGaussiana import ElimGaussiana
from GaussJacobi import GaussJacobi
from GaussSeidel import GaussSeidel
from matrizes_exemplos import *


#Eliminação Gaussiana
#Não implementadas outras tecnicas de pivoteamento
#eg = ElimGaussiana(matriz_ex3, "parcial", truncar=4)
#eg.resolver()


#Gauss-Jacobi
#Criterio de parada "absoluto" ou "relativo"
#gj = GaussJacobi(matriz_ex4, [0.1, 0.1, 0.1], 0.01, crit_parada="absoluto", truncar=4)
#gj.resolver()


#Gauss-Seidel
#Criterio de parada "absoluto" ou "relativo"
#matriz1[1], matriz1[2] = matriz1[2], matriz1[1]
gs = GaussSeidel(matriz_ex7, [0, 0, 0], 0.01, crit_parada="relativo", truncar=4)
gs.resolver()