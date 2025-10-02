import pyodbc
import pandas as pd

dados_conexao=('driver={sqlite3 odbc driver};server=localhost;database=banco de dados teste/chinook.db')

conexao=pyodbc.connect(dados_conexao)

cursor=conexao.cursor()

#cursor.execute('select * from artists')
#resultado=cursor.fetchall()
#print(resultado[:10])

cursor.execute('select * from artists') # lendo a tabela artists do banco de dados
resultado2=cursor.fetchall() # buscando os dados da consulta ao banco de dados e armazenar os dados na variavel "resultado2" na forma de uma lista de tuplas
descricao=cursor.description # pegando os nomes das colunas existentes na tabela "artists" onde foi realizada a consulta
colunas=[tupla[0] for tupla in descricao] #percorrendo a tupla para pegar apenas os nomes das colunas, que estao no indice 0 de cada tupla da variavel "descrição"


tabela=pd.DataFrame.from_records(resultado2,columns=colunas) 
print(tabela[:10])

cursor.close()
conexao.close()
