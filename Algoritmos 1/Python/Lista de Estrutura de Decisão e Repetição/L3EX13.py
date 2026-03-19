md = float(input('Informe média final: '))
f = int(input('Informe a frequência: '))
fp = f/100

if md > 0 and fp >0:
	if md >= 7 and fp >= 0.75:
		print('Aprovado')
	else: 
		print('Reprovado')
else:
	print('Informe dados corretos')
