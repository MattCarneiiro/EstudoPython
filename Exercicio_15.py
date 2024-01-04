# Teste de passar um vetor para outro invertido
a= 0
b = 9
lista = [1,2,3,4,5,6,7,8,9,10]
teste = [10,9,8,7,6,5,4,3,2,1]
inverso = []
for n in lista:
    inverso.append(a)
    inverso[a]= lista[b]
    a = a + 1
    b= b -1
print(inverso)


#imprimindo na ordem inversa
c = 9
for n in lista:
    print(lista[c])
    c = c-1
