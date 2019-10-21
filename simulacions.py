import numpy as np
import matplotlib.pyplot as plt

'''
def Int(dX):
    n = len(dX)
    X = [0 for i in range(n+1)]
    for i in range(n+1):
        X[i+1] = X[i] + dX[i]
    return X
'''
# constates de "resolución"
h = 0.001
r = 10

#  constantes "conocidas"
E = 0.0002
B = 0.3
C = 10.0
mu = 3
F = 0

f = lambda t_1, lbd: E*t_1*lbd**6 - B*(lbd-lbd**(-5))
g = lambda t_1: t_1**(-1/2)
#print(f(4.,5.))
#print(g(1/4))

D = [0 for j in range(r)]
for j in range(2,r):
    lbd_1 = np.power(j, 1/3)
    print(lbd_1)

    # Euler to find $T_1(\lambda)$
    LBD = np.arange(lbd_1, 1, -h)
    n = len(LBD)
    LBD = np.append(LBD, [1.0])
    #print(LBD)
    dLBD = [LBD[i+1]-LBD[i] for i in range(n)]
    dT_1 = [0 for i in range(n)]
    T_1 = [0 for i in range(n+1)]
    T_1[0] = 0
    for i in range(n):
        dT_1[i] = f(T_1[i], LBD[i]) * dLBD[i]
        T_1[i+1] = T_1[i] + dT_1[i]
    #dT_1[n-1] = f(T_1[n-1], LBD[n-1])*dLBD[n-1]
    '''
    plt.plot(LBD, T_1, label="$T_1(\lambda)$")
    plt.xlabel("$\lambda$")
    plt.ylabel("$T_1$")
    plt.title("First plot")
    plt.legend()
    plt.savefig("T_1-lbd.png")
    plt.show()
    '''

    # Euler to find $t(\lambda)$
    T = [0 for i in range(n+1)]
    dT = [0 for i in range(n)]
    dT[0] = h
    T[1] = T[0] + dT[0]
    for i in range(1,n):
        dT[i] = -g(T_1[i])*dLBD[i]
        T[i+1] = T[i] + dT[i]
    #dT[n-1] = g(T_1[n-1])*dLBD[n-1]
    
    plt.plot(T, LBD, label="$\lambda(t)$")
    plt.xlabel("$t$")
    plt.ylabel("$\lambda$")
    plt.title("Desinflado de un globo para $\lambda_1=$" + str(lbd_1))
    plt.legend()
    plt.savefig("lbd-t.png")
    plt.show()
    

    # Integrate to find $v(t)$
    A = [C * LBD[i]**4 * T_1[i] for i in range(n)]
    dV = [0 for i in range(n)]
    V = [0 for i in range(n+1)]
    for i in range(n):
        dV[i] = (A[i] - mu*V[i])*dT[i]
        V[i+1] = V[i] + dV[i]
    #T.append(T[n-1] + dT[n-1])
    i = n
    F = mu*V[n]
    while V[i]>0:
        #print(V[i])
        dT.append(h)
        T.append(T[i] + dT[i])
        dV.append(-(mu*V[i]+F)*dT[i]/2)
        V.append(V[i] + dV[i])
        i += 1
    dT.append(h)
    '''
    plt.plot(T, V, label="$v(t)$")
    plt.xlabel("$t$")
    plt.ylabel("$v$")
    plt.title("Third plot")
    plt.legend()
    plt.savefig("v-t.png")
    plt.show()
    '''

    # Integrate to find $x(t)$
    m = len(T)
    dX = [0 for i in range(m)]
    X = [0 for i in range(m+1)]
    #print(m, len(dT))
    for i in range(m):
        dX[i] = V[i]*dT[i]
        X[i+1] = X[i] + dX[i]
    T.append(T[m-1] + dT[m-1])
    '''
    plt.plot(T, X, label="$x(t)$")
    plt.xlabel("$t$")
    plt.ylabel("$x$")
    plt.title("Gráfica del movimiento teóirico del coche")
    plt.legend()
    plt.savefig("x-t.png")
    plt.show()
    '''

    D[j] = X[m]
    print(D[j])

plt.plot(D[1:], label="$d(V)$")
plt.xlabel("$n$")
plt.ylabel("$d$")
plt.title("Predicción teórica de los resultados experimentales")
plt.legend()
plt.savefig("d-n.png")
plt.show()
