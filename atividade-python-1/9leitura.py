# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

x=int(input('Informe um número entre 1000 e 9999: '))# pego numero
u=str(x) #transformação em string
print('O número informado foi:',x)#mostra o numero digitado
print('Unidade: {}' '\nDezena: {}' '\nCentena: {}' '\nMilhar: {}'.format(u[3], u[2], u[1], u[0]))#mostra no formato pedido separando