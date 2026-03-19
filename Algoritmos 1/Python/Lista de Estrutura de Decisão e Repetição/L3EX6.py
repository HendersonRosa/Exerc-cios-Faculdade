nu = int(input('Insira a primeira nota: '))
nd= int(input('Insira a segunda nota: '))
nt = int(input('Insira a terceira nota: '))
r = int(input('Insira a renda familiar: '))
m = (nu+nd+nt)//3
print('A média do aluno foi de:',m)

if m >= 8 and r < 2500:
	print('Aluno recebe bolsa integral')
elif m >= 7 and r < 4000:
	print('Aluno recebe meia bolsa')
else:
	print('Aluno não foi contemplado')
