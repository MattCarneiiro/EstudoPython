a = None
vetor = [0] * 6
vetor2 = [0]*6
#Loop de contagem de votos
while a !=0:
    print('Escolha uma das opções: ')
    print('1- Windows Server')
    print('2- Unix')
    print('3- Linux')
    print('4- Netware')
    print('5- Mac OS')
    print('6- Outro')
    
    b = int(input(""))
    if b== 1:
        vetor[0]+= 1
    elif b==2:
        vetor[1]+= 1
    elif b == 3:
        vetor[2]+= 1
    elif b == 4:
        vetor[3]+= 1    
    elif b == 5:
        vetor[4]+= 1
    elif b == 6:
        vetor[5]+= 1
    elif b==0:
        a= b
    else:
        print('Opção invalida! ')

# Loop para saber a porcentagem de cada um
total = sum(vetor)
c = 0
for n in vetor2:
    vetor2[c]= ((vetor[c]/total)*100)
    c +=1
c = 0
print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')
print('Windows Server           '+ str(vetor[0])+ '   '+ str(vetor2[0])+'')
print('Unix                     '+ str(vetor[1])+ '   '+ str(vetor2[1])+'')
print('Linux                    '+ str(vetor[2])+ '   '+ str(vetor2[2])+'')
print('Netware                  '+ str(vetor[3])+ '   '+ str(vetor2[3])+'')
print('Mac OS                   '+ str(vetor[4])+ '   '+ str(vetor2[4])+'')
print('Outro                    '+ str(vetor[5])+ '   '+ str(vetor2[5])+'')
print('-------------------     -----')
print('Total                    '+str(total)+ '')

# Exemplo de inicialização dos vetores (substitua pelos seus dados reais)
vetor3 = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS"]

maior = vetor[0]  # Assume que o primeiro elemento é o maior inicialmente

for c in range(len(vetor) - 1):
    if vetor[c + 1] > maior:
        maior = vetor[c + 1]

# Encontrar o sistema operacional mais votado
indice_maior = vetor.index(maior)

# Imprimir o resultado
print(f'O Sistema Operacional mais votado foi o {vetor3[indice_maior]}, com {maior} votos.')
