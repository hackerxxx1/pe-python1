# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

p = input('Digite o valor do primeiro lado do triângulo: ')
s = input('Digite o valor do segundo lado do triângulo: ')
t = input('Digite o valor do terceiro lado do triângulo: ')
if p == s == t: #checa se os tres lados sao iguais
print('Triângulo Equilátero')
elif p == s != t or p != s == t or p == t != s: #checa se pelo menos um lado e diferente
print('Triângulo Isóceles')
else:
print('Triângulo Escaleno')