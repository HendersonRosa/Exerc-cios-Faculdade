d = int(input('Insira a distância: '))
v = int(input('Insira a velocidade: '))

if d < v//2:
	print('Freios acionados')
elif v > 80 and d < v:
	print('Frenagem de emergência ativada')
else:
 print('Tudo normal')
