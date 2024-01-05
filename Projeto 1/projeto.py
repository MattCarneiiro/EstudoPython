username= []
space = []
porcent= []

def abrirarquivo(username, space):
    i = 0
    j = 0
    with open('usuarios.txt' , 'r') as arquivo:
        for linha in arquivo:
            username.append(1)
            space.append(1)
            partes = linha.strip().split('       ')
            username[i] = partes[0]
            space[j] = partes[1]
            i+=1
            j+= 1
    return (username, space)

def conversorByteMB(space):
    i = 0
    for valor in space:
        space[i] = float(space[i])/1000000
        i+=1
    return (space)

def porcentagem(space, porcent): 
    total = sum(space)
    i = 0    
    for n in space: 
        porcent.append(1)
        porcent[i] = ((space[i])/total)*100
        i+=1
    return (space, porcent)

def print_report(space, porcent):
    i = 0
    j = 1

    print("ACME Inc.           Uso do espaço em disco pelos usuários")
    print("------------------------------------------------------------------------")
    print("Nr.  Usuário        Espaço utilizado     % do uso")
    mensagem = "{}  {}        {}     {}"
    for n in space:
        print(mensagem.format(j, username[i], space[i], porcent[i]))
        i+=1
        j+=1
    print("\nEspaço total ocupado: {:.2f} MB".format(sum(space)))
    print("Espaço médio ocupado: {:.2f} MB".format(sum(space)/6))

abrirarquivo(username, space)
conversorByteMB(space)
porcentagem(space, porcent)
print_report(space, porcent)



    



