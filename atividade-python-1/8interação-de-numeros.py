# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

print('Digite numeros, para encerra o programa digite 0')
a=1 #numero que sera digitado
maior=0 #lugar do maior numero da interação
qtd=0 # pra saber se estou na primeira interação
while a != 0:
    a = int(input('Valor: ')) #pega o valor ja no int
    qtd +=1 #pra colocar a condição de primeira interação do laço
    if qtd == 1: #checa se estou na primeira interação
        maior = qtd = a #joga o valor digitado no input pra maior e qtd
    else: # se não for a primeira interação faz o checar normal
        if a > maior: #checa se o que eu tenho e menor que o que o usuario digitou e armazeno se for menor
            maior = a
print(maior)# no final do programa printo o maior valor quando digita-se 0
