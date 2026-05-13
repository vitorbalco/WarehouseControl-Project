from .repository import load_data, save_data, register_log, ARQUIVO_ESTOQUE

def read_integer(message):
    """
    Sanitização de input: Intercepta erros de digitação (ValueError).
    Força o usuário a digitar um número válido, impedindo o crash da aplicação.
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Erro de Sistema: Por favor, insira apenas números inteiros válidos.")

def register_entry(product, quantity, user):
    """
    Handler Web: Processa entrada recebendo dados diretos da interface.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    # Proteção de QA caso o JSON não exista
    if not isinstance(inventory, dict):
        inventory = {}
        
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity
        
    save_data(ARQUIVO_ESTOQUE, inventory)
    register_log("ENTRADA", product, quantity, user)
    return True

def register_exit(product, quantity, user):
    """
    Handler Web: Valida saldo e processa saída. Devolve False se der erro.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    # Proteção de QA
    if not isinstance(inventory, dict):
        inventory = {}
        
    # Fail-fast: Bloqueia se o produto não existe ou se a quantidade pedida é maior que o saldo
    if product not in inventory or inventory[product] < quantity:
        return False 
        
    inventory[product] -= quantity
    save_data(ARQUIVO_ESTOQUE, inventory)
    register_log("SAÍDA", product, quantity, user)
    return True

def register_exit(product, quantity, user):
    """
    Handler Web: Valida saldo e processa saída. Devolve False se der erro.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    # Proteção de QA
    if not isinstance(inventory, dict):
        inventory = {}
        
    # Fail-fast: Bloqueia se o produto não existe ou se a quantidade pedida é maior que o saldo
    if product not in inventory or inventory[product] < quantity:
        return False 
        
    inventory[product] -= quantity
    save_data(ARQUIVO_ESTOQUE, inventory)
    register_log("SAÍDA", product, quantity, user)
    return True

def view_inventory():
    """
    Gera um relatório consolidado do estado atual da aplicação.
    Lê os dados formatados diretamente da base JSON.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    print("\n" + "="*40)
    print("📦 RELATÓRIO DE SALDO DE ESTOQUE")
    print("="*40)
    
    if not inventory:
        print("Nenhum produto cadastrado no momento.")
    else:
        for product, quantity in inventory.items():
            print(f"> {product.ljust(25)} | Saldo: {quantity}")
    print("="*40)