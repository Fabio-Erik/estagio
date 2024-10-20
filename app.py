import streamlit as st
import sqlite3
import matplotlib.pyplot as plt

def get_data():
    conn = sqlite3.connect('futebol.db')  # Caminho para seu banco de dados
    query = "SELECT * FROM jogos"  # Ajuste a consulta conforme necessário
    df = conn.execute(query).fetchall()
    conn.close()
    return df

def plot_data(data):
    teams = ['Flamengo', 'Fluminense']  # Exemplo; substitua pelos dados reais
    scores = [2, 1]  # Exemplo; substitua pelos dados reais

    plt.bar(teams, scores, color=['red', 'green'])
    plt.title('Placar dos Times')
    plt.xlabel('Times')
    plt.ylabel('Placar')

    st.pyplot(plt)

def main():
    st.set_page_config(page_title="Dados dos Jogos de Futebol", layout="wide")
    st.markdown('<h1 style="color: blue;">Dados dos Jogos de Futebol</h1>', unsafe_allow_html=True)

    team_filter = st.sidebar.selectbox("Escolha um time:", ["Flamengo", "Fluminense", "Outros"])

    if st.button("Carregar Dados"):
        data = get_data()
        st.write(data)
        plot_data(data)

if __name__ == "__main__":
    main()
