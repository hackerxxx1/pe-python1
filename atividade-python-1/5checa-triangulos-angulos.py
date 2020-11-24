# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

a = int (input('Digite o valor do primeiro ângulo: '))
b = int (input('Digite o valor do segundo ângulo: '))
c = int (input('Digite o valor do terceiro ângulo: '))
if a + b + c == 180: #checa se e um triangulo vendo a soma dos angulos
    if a == 90 or b == 90 or c == 90:  #checa se e um triangulo retangulo
        print('Triângulo Retângulo')
    elif a > 90 or b > 90 or c > 90:   #checa se e um triangulo obtusangulo
        print('Triângulo Obtusângulo')
    elif a < 90 and b < 90 and c < 90: #checa se e um triangulo acutangulo
        print('Triângulo Acutângulo ')
else:
    print('Não é um triângulo')