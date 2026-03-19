print('Bem vindo ao cardápio nele temos 3 itens: Açaí, Sorvete e Picolé. Os preços são:')
print('Açaí = 15, Sorvete = 10 e Picolé = 5')
c = input('código: ')
if c == 'Açaí':
 qa = int(input('quantidade'))
 ta = 15 * qa
 print('O valor total foi de: ', ta)
elif c == 'Sorvete':
 qs = int(input('quantidade'))
 ts = 10 * qs
 print('O valor total foi de: ', ts)
elif c == 'Picolé':
 qp = int(input('quantidade: '))
 tp = 5 * qp
 print('O valor total foi de: ', tp)
else:
 print('Digite o código correto')
 
 
