# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

x=int(input("Digite um número entre 1 e 4: ")) #pega o numero e ja garante que e inteiro
while (x < 1 or x > 4): #checa se e 1 2 3 ou 4 se for sai direto se não for entra no while
    print('Entrada inválida, digite o número novamente')
    x=int(input("Digite um número entre 1 e 4: ")) #digitar um novo numero ate que a condição do while n seja mais satisfeita
    continue;
else:
    print('O número informado é:', x) #printa o numero que digitiou entre 1 e 4