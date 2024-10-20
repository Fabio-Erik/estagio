import requests

# URL da API para jogos futuros
url = "https://api.football-data.org/v4/matches?status=SCHEDULED"  # Endpoint para jogos futuros
headers = {
    'X-Auth-Token': 'c602ea819c7e4cf786be4b45c67b42ef'  # Sua chave de API
}

# Fazer a requisição para a API
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Acesso bem-sucedido!")
    data = response.json()  # Converter a resposta para JSON
    jogos_futuros = data['matches']  # Acessar a lista de jogos futuros
    
    # Exibir os dados coletados
    for jogo in jogos_futuros:
        time_a = jogo['homeTeam']['name']  # Nome do time da casa
        time_b = jogo['awayTeam']['name']  # Nome do time visitante
        data_jogo = jogo['utcDate']  # Data do jogo
        estadio = jogo['venue']['name'] if 'venue' in jogo else 'Desconhecido'  # Nome do estádio
        
        print(f"Próximo Jogo: {time_a} vs {time_b} | Data: {data_jogo} | Estádio: {estadio}")
else:
    print("Erro ao acessar a API:", response.status_code, response.text)
