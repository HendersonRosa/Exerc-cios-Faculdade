c = float(input('Insira o comprimento: '))
l = float(input('Insira a largura: '))
pr = float(input('Insira a profundidade: '))
pe = float(input('Insira o peso: '))
cm = c*l*pr
dm = cm/1000
p = 5*pe
v = 3*dm
print('Custo volume:',v,'|Custo peso:',p,'|Frete:',p+v)

