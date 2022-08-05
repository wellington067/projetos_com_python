"""
Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. 
A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo 
dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.
"""


import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media


df.loc[df["media"] >=7 and df["faltas"] <=5, "situaçao"]= "aprovado"
df.loc[df["media"] <7 or df["faltas"] >5, "situaçao"]= "reprovado"


maior_faltas = df["faltas"].max()
print("O maior número de faltas: " + str(maior_faltas))

media_geral = df["media"].median()
print("A media das notas dos alunos foi: " + str(media_geral))

maior_media = df["media"].max()
print("A maior maior media foi: " + str(maior_media))

pd.to_csv()
