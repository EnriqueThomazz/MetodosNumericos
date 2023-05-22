import math
from Bisseccao import *
from Newton import *
from Secante import *
from FalsaPosicao import *

# Voce deve programar a funcao do seu problema, junto com a respectiva derivada
def funcao(x):
    return math.cos(x) - x


def derivada(x):
    return -math.sin(x) - 1



bs = Bisseccao(funcao, [-1, 1], 0.001)
#bs.resolver()

fp = FalsaPosicao(funcao, [-1, 1], 0.001)
#fp.resolver()

nt = Newton(funcao, derivada, 0, 0.001)
#nt.resolver()

sc = Secante(funcao, 0, 0.3, 0.001)
#sc.resolver()