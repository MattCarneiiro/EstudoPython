#Calculo pra saber quando o Pais A vai passar o B em populção usando as taxas respectivas
a = 80000
b = 200000
i= 0
while b > a:
    a = a*1.03
    b = b*1.015
    i = i+1
print('O país A vai superar o país B em ' + str(i)+ ' anos ') 