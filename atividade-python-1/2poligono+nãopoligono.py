# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 4

l = int(input('Digite o número de lados do polígono:'))  #le quantos lados pedidos 
m = float(input('Digite a medida do lado do polígono:')) #le a medida do lado
if l == 3:  #condição 3 lados
    area = m ** 2 * 3 ** (1/2) / 4  #calcula a area do triangulo considerando ele equilatero
    print('Triângulo') 
    print(area)
elif l == 4:  #condição 4 lados
    print('Quadrado')
    area = m ** 2  #calcula a area do quadrado
    print(area)
elif l == 5:  #condição 5 lados
    print('Pentágono')
elif l < 3:   #condição -3 lados
    print('NÃO É UM POLÍGONO')
elif l > 5:   #condição +5 lados
    print('POLÍGONO NÃO INDENTIFICADO')