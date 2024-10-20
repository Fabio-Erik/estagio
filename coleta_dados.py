import requests
from bs4 import BeautifulSoup

# URL do site que contém os dados (substitua pela URL real)
url = "https://ge.globo.com/rj/futebol/brasileirao-serie-a/jogo/17-10-2024/flamengo-fluminense.ghtml"  # Altere para a URL correta

# Fazer a requisição para a página
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar os placares das partidas
    placares = soup.find_all('div', class_='sc-gVtpNI evILMu')  # Ajuste a classe se necessário
    
    # Criar uma lista para armazenar os resultados
    resultados = []
    
    for placar in placares:
        # Extrair os valores dos spans
        gols = placar.find_all('span', class_='sc-hJFzDP fusNkn')
        if len(gols) == 2:  # Verifica se encontrou dois gols
            resultado = {
                "gols_time_a": gols[0].text,
                "gols_time_b": gols[1].text,
            }
            resultados.append(resultado)

    # Exibir os dados coletados
    for resultado in resultados:
        print(f"Gols Time A: {resultado['gols_time_a']} - Gols Time B: {resultado['gols_time_b']}")
else:
    print("Erro ao acessar a página:", response.status_code)
