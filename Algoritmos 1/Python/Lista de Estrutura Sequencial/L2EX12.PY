p = float(input('Insira as polegadas: '))
cm = p*2.54
tb = int(cm/100-1.5)
s = (cm/100-1.5)*100
print('Centímetros:',cm,'|Tábuas completas:',tb,'|Sobra:',s)
