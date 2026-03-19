print('Bem vindo a calculadora de consumo de energia')
con = float(input('Digite o consumo mensal em kWh: '))
tar = float(input('Digite o valor por kWh: '))
conB = con * tar
print('O valor bruto foi de: ',conB)
conI = conB/100 * 18
print('O valor do imposto foi de: ',conI)
conF = conB+conI
print('O valor final foi de: ',conF)
