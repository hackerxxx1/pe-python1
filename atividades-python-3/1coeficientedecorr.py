# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 6

import pandas as pd #importando bibliotecas
import seaborn as sn
import matplotlib.pyplot as plt
data = {'criança':[1,2,3,4,5,6,7,8,9,10,11,12],
        'aptmat':[60,58,73,51,54,75,48,72,75,83,62,52],
        'aptmus':[80,62,70,83,62,92,79,88,54,82,64,69]} #conjunto com as listas dos dados a serem analisados
df = pd.DataFrame(data,columns = ['criança', 'aptmat', 'aptmus']) #função para definir os dados e organizar como uma tab
Corr = df.corr() #função de correlação para calcular o coeficiente
print(Corr) #mostra a tab ja com o coeficiente
sn.heatmap(Corr, annot=True)
plt.show() #mostra depois a tab bonitinha do coeficiente

