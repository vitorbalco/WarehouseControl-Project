"""
Ponto de Entrada (Entrypoint) da Aplicação.
Atua como o 'Controller' principal, roteando as ações do usuário 
para os módulos de negócio apropriados.
"""

from src.authentication import login
from src.operations import register_entry, register_exit, view_inventory

def main():
    # Inicia o fluxo forçando a barreira de autenticação
    logged_user = login()
    
    if not logged_user:
        return

    # Loop principal da CLI (Interface de Linha de Comando)
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Registrar Nova Entrada")
        print("2. Registrar Saída de Material")
        print("3. Consultar Saldo em Estoque")
        print("4. Encerrar Sistema")
        
        choice = input("Selecione a ação desejada: ").strip()
        
        # Roteamento baseado na escolha do usuário
        if choice == '1':
            register_entry(logged_user)
        elif choice == '2':
            register_exit(logged_user)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            print("Encerrando as operações... Até breve!")
            break
        else:
            print("❌ Opção não reconhecida. Escolha um valor entre 1 e 4.")

# Garante que o main() só seja executado se este arquivo for rodado diretamente,
# protegendo contra execuções acidentais em caso de importação.
if __name__ == "__main__":
    main()