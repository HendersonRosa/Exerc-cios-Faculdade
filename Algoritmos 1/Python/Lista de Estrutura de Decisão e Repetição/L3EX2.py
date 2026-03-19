u = int(input('Insira a umidade do ar: '))
t = int(input('Insira a temperatura: '))
r = (100-u)+(t-25)*2

print('O risco calculado foi de:',r)

if r > 0:
    if r >= 80:
	    print('Alerta Máximo')
    elif r >= 50 and r < 80:
	    print('Alerta Moderado')
    if r < 50:
        print('Estado Normal')
else:
    print('Digite um valor correto')
