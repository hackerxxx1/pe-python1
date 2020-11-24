# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

p = int(input('Digite o primeiro valor: '))
s = int(input('Digite o segundo valor: '))
t = int(input('Digite o terceiro valor: '))
if p != s != t:  #se eles forem diferentes checa as diferenças
    if p > s and p > t:
        print('O maior valor é o primeiro: ', p)
    elif s > p and s > t:
        print('O maior valor é o segundo: ', s)
    elif t > p and t > s:
        print('O maior valor é o terceiro: ', t)
else:  #acho iguais
    print('Não pode digitar valores iguais!')
