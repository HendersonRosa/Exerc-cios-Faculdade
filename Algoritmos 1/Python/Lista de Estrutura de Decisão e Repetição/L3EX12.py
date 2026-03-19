print('Bem vindo ao banco de doação de sangue, informe seus dados: ')

i = int(input('Informe sua idade: '))
p = float(input('Informe seu peso: '))

if i > 0 and p > 0:
	if 16 <= i <= 69 and p >= 50:
		print('doação permitida')
	else: 
		print('doação não permitida')
else:
	print('Informe dados válidos')
