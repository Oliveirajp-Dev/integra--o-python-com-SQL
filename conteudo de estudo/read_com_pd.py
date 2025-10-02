import pandas as pd
import sqlite3 # biblioteca do sqlite, que ja vem com todas as configurações de integração com o sqlite

conexao=sqlite3.connect('banco de dados teste/chinook.db') # criando a conexao, esta forma de conexao so funciona se o banco de dados for um banco sqlite

tabela_artista=pd.read_sql('select * from artists', conexao)
print(tabela_artista[:10])
conexao.close() # fechando a conexão com o banco, semmpre importante para evitar que a conexão continue rodando, podendo gerar bugs 