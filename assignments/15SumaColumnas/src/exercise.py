
def matriz():
    lista = []
    fila = int(input())
    columna = int(input())
    if fila > 0 and columna > 0: 
        for i in range(fila):
            lista.append([])
            for j in range(columna):
                n = int(input())
                lista[i].append(n)
    else: 
        print('Error')
    return lista
def main():
    sumatriz = matriz()
    lista_columna = []
    if len(sumatriz) > 0:
        for i in range(len(sumatriz[0])):
            count = 0
            for j in range(len(sumatriz)):
                count += sumatriz[j][i] 
            lista_columna.append(count)
        print(lista_columna)

if __name__=='__main__':
    main()
