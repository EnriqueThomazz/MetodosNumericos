import math
from Bisseccao import *
from Newton import *
from Secante import *
from FalsaPosicao import *

# Voce deve programar a funcao do seu problema e, se preciso, a respectiva derivada
def funcao(x):
    return math.cos(x) - x


def derivada(x):
    return -math.sin(x) - 1

#Bisseccao(funcao, -1, 1, 0.001)

#Newton(funcao, derivada, 0.5, 0.001)

Secante(funcao, 0.5, 0.6, 0.001)
