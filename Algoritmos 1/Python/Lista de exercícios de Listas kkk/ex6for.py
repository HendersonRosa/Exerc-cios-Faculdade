m = str(input('Informe 10 manchetes:'))
l = m.split(',')
print('As manchetes do dia são:',m)
t = len(l)
if t != 10:
    print('Informe 10 manchetes')
else:
    print('Foram contabilizadas',t,'manchetes')
o1 = l[7:10]
o2 = l[0:3]
o3 = l[3:7]
nova_lista = [o1,o2,o3]
print('A nova lista ficou:',nova_lista)
