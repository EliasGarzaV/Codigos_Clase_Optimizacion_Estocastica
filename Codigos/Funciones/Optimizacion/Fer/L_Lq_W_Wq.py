def P0(lamda, mu, N):
    x = lamda / mu
    return (x - 1) / ((x ** (N + 1)) - 1)

def Pn(lamda, mu, N, n, p0):
    return ((lamda / mu) ** n) * (p0)

def Pk(lamda, mu, N):
    lst = [P0(lamda, mu, N)]
    for i in range(1, N + 1):
        lst.append(Pn(lamda, mu, N, i, lst[0]))
    return lst

# L es numero de personas en el sistema 
def L(lamda, mu, N):
    Pk_lst = Pk(lamda, mu, N)
    return sum([Pk_lst[i] * i for i in range(N + 1)])

# Lq Promedio de clientes en la fila
## s es el numero de servidores
def Lq(lamda, mu, N, s):
    Pk_lst = Pk(lamda, mu, N)
    return sum([Pk_lst[i] * (i - s) for i in range(s, N + 1)])

def E_lamda(lamda, mu, N):
    Pk_lst = Pk(lamda, mu, N)
    return sum([lamda * Pk_lst[i] for i in range(0, N)])

# W es L/ E(lamda) tiempo promedio de espera en el sistema
def W(lamda, mu, N):
    return L(lamda, mu, N) / E_lamda(lamda, mu, N)

# Wq Lq / E(lamda) tiempo promedio de espera en la fila
def Wq(lamda, mu, N, s):
    return Lq(lamda, mu, N, s) / E_lamda(lamda, mu, N)

print(L(8, 6, 4))
print(Lq(8, 6, 4, 1))
print(W(8, 6, 4)) 
print(Wq(8, 6, 4, 1))

