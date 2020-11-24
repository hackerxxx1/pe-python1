# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

l = int(input('Digite o número de lados do polígono:'))  #le quantos lados pedidos 
m = float(input('Digite a medida do lado do polígono:')) #le a medida do lado
if l == 3:  
    area = m ** 2 * 3 ** (1/2) / 4  #calcula a area do triangulo considerando ele equilatero
    print('Triângulo') 
    print(area)
elif l == 4:
    print('Quadrado')
    area = m ** 2  #calcula a area do quadrado
    print(area)
elif l == 5:
    print('Pentágono')