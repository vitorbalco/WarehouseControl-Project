from .repository import load_data, save_data, ARQUIVO_USUARIOS

def register_user(user, password):
    users = load_data(ARQUIVO_USUARIOS)
    
    # Se o arquivo não existia e o load_data devolveu uma lista ou nada, 
    # nós forçamos ele a virar um dicionário vazio.
    if not isinstance(users, dict):
        users = {}
        
    if user in users:
        return False
        
    users[user] = password
    save_data(ARQUIVO_USUARIOS, users)
    return True

def authenticate_user(user, password):
    """
    Valida as credenciais comparando com o banco JSON.
    """
    users = load_data(ARQUIVO_USUARIOS)
    return user in users and users[user] == password