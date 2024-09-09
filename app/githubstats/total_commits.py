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

# Função principal para obter o total de commits de todos os repositórios de um usuário
def total_commits_usuario(usuario):
    repositorios = listar_repositorios(usuario)
    
    total_commits = 0
    for repo in repositorios:
        nome_repositorio = repo['name']
        try:
            total_commits += contar_commits(usuario, nome_repositorio)
        except requests.exceptions.HTTPError as e:
            print(f"Erro ao contar commits no repositório {nome_repositorio}: {e}")
    
    return total_commits

# Solicitar o nome de usuário do GitHub ao usuário do script
usuario = input("Digite o nome de usuário do GitHub: ")

total_commits = total_commits_usuario(usuario)
print(f'Total de commits de {usuario}: {total_commits}')
