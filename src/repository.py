import json
import os
from datetime import datetime

# Constantes de configuração de arquivos de dados (I/O)
ARQUIVO_ESTOQUE = 'estoque.json'
ARQUIVO_LOGS = 'logs.json'
ARQUIVO_USUARIOS = 'usuarios.json'

def load_data(file_path):
    """
    Lê o JSON do disco e carrega em memória.
    Garante que o sistema não quebre se o arquivo ainda não existir,
    retornando a estrutura de dados apropriada (dict vazio ou lista vazia).
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {} if file_path == ARQUIVO_ESTOQUE else []

def save_data(file_path, data):
    """
    Persiste o estado atual dos dados no disco.
    O parâmetro indent=4 garante a legibilidade, e ensure_ascii=False 
    permite a gravação correta de acentos (ç, ã, í).
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        # Adicionamos o ensure_ascii=False aqui no final:
        json.dump(data, f, indent=4, ensure_ascii=False)

def register_log(action, product, quantity, user):
    """
    Log do tipo append-only: Adiciona um novo registro de movimentação.
    Implementa o padrão de trilha de auditoria para garantir histórico imutável.
    """
    logs = load_data(ARQUIVO_LOGS)
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    record = {
        "data": timestamp,
        "responsavel": user,
        "acao": action,
        "produto": product,
        "quantidade": quantity
    }
    
    logs.append(record)
    save_data(ARQUIVO_LOGS, logs)