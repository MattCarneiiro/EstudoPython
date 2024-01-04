#Programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    n = float(input('Digite um numero entre 0 e 10: '))
    if n > 10 or n<0:
        print('Resposta inválida!')
    else:
        print('Valor válido! ')
        break