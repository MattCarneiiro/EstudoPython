#Por algum motivo desconhecido ele repete o input da função 2 vezes mesmo sem ter nenhum loop, não corrigi ainda(definindo a mesma função dentro do arquivo ela funciona normalmente)
from Exercicio_6 import perguntavalorehora #Treinando o import


bruto = perguntavalorehora()


inss= bruto*0.08
ir= bruto*0.11
sindicato= bruto*0.05
liquido= bruto-(inss+ir+sindicato)

print('+ Salário Bruto : R$'+ str(bruto))
print('- IR (11%) : R$'+ str(ir))
print('- INSS (8%) : R$'+ str(inss))
print('- Sindicato ( 5%) : R$'+ str(sindicato))
print('= Salário Liquido : R$'+ str(liquido))
