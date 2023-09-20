def Trapezio(funcao, a, b, n):
    h = (b -a)/n

    area = 0
    for c in range(1, n+1):
        area += ( funcao(a + (c-1)*h) + funcao(a + c*h) ) * h/2

    print(area)
