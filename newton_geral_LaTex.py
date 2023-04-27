from numpy import *


def NG(x, y, tol, N, f, Jf, tipo):
    def itr(x, y, f, Jf):
        F = array(eval(f))
        invJ = linalg.inv(eval(Jf))
        return array([x, y]) - dot(invJ, F)

    if tipo == 'LaTex':
        f_modificada = f.replace('[', '(').replace(']', ')')
        print(f'Aplique o método de Newton para obter ao menos um zero de $f(x,y) = [???,???]^{{T}} $ a partir de ' \
              f'$(x_{{0}},y_{{0}}) = [???,???]^{{T}}$. \nAdote $\delta =???$ e $N = ???$ (no máximo ??? iterações).')
        print(f'\\\\\n' \
              f'Solução: Inicialmente, devemos obter a matriz jacobiana associada a $f$. Pois bem,\n' \
              f'\\begin{{displaymath}}\n' \
              f'J_{{f}}(x,y) = \\left[\\begin{{array}}{{cc}}\n' \
              f'\\frac{{\\partial f_{{1}}}}{{\\partial{{x}}}} & \\frac{{\\partial f_{{1}}}}{{\\partial{{y}}}} \\\\\n' \
              f'\\frac{{\\partial f_{{2}}}}{{\\partial{{x}}}} & \\frac{{\\partial f_{{2}}}}{{\\partial{{y}}}} \\\\\n' \
              f'\\end{{array}}\\right] = ' \
              f'\\left[\\begin{{array}}{{cc}}\n' \
              f' ??? & ??? \\\\\n' \
              f' ??? & ??? \\\\\n' \
              f'\\end{{array}}\\right].\n'
              f'\\end{{displaymath}}')
        print(f'A seguir apresentamos as iterações e o erro com base na fórmula recursiva\n' \
              f'$$(x_{{n+1}},y_{{n+1}}) = (x_{{n}},y_{{n}}) -' \
              f' J_{{f}}^{{-1}}(x_{{n}},y_{{n}})f(x_{{n}},y_{{n}})$$\n'
              f'em sua forma matricial:')
    delta = float('inf')
    if tipo == 'LaTex':
        print('\\begin{displaymath}')
        print('\\begin{array}{ccc}')
    count = 0
    for k in range(N):
        I0 = array([x, y])
        I1 = itr(*I0, f, Jf)
        delta = max(abs(I1 - I0))
        if tipo == 'LaTex':
            if count == 0:
                print(f'n & X_{{n}} & e_{{n}}\\\\')
                count = 1
            print(f'{k + 1} & [{round(I1[0], 8)}\,\,\,{round(I1[1], 8)}]^{{T}} & {round(delta, 8)}\\\\')
        else:
            print(f'n = {k + 1}, X_{k + 1} = [{round(I1[0], 8)}  {round(I0[1], 8)}]^T, e_{k + 1} = {round(delta, 8)}')
        x, y = I1
        if delta <= tol:
            break
    if tipo == 'LaTex':
        print('\\end{array}')
        print('\\end{displaymath}')
    if tipo == 'LaTex':
        return print(f'A solução é ${array([x, y])}^{{T}}$ com erro ${round(delta, 8)}$.')
    else:
        return print(f'A solução é {array([x, y])}^T com erro {round(delta, 8)}.')


NG(-1, 1, 0.01, 10,
   '[x ** 2 + x * y + 2 * y ** 2 - 3, x + exp(y) - 2]',
   '[[2 * x + y, x + 4 * y], [1, exp(y)]]', 'LaTex')
