#Pergunta 4 notas e faz a média
notas= []

for n in range(4):
    numero= int(input('Digite a nota:'))
    notas.append(numero)

media= (sum(notas))/4
print('A media de notas é ' + str(media))
