import pandas as pd

url = 'https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv'

dados = pd.read_csv(url)


#dados    # mostra o número de linhas e colunas (resumo)

#dados.head()    #acessa as primeiras n linhas

#dados.sample(10)   # retorna uma selecao aleatoria de linhas na quantidade escolhida

#dados.info()     # informação dos dados (str, int, etc)

#dados["Bairro"][6522]   # buscando X coluna na linha X

#dados.Bairro   # outra maneira de puxar só X coluna

#dados.Metragem.mean()   #média da coluna X que é int

#dados["Metragem"].mean()  #achando média de colunas com nomes ruins

#-------------------------
#QUANTOS IMOVEIS EU TENHO NA VILA MARIANA??

tem_imoveis_vila_mariana = (dados["Bairro"] == "Vila Mariana")        #onde tem imovel vila mariana
qtde_imoveis_vila_mariana = sum(dados["Bairro"] == "Vila Mariana")  #quantos imoveis tem na vila mariana

imoveis_vila_mariana = dados[tem_imoveis_vila_mariana]   
 
print(imoveis_vila_mariana["Metragem"].mean())