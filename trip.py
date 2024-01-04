from sys import stdin
def trip(n,m,lista):
    lista[0]+=1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    acum = 0
    for i in range(m):
        acum+= trip(n-i,m-1,lista)
    return acum

def main():
    linea = stdin.readline().strip().split()
    while linea:
        lista = [0]
        trip(int(linea[0]),int(linea[1]),lista)
        print(lista[0])
        linea = stdin.readline().strip().split()

main()
