# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 5

from scipy.stats.mstats import gmean
import statistics as s
x=[67,75,63,72,77,78,81,77,80] #lista
print("A media aritimetica é",s.mean(x)) #mostra media aritimetica
print("A media harmonica é",s.harmonic_mean(x)) #mostra media harmonica
print("A media geometrica é",gmean(x)) #mostra media geometrica
print("A moda é",s.mode(x)) #mostra a moda
print("A mediana é",s.median(x)) #mostra a mediana
print("A variancia é",s.variance(x)) #mostra a variancia
print("O desvio padrao é",s.stdev(x)) #mostra o desvio padrao