import pandas as pd 
import pandas_datareader as pdr 
import yfinance as yf 
yf.pdr_override()
import seaborn as sns
import matplotlib.pyplot as plt

acoes = ['^BVSP', 'SANB11.SA', 'BBAS3.SA', 'BBDC4.SA', 'ITUB4.SA']

ativos = pd.DataFrame()

for i in acoes:
    ativos[i] = pdr.data.get_data_yahoo(i, start = '2022-01-01')['Adj Close']

ativos.rename(columns={'^BVSP':'IBOV', 'SANB11.SA':'SANB11', 'BBAS3.SA':'BBAS3', 'BBDC4.SA':'BBDC4', 'ITUB4.SA':'ITUB4'}, inplace=True)

plt.figure()

sns.heatmap(ativos.corr(), vmin = -1, vmax = 1, annot = True, cmap = 'Blues')

plt.show()
