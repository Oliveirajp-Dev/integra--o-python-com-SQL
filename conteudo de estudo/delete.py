import pyodbc


dados_conexao=('driver={sqlite3 odbc driver};server=localhost;database=banco de dados teste/chinook.db')
conexao=pyodbc.connect(dados_conexao)
cursor=conexao.cursor()

cursor.execute("""
 
delete from customers where CustomerId=1            
               
               """)
cursor.commit()

cursor.close()
conexao.close()