import pyodbc

print(pyodbc.drivers())
dados_conexao=(
    "driver={SQLite3 ODBC Driver};server=localhost;database=banco de dados teste/chinook.db"
)

conexao=pyodbc.connect(dados_conexao)

cursor=conexao.cursor()

cursor.execute("""
INSERT INTO albums (title,artistId)
VALUES
('flamengo', 10)
""")
cursor.commit()
cursor.close()
conexao.close() 