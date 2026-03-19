vi = float(input('Informe valor inicial do investimento:'))
t = float(input('Informe a taxa de juros:'))
m = int(input('Informe o número de meses:'))
taxa = 1 + t/100

vf = vi * (taxa*m)
print(vf,taxa)

if vf > 2*vi:
    print('ótimo retorno')

elif vf < vi:
    print('indica rentabilidade negativa')
	
