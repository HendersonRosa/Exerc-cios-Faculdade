print('Calculadora de juros')
a = float(input('Insira a quantidade de ações: '))
pa = float(input('Insira o preço das ações: '))

ii = a*pa
v = ii/100*15
vap = v+ii
c = ii/100*1.5
vf = vap-ii-c

print('Investimento inicial: ',ii,'| Valor após valorização: ',vap,'| Corretagem: ',c,'| Lucro líquido: ',vf) 
