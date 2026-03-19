def a():
    print('*'*10)

def b(n):
    print('*'*n)

def c(d,e):
    print(d*e)

def opções():
    print('Opção 1 faz o primeiro código\nOpção 2 faz o segundo código\nOpção 3 faz o terceiro código')

    p = int(input('Insira a opção:'))  

    if p == 1:
        a()
    elif p == 2:
        n = int(input('Número de asteriscos:'))
        if n > 0:
            b(n)
        else:
            print('Insira um valor válido de asteriscos')    
    elif p == 3:
        d = int(input('Número de asteriscos:'))
        if d > 0:
            e = (input('Número de caracteres:'))
            c(d,e)
        else:
            print('Insira um valor válido de asteriscos')
    else:
        print('Digite uma opção válida')

print('opção 1 faz o código em ordem\nOpção 2 pode escolher um único código')

o = int(input('Insira sua escolha:'))

if o == 1:
    a()
    
    n = int(input('Número de asteriscos:'))
    if n > 0:
        b(n)
    
    d = int(input('Número de asteriscos:'))
    if d > 0:
        e = (input('Número de caracteres:'))
        c(d,e)

elif o == 2:
    opções()

else:
    print('Insira uma opção correta')