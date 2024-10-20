import sqlite3
import matplotlib.pyplot as plt
import streamlit as st

# Conectar ao banco de dados
conn = sqlite3.connect('futebol.db')
cursor = conn.cursor()

# Consultar desempenho dos jogadores
cursor.execute("SELECT nome, gols FROM jogadores")
dados = cursor.fetchall()

# Verificar se dados foram retornados
if dados:
    # Separar nomes e gols
    nomes = [linha[0] for linha in dados]
    gols = [linha[1] for linha in dados]

    # Criar gráfico
    plt.bar(nomes, gols, color='blue')
    plt.title('Gols por Jogador')
    plt.xlabel('Jogadores')
    plt.ylabel('Gols')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibir gráfico com Streamlit
    st.title("Desempenho dos Jogadores")
    st.pyplot(plt)
else:
    st.write("Nenhum dado encontrado.")

# Fechar a conexão
conn.close()
