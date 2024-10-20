import requests
import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('futebol.db')
cursor = conn.cursor()

# Criar uma tabela para armazenar dados dos jogos
cursor.execute('''
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY,
    time_a TEXT,
    time_b TEXT,
    data_jogo TEXT,
    estadio TEXT
)
''')

# Função para inserir dados
def inserir_jogo(time_a, time_b, data_jogo, estadio):
    cursor.execute('''
    INSERT INTO jogos (time_a, time_b, data_jogo, estadio)
    VALUES (?, ?, ?, ?)
    ''', (time_a, time_b, data_jogo, estadio))
    conn.commit()

# URL da API para jogos futuros
url = "https://api.football-data.org/v4/matches?status=SCHEDULED"
headers = {
    'X-Auth-Token': 'c602ea819c7e4cf786be4b45c67b42ef'  # Sua chave de API
}

# Fazer a requisição para a API
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converter a resposta para JSON
    jogos_futuros = data['matches']  # Acessar a lista de jogos futuros
    
    # Iterar sobre cada jogo futuro e extrair informações
    for jogo in jogos_futuros:
        time_a = jogo['homeTeam']['name']  # Nome do time da casa
        time_b = jogo['awayTeam']['name']  # Nome do time visitante
        data_jogo = jogo['utcDate']  # Data do jogo
        estadio = jogo['venue']['name'] if 'venue' in jogo else 'Desconhecido'  # Nome do estádio
        
        # Inserir dados no banco de dados
        inserir_jogo(time_a, time_b, data_jogo, estadio)
else:
    print("Erro ao acessar a API:", response.status_code, response.text)

# Fechar a conexão
conn.close()
