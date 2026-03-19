te = int(input('Informe a temperatura externa: '))
td = int(input('Informe a temperatura desejada: '))

if te < td-5:
	print('Modo máximo ativado')
elif te - td <= 5:
	print('modo econômico')
elif te >= td:
	print('aquecedor desligado')
