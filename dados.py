import matplotlib.pyplot as plt
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('futebol.db')
cursor = conn.cursor()

# Consulta
cursor.execute("SELECT nome, gols FROM jogadores")
dados = cursor.fetchall()

# Separar nomes e gols
nomes = [linha[0] for linha in dados]
gols = [linha[1] for linha in dados]

# Criar gráfico
plt.bar(nomes, gols)
plt.title('Gols por Jogador')
plt.xlabel('Jogadores')
plt.ylabel('Gols')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
