a = int(input('Insira a distância: '))
v = int(input('Insira a velocidade de descida: '))

if a < 300 and v > 5 and v < 10:
	print('Trem de pouso ativado')

else:
    if v > 10:
        print('pouso forçado acionado')
    else:
        print('voo segue normalmente')
