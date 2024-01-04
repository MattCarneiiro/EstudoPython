#programa que receba a temperatura média de cada mês do ano e armazene-as em 
#uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
tempmes = [None]*12
a = 0
tempmaiores= []
for meses in tempmes:
    tempmes[a]= float(input('Qual a temperatura média desse mes? '))
    a = a+1
a = 0
b = 0
media_ano= (sum(tempmes))/12

while a<12:
    if tempmes[a]> media_ano:
        tempmaiores.append(1)
        tempmaiores[b] = a + 1
        a = a+1
        b = b+1
    else:
        a = a+1
print('Os meses que foram acima da media foram os meses ' + str(tempmaiores))

    