# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 6

import pandas as pd #importando bibliotecas
import seaborn as sn
import matplotlib.pyplot as plt
data = {'x':[12,16,18,20,28,30,40,48,50,54],
        'y':[7.2,7.4,7.0,6.5,6.6,6.7,6.0,5.6,6.0,5.5]} #conjunto com as listas dos dados a serem analisados
df = pd.DataFrame(data,columns = ['x', 'y']) #função para definir os dados e organizar como uma tab
Corr = df.corr() #função de correlação para calcular o coeficiente
print(Corr) #mostra a tab ja com o coeficiente 
sn.heatmap(Corr, annot=True) 
plt.show() #mostra depois a tab bonitinha do coeficiente

