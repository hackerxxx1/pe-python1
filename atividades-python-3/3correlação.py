# Disciplina: Probabilidade e Estatística
# Aluno: gabriel rodrigues da silva
# Lista 6

import pandas as pd #importando bibliotecas
import seaborn as sn
import matplotlib.pyplot as plt
data = {'anos':[2,3,4,5,4,6,7,8,8,10],
        'nclient':[48,50,56,52,43,60,62,58,64,72]} #conjunto com as listas dos dados a serem analisados
df = pd.DataFrame(data,columns = ['anos', 'nclient']) #função para definir os dados e organizar como uma tab
Corr = df.corr() #função de correlação para calcular o coeficiente
print(Corr) #mostra a tab ja com o coeficiente 
sn.heatmap(Corr, annot=True) 
plt.show() #mostra depois a tab bonitinha do coeficiente

#nesse caso o coeficiente tem um valor de 0.87, logo correlação forte dos dados.