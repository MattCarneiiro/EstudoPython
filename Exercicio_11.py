while True:
    user= str(input('Digite uma um nome de usuário: '))
    senha= str(input('Digite uma senha: '))
    if user != senha:
        print("Login e senha válidos! ")
        break
    else:
        print('Error: Login e senha não podem ser iguais!!')