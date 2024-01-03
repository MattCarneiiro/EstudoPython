#Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def perguntavalorehora():
    valor= int(input('Qual seu valor por hora trabalhada? '))
    horas= int(input('Quantas horas vc trabalha por mes? '))
    resultado = valor*horas # variavel local, nao pode ser usada diretamente pra fora da função
    return resultado # retornando a VALOR ARMAZENADO na variavel resultado

resultado= perguntavalorehora() # passando o valor retornado para a variavel resultado

print('Você ganha '+ str(resultado) + ' reais por mês')