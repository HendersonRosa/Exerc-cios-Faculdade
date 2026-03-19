tp = float(input('Insira seu tempo de prova: '))
p = float(input('Insira sua pontuação: '))

if tp <= 30 and p >= 80:
 print('Competidor vai para a final A')

elif tp >= 30 and tp <= 40 and p >= 60:
 print('Competidor vai para a final B')

else:
 print('Competidor foi para repescagem')
