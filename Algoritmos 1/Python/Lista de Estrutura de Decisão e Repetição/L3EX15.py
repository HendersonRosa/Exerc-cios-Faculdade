cm = float(input('informe seu consumo de energia: '))
tb = 1.20
if cm > 0:
	if cm < 100:
		tr = cm*(tb*0.90)
		print('Tarifa reduzida em 10 por cento, então ficou:', tr)
	elif 100 <= cm <= 200:
		tn = cm * tb
		print('Tarifa normal, então ficou:', tn)
	else: 
		ta = cm * (tb * 1.20)
		print('Tarifa com acréscimo de 20 por cento, , então ficou:', ta)
else:
	print('Informe valores válidos')
