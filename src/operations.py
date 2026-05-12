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

def register_entry(user):
    """
    Handler de regra de negócio: Entrada de Produto (Lógica de Upsert).
    Implementa a lógica de criação de novo item ou incremento de saldo existente.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    product = input("\n[ENTRADA] Informe o nome do produto: ").strip().upper()
    quantity = read_integer(f"Quantidade a ser adicionada de '{product}': ")
    
    # Fail-fast: Rejeita lógica de negócio inválida o mais cedo possível
    if quantity <= 0:
        print("❌ Operação cancelada: A quantidade de entrada deve ser maior que zero.")
        return

    if product in inventory:
        inventory[product] += quantity
        print(f"✅ Estoque atualizado. Saldo atual de '{product}': {inventory[product]}")
    else:
        inventory[product] = quantity
        print(f"✅ Novo item registrado: '{product}' com {quantity} unidade(s).")
        
    # Efetiva a transação salvando no disco e gerando o log
    save_data(ARQUIVO_ESTOQUE, inventory)
    register_log("ENTRADA", product, quantity, user)

def register_exit(user):
    """
    Handler de regra de negócio: Saída de Produto.
    Implementa restrições de consistência para impedir saldos negativos.
    """
    inventory = load_data(ARQUIVO_ESTOQUE)
    
    # Early return: Se não há dados processáveis, interrompe a função imediatamente
    if not inventory:
        print("\n⚠️ O estoque está vazio. Nenhuma saída pode ser processada.")
        return
        
    product = input("\n[SAÍDA] Informe o nome do produto: ").strip().upper()
    
    if product not in inventory:
        print(f"❌ Erro: O item '{product}' não foi localizado no estoque.")
        return
        
    current_balance = inventory[product]
    quantity = read_integer(f"Quantidade a retirar de '{product}' (Disponível: {current_balance}): ")
    
    # Validações de integridade do estoque
    if quantity <= 0:
        print("❌ Operação cancelada: Informe uma quantidade válida para retirada.")
    elif quantity > current_balance:
        print(f"❌ Erro de Validação: Saldo insuficiente. Tentativa de retirar {quantity}, mas há apenas {current_balance}.")
    else:
        inventory[product] -= quantity
        save_data(ARQUIVO_ESTOQUE, inventory)
        register_log("SAÍDA", product, quantity, user)
        print(f"✅ Saída processada com sucesso. Saldo remanescente de '{product}': {inventory[product]}")

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