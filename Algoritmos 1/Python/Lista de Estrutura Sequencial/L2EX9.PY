print('Coloque os valores')

pf = float(input('Insira o valor da xícara de farinha: '))
pa = float(input('Insira o valor da xícara de açúcar: '))
po = float(input('Insira o valor de ovo por bolo: '))

print('Coloque as quantidades')

qb = float(input('Insira a quantidade de bolo: '))
qf = float(input('Insira a quantidade de xícaras de farinha: '))
qa = float(input('Insira a quantidade de xícaras de açúcar: '))
qo = float(input('Insira a quantidade de ovos: '))

cf = (pf*qf)*qb
ca = (pa*qa)*qb
co = (po*qo)*qb
ct = cf+ca+co

print('Farinha:',qf,'xícairas','| Açúcar:',qa,'xícairas','| Ovos:',qo,'xícairas','| Custo Total:',ct,'reais')


