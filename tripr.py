from sys import stdin
def trip(n,m,dicc):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    acum = 1
    for i in range(m):
        acum+= memo(n-i,m-1,dicc)
    return acum

def memo(n,m,dicc):
    if (n,m) in dicc:
        return dicc[(n,m)]
    dicc[(n,m)] = trip(n,m,dicc)
    return dicc[n,m]
def main():
    linea = stdin.readline().strip().split()
    dicc = {}
    while linea:
        print(trip(int(linea[0]),int(linea[1]),dicc))
        print(dicc)
        linea = stdin.readline().strip().split()

main()
