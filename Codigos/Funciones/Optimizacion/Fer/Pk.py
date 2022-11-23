
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

print(Pk(8, 6, 4))