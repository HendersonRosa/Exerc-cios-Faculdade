print('Simulador de frenagem, informe: ')
rm = float(input('Tempo de resposta do motorista: '))
tf = float(input('Tempo de frenagem: '))

if rm >= 0 and tf >= 0:
    if rm + tf > 6:
	    print('Reprovado')
    else:
	    print('Aprovado')
else:
    print('Informe valores válidos')
