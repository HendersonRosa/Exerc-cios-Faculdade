m = int(input('Insira a quantidade de motoristas: '))
p = int(input('Insira a quantidade de passageiros: '))
dc = float(input('Insira a distância da corrida: '))
vic = float(input('Insira o valor da corrida: '))

if p > 2*m:
    print('Preço dinâmico ativado')
    vca = vic * 1.5 
    if dc > 10:
        print('Valor de acréscimo por distância')
        vad = vca * 1.2  
        print('O valor da corrida foi de:', vad)
    else:
        print('O valor da corrida foi de:', vca)
else:
     if dc > 10:
        print('Valor de acréscimo por distância')
        print('O valor da corrida foi de:', vic * 1.2)
    else:
        print('O valor da corrida foi de:', vic)
