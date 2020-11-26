# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 5


import statistics as s
x=[4.0,4.5,5.0,5.5,6.0,6.0,6.5,6.5,6.5,6.5,7.0,7.0,7.0,7.0,7.0,7.0,7.5,8.5,9.0,9.0,9.0,9.5,10.0,10.0,10.5,11.0,12.0,12.5,13.0,13.0] #lista
cv = (s.stdev(x) / len(x)) * 100 #calculo coeficiente
print(f'Coeficiente de Variação: {cv:.1f}%') #mostra coeficiente formatado