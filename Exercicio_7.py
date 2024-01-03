#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso= float(input('Quantos quilos de peixo o senhor pescou? '))
if peso<= 50:
    print('O Senhor pescou abaixo do limite hoje, não terá que pagar multa :)')
else:
    peso= peso-50
    multa= 4*peso
    print('O senhor pescou ' + str(peso)+ ' quilos a mais do limite permitido portanto pagará ' + str(multa) + ' reais de multa')