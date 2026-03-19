print('Bem vindo a calculadora de salário')
sb = float(input('Insira o seu salário bruto: '))
p = sb/100*11
print('Valor da previdência:',p)
sp = sb-p
ir = sp/100*15
print('Valor do IRRF:',ir)
st = sp-ir
print('Seu salário Líquido ficou de:',st)

