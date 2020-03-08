import pandas as pd
import matplotlib.pyplot as plt

# Importando e abrindo o arquivo

csv = open("C:\\Users\\agaab\\Desktop\\Python\\Dados\\dados_comercio_wits.csv", "r")

dataframe = pd.read_csv(csv)

# Definindo funções relevantes

def mktShare(regiao):
    j = 0
    ano = 0
    market_shares_anuais = []
    for i in dataframe['ReporterISO3']:
        j += 1
        if dataframe['ReporterISO3'][j-1] == regiao:
            if dataframe['PartnerISO3'][j-1] == 'All':
                market_share = (dataframe['total'][j-1])/(dataframe['total'][ano])
                market_shares_anuais.append(market_share)
                ano += 1
    return market_shares_anuais

def vantagensComp(regiao):
    j = 0
    ano = 0
    indices_anuais = []
    for i in dataframe['ReporterISO3']:
        j += 1        
        if dataframe['ReporterISO3'][j-1] == regiao:
            if dataframe['PartnerISO3'][j-1] == 'All':
                ind_vant_comp = (dataframe['industria'][j-1]/dataframe['industria'][ano])/(dataframe['total'][j-1]/dataframe['total'][ano])
                indices_anuais.append(ind_vant_comp)
                ano += 1
    return indices_anuais

# Definindo variáveis relevantes

dados_industria_mer = list(dataframe['industria'][103:120])
dados_totais_mer = list(dataframe['total'][103:120])
dados_industria_eu = list(dataframe['industria'][52:69])
dados_totais_eu = list(dataframe['total'][52:69])
anos = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
share_mer = mktShare('Mercosul')
share_eu = mktShare('EU27')
indice_vantagens_comparativas_mer = vantagensComp('Mercosul')
indice_vantagens_comparativas_eu = vantagensComp('EU27')

# Figuras 1 e 2, evolução das exportações industriais e totais do MERCOSUL

plt.figure(1, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, dados_industria_mer)
plt.ylabel('Volume de exportações, em centenas de bilhões de dólares nominais')
plt.xlabel('Ano')
plt.suptitle('Exportações industriais do MERCOSUL de 2002 a 2018')

plt.figure(2, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, dados_totais_mer)
plt.ylabel('Volume de exportações, em centenas de bilhões de dólares nominais')
plt.xlabel('Ano')
plt.suptitle('Exportações totais do MERCOSUL de 2002 a 2018')

# Figura 3 e 4, evolução das exportações industriais e totais da UE

plt.figure(3, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, dados_industria_eu)
plt.ylabel('Volume de exportações, em centenas de bilhões de dólares nominais')
plt.xlabel('Ano')
plt.suptitle('Exportações industriais da União Européia de 2002 a 2018')

plt.figure(4, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, dados_totais_eu)
plt.ylabel('Volume de exportações, em centenas de bilhões de dólares nominais')
plt.xlabel('Ano')
plt.suptitle('Exportações totais da União Européia de 2002 a 2018')

# Figuras 5 e 6, evolução dos market shares do MERCOSUL e UE nas exportações mundiais

plt.figure(5, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, share_mer)
plt.ylabel('Market share')
plt.xlabel('Ano')
plt.suptitle('Fatia de mercado das exportações do MERCOSUL ao longo do tempo')

plt.figure(6, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, share_eu)
plt.ylabel('Market share')
plt.xlabel('Ano')
plt.suptitle('Fatia de mercado das exportações da União Européia ao longo do tempo')

# Figuras 7 e 8: evolução dos índice de vantagens comparativas do MERCOSUL e UE

plt.figure(7, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, indice_vantagens_comparativas_mer)
plt.ylabel('Índice')
plt.xlabel('Ano')
plt.suptitle('Índice de vantagens comparativas para a indústria do MERCOSUL')

plt.figure(8, figsize = (10, 5))
plt.subplot(111)
plt.plot(anos, indice_vantagens_comparativas_eu)
plt.ylabel('Índice')
plt.xlabel('Ano')
plt.suptitle('Índice de vantagens comparativas para a indústria da UE')

# Exibindo os gráficos

plt.show()

#def valorPresenteFluxo(regiao1, regiao2):
#    j = 0
#    industria_total = 0
#    total = 0
#    for i in dataframe['ReporterISO3']:
#        j += 1
#        if dataframe['ReporterISO3'][j-1] == regiao1:
#            if dataframe['PartnerISO3'][j-1] == regiao2:
#                industria_total = industria_total + dataframe['industria'][j-1]*(1/(1+inflação**(17-(j-1))))
#                total = total + dataframe['total'][j-1]*(1/(1+inflação**(17-(j-1)))) # buscar série temporal de inflação depois
#    return industria_total, total
#
#contar(regiao1 = 'Mercosul', regiao2 = 'All')