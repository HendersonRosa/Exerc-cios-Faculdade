u = int(input('Insira a umidade do ar: '))
if u > 0 and u <= 100:
 c = int(input('Insira a chance de chuva: '))
else: 
 print('Digite o valor correto')
 
if c > 0 and c <= 100:
 if u <= 30 and c< 20:
  print('Sistema de irrigação ativada')
 else:
  print('Monitorando')
else: 
 print('Digite o valor correto')


