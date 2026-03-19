V = input("valor pago:")
vp = int(V)
int(vp)
if vp >=1000:
  d = vp * 0.10
  print('o desconto foi de:',d)
  rf = vp - d
  print('o valor final foi de:',rf)
else:
  print('o valor não recebeu desconto')
 


