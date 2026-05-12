USERS = {
    'vitor': '1234',
    'admin': 'admin'
}

def login():
    """
    Gerencia o fluxo de autenticação via CLI.
    Implementa bloqueio após 3 tentativas falhas para mitigar ataques de força bruta.
    Retorna o username em caso de sucesso, ou None se falhar.
    """
    print("=== SISTEMA DE CONTROLE DE ALMOXARIFADO ===")
    attempts = 3
    
    while attempts > 0:
        user = input("Usuário: ").strip().lower()
        password = input("Senha: ").strip()
        
        # Busca no dicionário em O(1) para validar credenciais
        if user in USERS and USERS[user] == password:
            print(f"\n✅ Acesso liberado. Usuário responsável: {user.capitalize()}")
            return user
        
        attempts -= 1
        print(f"❌ Credenciais inválidas. Você tem mais {attempts} tentativa(s).")
    
    print("⚠️ Acesso bloqueado por segurança.")
    return None