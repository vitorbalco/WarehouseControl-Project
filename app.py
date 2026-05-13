import streamlit as st
from src.authentication import authenticate_user, register_user
from src.repository import load_data, ARQUIVO_ESTOQUE
from src.operations import register_entry, register_exit

# Configuração da página
st.set_page_config(page_title="Gestão de Estoque", page_icon="📦")

# 1. INICIALIZAÇÃO DO ESTADO (Memória da sessão)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''

def login_screen():
    """Desenha a tela de Login e Cadastro"""
    st.title("📦 Sistema de Estoque Web")
    tab_login, tab_cadastro = st.tabs(["🔑 Login", "📝 Novo Cadastro"])
    
    with tab_login:
        st.subheader("Acesso ao Sistema")
        user = st.text_input("Usuário").strip().lower()
        password = st.text_input("Senha", type="password")
        
        if st.button("Entrar", type="primary"):
            if authenticate_user(user, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = user
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")

    # Lógica da Aba de Cadastro
    with tab_cadastro:
        st.subheader("Criar Nova Conta")
        new_user = st.text_input("Novo Usuário").strip().lower()
        new_password = st.text_input("Nova Senha", type="password")
        
        if st.button("Cadastrar"):
            if not new_user or not new_password:
                st.warning("⚠️ Preencha todos os campos.")
            elif register_user(new_user, new_password):
                st.success("✅ Conta criada com sucesso! Volte à aba de Login para entrar.")
            else:
                st.error("❌ Este nome de usuário já está em uso. Escolha outro.")

def main_app():
    """Tela principal exibida apenas para usuários logados"""
    # Barra lateral (Sidebar)
    with st.sidebar:
        st.markdown(f"### 👤 Usuário: {st.session_state['username'].capitalize()}")
        st.markdown("---")
        if st.button("Sair (Logout)"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ''
            st.rerun()

    st.title("📦 Painel de Controle")
    
    # Criamos abas para organizar a tela
    tab_visao, tab_entrada, tab_saida = st.tabs(["📊 Visão Geral", "📥 Entrada", "📤 Saída"])
    
    with tab_visao:
        st.subheader("Estoque Atual")
        
        # O Streamlit lê o JSON e desenha a tabela sozinho!
        estoque_atual = load_data(ARQUIVO_ESTOQUE)
        
        if estoque_atual:
            # Transformamos o dicionário para ficar mais amigável na tela
            st.table(estoque_atual)
        else:
            st.info("O estoque está vazio no momento. Vá para a aba 'Entrada' para adicionar produtos.")

    with tab_entrada:
        st.subheader("Registrar Entrada de Material")
        with st.form("form_entrada"):
            produto_in = st.text_input("Nome do Produto").strip().upper()
            qtd_in = st.number_input("Quantidade", min_value=1, step=1)
            btn_entrada = st.form_submit_button("Adicionar ao Estoque")
            
            if btn_entrada:
                if produto_in == "":
                    st.warning("⚠️ Por favor, digite o nome do produto.")
                else:
                    register_entry(produto_in, qtd_in, st.session_state['username'])
                    # st.success("...") -> Você pode manter ou tirar o success
                    st.rerun()

    with tab_saida:
        st.subheader("Registrar Saída de Material")
        with st.form("form_saida"):
            produto_out = st.text_input("Nome do Produto a retirar").strip().upper()
            qtd_out = st.number_input("Quantidade a retirar", min_value=1, step=1)
            btn_saida = st.form_submit_button("Retirar do Estoque")
            
            if btn_saida:
                if produto_out == "":
                    st.warning("⚠️ Por favor, digite o nome do produto.")
                else:
                    sucesso = register_exit(produto_out, qtd_out, st.session_state['username'])
                    if sucesso:
                        # st.success("...") -> Você pode manter ou tirar
                        st.rerun() # <-- ADICIONE ESTA LINHA AQUI
                    else:
                        st.error("❌ Erro: Saldo insuficiente ou produto não encontrado.")

# ROTEADOR: Decide qual tela mostrar baseado no status do usuário
if not st.session_state['logged_in']:
    login_screen()
else:
    main_app()