#PROJETO FINAL - SI - INSPER - LUIS GUSTAVO; THOMAZ; LAÍS
#bibliotecas importadas
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as fig

#período de análise
inicio=dt.datetime(2022,1,5)
fim=dt.datetime(2022,10,7)

#especificando a ação do Banco do Brasil

df=web.DataReader('BBAS3.SA','yahoo',inicio,fim)

#Excluindo as colunes de 'volume' e 'adj close'
df=df.drop(['Volume','Adj Close'],axis=1)
print(df)

#Calculando o Retorno
df['Retorno']=df['Close'].pct_change(1)
#Calculando o mínimo a cada 30 dias
df['Mín30']=df['Close'].rolling(window=30).min()

#Calculando o máximo a cada 30 dias
df['Max30']=df['Close'].rolling(window=30).max()
#Calculo do Estocástico
df['Estocástico']=100*((df['Close']-df['Mín30'])/(df['Max30']-df['Mín30']))
#Cálculo da Média móvel a cada 30 dias
df['Média Móvel']=df['Close'].rolling(window=30).mean()

print(df)

print('######### Estátisticas da Ação ####################')

print('ÚLTIMO DOS PREÇOS = ', df['Close'][-1:].values)
print('MAIOR PREÇO DA AÇÃO = ', df['Close'].max())
print('MENOR PREÇO DA AÇÃO = ', df['Close'].min())
print('PREÇO MÉDIO DA AÇÃO = ', df['Close'].mean())
print('MÁXIMO VALOR DE RETORNO = ', df['Retorno'].max())
print('DATA DO MÁXIMO VALOR DE RETORNO = ', df.index[df['Retorno'].argmax()])
print('MÍNIMO VALOR DE RETORNO = ', df['Retorno'].min())
print('DATA DO MÍNIMO VALOR DE RETORNO = ', df.index[df['Retorno'].argmin()])
print('VOLATILIDADE (desvio padrão pop) DOS PREÇOS = ', df['Close'].std(ddof=0))
print('VOLATILIDADE (desvio padrão pop) DOS RETORNOS = ', df['Retorno'].std(ddof=0))

#GRÁFICO FECHAMENTO E RETORNO

df.plot(y=['Close', 'Retorno'],
    title=['FECHAMENTO','RETORNO'],
    color=['orange','blue'],
    subplots=True)

#GRÁFICO FECHAMENTO E ESTOCÁSTICO
df.plot(y=['Close', 'Estocástico'],
    title=['FECHAMENTO','ESTOCÁSTICO'],
    color=['orange','purple'],
    subplots=True)

#GRÁFICO FECHAMENTO E MÉDIA MÓVEL
fig.figure()
fig.subplot()
fig.plot(df['Close'], color='orange')
fig.plot(df['Média Móvel'], color='green')
fig.title('MÉDIA MÓVEL')
fig.xticks(rotation=30)
fig.xlabel('Data')

#GRÁFICO DO RETORNO DA BBAS3
fig.figure()
fig.style.use('ggplot')
fig.subplot(121)
fig.plot(df['Retorno'], color='blue')
fig.title('RETORNO')
fig.xticks(rotation=30)
fig.xlabel('Data')

#GRÁFICO DO HISTOOGRAMA DO RETORNO DA BBAS3
fig.subplot(122)
fig.hist(df['Retorno'],bins=10, color='black')
fig.title('HISTOGRAMA DO RETORNO')
fig.xticks(rotation=30)
fig.xlabel('Classes')
fig.ylabel('Frequência')

#PERÍODO DA NOSSA ANÁLISE PARA BOXPLOT

inicio=dt.datetime(2022,9,1)
fim=dt.datetime(2022,10,1)
#especificando a ação do Banco do Brasil
df=web.DataReader('BBAS3.SA','yahoo',inicio,fim)
#Excluindo as colunes de 'volume' e 'adj close'
df=df.drop(['Volume','Adj Close'],axis=1)

#Gráfico BOXPLOT
figura,ax=fig.subplots()
ax.plot(df['Close'].values, color='orange')
df.T.boxplot()
fig.xticks(rotation=30)
fig.title('BOXPLOT DO FECHAMENTO')
fig.xlabel('Data')