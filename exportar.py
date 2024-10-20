import sqlite3
import pandas as pd

# Passo 1: Conectar ao banco de dados
conn = sqlite3.connect('futebol.db')

# Passo 2: Consultar os dados
df_jogos = pd.read_sql_query("SELECT * FROM jogos", conn)

# Passo 3: Exibir os dados
print(df_jogos)

# Passo 4: Fechar a conexão
conn.close()
