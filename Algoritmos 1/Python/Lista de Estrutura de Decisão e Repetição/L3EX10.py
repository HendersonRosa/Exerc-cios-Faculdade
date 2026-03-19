ca = int(input('informe quantidade de carga da bateria: '))
co = float(input('Informe o consumo: '))

if ca > 0 and co > 0:
	if ca < 20 and co > 1.5:
		print('Recarregar imediatamente')
	elif ca < 40 and co > 2.0:
		print('Recarregar daqui uma hora')
	else:
		print('Não recarregar')
else:
	print('Informe valores válidos')
