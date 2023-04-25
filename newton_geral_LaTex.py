import numpy as np


def NG(x,y,tol,N,matriz_F, matriz_invJ,tipo):
    def itr(x, y, matriz_F, matriz_invJ):
        F = np.array(eval(matriz_F))  # Digite a função aqui
        invJ = np.linalg.inv(eval(matriz_invJ)) # Digite a matriz jacobiana aqui
        return np.array([x, y]) - np.dot(invJ, F)

    delta = float('inf')

    for k in range(N):
        I0 = np.array([x, y])
        I1 = itr(*I0, matriz_F, matriz_invJ)
        delta = np.max(np.abs(I1 - I0))
        if tipo == 'LaTex':
            print(f'{k+1} & {I1} & {delta}\\\\')
        else:
            print(f'n = {k + 1}, X_n = {I1}, e_n = {delta}')
        x, y = I1
        if delta <= tol:
            break

    return print(f'A solução é {np.array([x, y])} com erro {delta}.')
print('A seguir apresentamos a iterações e erro:')


NG(1, -1,0.01, 10,
   '[x ** 2 + x * y + 2 * y ** 2 - 3, x + np.exp(y) - 2]',
   'np.array([[2 * x + y, x + 4 * y], [1, np.exp(y)]])','LaTex')