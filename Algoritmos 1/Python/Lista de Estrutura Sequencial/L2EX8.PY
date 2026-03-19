print('Bem vindo a calculadora do custo de viagem')
a = float(input('Insira a distância percorrida em km: '))
b = float(input('Insira o consumo do véiculo em km/l: '))
c = float(input('Insira o preço do combustível em reais: '))
cons = a/b
print ('O consumo de combustível foi: ',cons,'L')
cust = cons * c
print ('O custo do combustível foi: ',cust,'reais')
hos = float(input('Insira o valor da hospedagem: '))
ali = float(input('Insira o valor da alimentação: '))
cusT = cust+hos+ali
print('O custo total da viagem foi de: ',cusT,'reais')


