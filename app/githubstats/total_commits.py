import requests

# Função para listar todos os repositórios de um usuário com paginação
def listar_repositorios(usuario):
    repositorios = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{usuario}/repos'
        params = {'per_page': 100, 'page': page}  # Máximo de 100 repositórios por página
        response = requests.get(url, params=params)
        response.raise_for_status()
        repos = response.json()
        if not repos:  # Se não houver mais repositórios, saímos do loop
            break
        repositorios.extend(repos)
        page += 1
    return repositorios

# Função para contar todos os commits de um repositório específico com paginação
def contar_commits(usuario, repositorio):
    total_commits = 0
    page = 1
    while True:
        url = f'https://api.github.com/repos/{usuario}/{repositorio}/commits'
        params = {'per_page': 100, 'page': page}  # Máximo de 100 commits por página
        response = requests.get(url, params=params)
        response.raise_for_status()
        commits = response.json()
        if not commits:  # Se não houver mais commits, saímos do loop
            break
        total_commits += len(commits)
        page += 1
    return total_commits

# Função para obter o total de seguidores de um usuário
def total_seguidores(usuario):
    url = f'https://api.github.com/users/{usuario}'
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()
    return user_data.get('followers', 0)

# Função para obter o total de estrelas em todos os repositórios de um usuário
def total_estrelas(repositorios):
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repositorios)
    return total_stars

# Função principal para obter todas as métricas de um usuário
def obter_metricas_usuario(usuario):
    # Obter todos os repositórios do usuário
    repositorios = listar_repositorios(usuario)
    
    # Total de repositórios é o tamanho da lista de repositórios
    total_repositorios = len(repositorios)
    
    # Contar todos os commits em todos os repositórios
    total_commits = 0
    for repo in repositorios:
        nome_repositorio = repo['name']
        try:
            total_commits += contar_commits(usuario, nome_repositorio)
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao contar commits no repositório {nome_repositorio}: {e}")
    
    # Obter total de seguidores
    seguidores = total_seguidores(usuario)
    
    # Obter total de estrelas em todos os repositórios
    estrelas = total_estrelas(repositorios)
    
    return total_commits, total_repositorios, seguidores, estrelas

# Solicitar o nome de usuário do GitHub ao usuário do script
usuario = input("Digite o nome de usuário do GitHub: ")

# Obter todas as métricas do usuário
total_commits, total_repositorios, seguidores, estrelas = obter_metricas_usuario(usuario)

# Exibir as métricas obtidas
print(f'Total de commits de {usuario}: {total_commits}')
print(f'Total de repositórios de {usuario}: {total_repositorios}')
print(f'Total de seguidores de {usuario}: {seguidores}')
print(f'Total de estrelas em todos os repositórios de {usuario}: {estrelas}')
