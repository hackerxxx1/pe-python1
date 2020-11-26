# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 5

from scipy.stats.mstats import gmean
import statistics as s
x=[] #lista
t=11 #variavel para pegar p input
while t !=-999: #loop infinito, para so quando o usuario digitar -999
    while (10<t or t<0):
        t=input("Digite o valor da nota do aluno:")# pega valor
        pass
    x.append(t) #coloca valor na lista   
    pass
print("A media aritimetica é",s.mean(x)) #mostra media aritimetica
print("A media harmonica é",s.harmonic_mean(x)) #mostra media harmonica
print("A media geometrica é",gmean(x)) #mostra media geometrica
print("A moda é",s.mode(x)) #mostra a moda
print("A variancia é",s.variance(x)) #mostra a variancia
print("O desvio padrao é",s.stdev(x)) #mostra o desvio padrao
cv = (s.stdev(x) / len(x)) * 100 #calculo coeficiente
print(f'Coeficiente de Variação: {cv:.1f}%') #mostra coeficiente formatado