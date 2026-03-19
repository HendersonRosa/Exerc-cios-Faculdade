t = str(input('Informe as temperaturas registradas essa semana:'))
print('Nossa cidade registrou as seguintes temperaturas essa semana:',t)
l = t.split(',')
T = int(len(l))
if T != 7:
	print('Informe a temperatura dos 7 dias da semana')
else:
	s = l[0:3]
	print('Temperatura média dos 3 primeiros dias da semana foi de:', s)
