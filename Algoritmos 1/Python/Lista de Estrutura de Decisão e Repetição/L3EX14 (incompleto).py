l_1 = float(input('Informe lado 1: '))
l_2 = float(input('Informe lado 2: '))
l_3 = float(input('Informe lado 3: '))

if l_1 == l_2 == l_3:
	print('triângulo equilátero')
elif l_1 != l_2 or l_2 != l_3:
	print('triângulo isósceles')
elif l_1 != l_2 != l_3:
	print('triângulo escaleno')
