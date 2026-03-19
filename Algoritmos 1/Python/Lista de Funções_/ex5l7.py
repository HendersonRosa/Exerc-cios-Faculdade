def contar_pares(lista):
    c = 0 
    for num in lista:
        if num % 2 == 0:
            c += 1
    print('A lista tem',c,'números pares')

def lista():
    lista_numeros = []
    quantidade = int(input("Quantos números você quer adicionar na lista? "))
    
    for _ in range(quantidade):
        n = int(input("Informe um número: "))
        lista_numeros.append(n)
    
    contar_pares(lista_numeros)

lista()
