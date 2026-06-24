# 📦 Sistema de Gestão de Almoxarifado (Warehouse Management System)

Um sistema web robusto desenvolvido em Python para o controle de entrada e saída de materiais em ambientes de estoque logístico e industrial. 

O projeto nasceu com o propósito de aplicar metodologias reais de Engenharia de Software, transformando processos manuais de um almoxarifado em uma aplicação segura, rastreável e à prova de falhas de operação.

---

## 🚀 O Problema e a Solução

Em cenários industriais e administrativos, furos de estoque e a falta de rastreabilidade são problemas críticos. Este sistema resolve isso implementando regras de negócio estritas (QA) no back-end, impedindo a retirada de quantidades maiores do que o saldo físico e registrando todas as movimentações em uma trilha de auditoria (Logs).

---

## 💡 Principais Funcionalidades

*   🔐 **Gestão de Acesso (Sessão Web):** Criação de contas e sistema de login utilizando controle de estado (`session_state`), garantindo que apenas usuários registrados operem o sistema.
*   🛡️ **Trava Lógica de Consistência (Fail-Fast):** O motor do Back-end possui validação matemática em tempo real. Se um usuário tentar retirar um material com quantidade superior ao saldo, o sistema bloqueia a transação e alerta o usuário.
*   📊 **Trilha de Auditoria Imutável:** Cada movimentação (Entrada/Saída) gera um log automático registrando: Data/Hora, Produto, Quantidade, Tipo de Operação e Usuário.
*   💾 **Persistência de Dados (JSON):** Os dados de estoque, usuários e logs são salvos em arquivos `.json` estruturados, com sanitização nativa para evitar quebras de sistema (*crashes*) na leitura de arquivos vazios.

---

## 🛠️ Tecnologias e Arquitetura

O projeto foi construído seguindo os princípios de **Clean Architecture** (Arquitetura Limpa), desacoplando a interface visual das regras de negócio e da manipulação de dados.

*   **Linguagem:** Python 3
*   **Interface Web:** Streamlit
*   **Banco de Dados:** JSON (Local File System)

### 📁 Estrutura de Diretórios
*   `app.py` / `main.py`: Camada de Apresentação (Interface de Usuário).
*   `operations.py`: Camada de Regras de Negócio (Lógica, validações matemáticas).
*   `repository.py`: Camada de Dados (Leitura, sanitização e gravação dos arquivos JSON).

---

## 📈 Planejamento e Metodologia Ágil

Todo o ciclo de desenvolvimento (SDLC) foi gerenciado utilizando o framework **Scrum** com fluxos visuais no Kanban (**Trello**).

As funcionalidades foram estruturadas através de *User Stories* e os ciclos de entrega priorizaram funcionalidades de maior valor para a operação logística. A qualidade do código (QA) foi acompanhada em cada etapa, desde a arquitetura inicial até os testes de resiliência de dados.

---

## 📸 Demonstração da Aplicação

<!-- COLOQUE O LINK DO SEU GIF OU IMAGEM AQUI ABAIXO -->
![Demonstração do Sistema](https://via.placeholder.com/800x450.png?text=Insira+aqui+um+GIF+ou+Print+do+Streamlit+funcionando)

---

## 🧠 Desafios Enfrentados & Soluções

### 🧩 Persistência Segura com Arquivos JSON
*   **Desafio:** Durante os testes de escrita e leitura síncrona, arquivos JSON vazios ou corrompidos causavam *crashes* imediatos na inicialização do Streamlit.
*   **Solução:** Foi implementada uma camada de persistência (`repository.py`) com blocos de tratamento de exceções robustos e uma função de inicialização automática (sanitização), garantindo que o sistema recrie a estrutura básica de chaves vazias caso detecte falhas no arquivo.

## ⚙️ Como executar o projeto localmente

Siga os passos abaixo para rodar a aplicação na sua máquina:

1. Clone este repositório:
```bash
git clone [https://github.com/vitorbalco/Warehouse-Project.git](https://github.com/vitorbalco/Warehouse-Project.git)
```
2. Acesse a pasta do projeto:
```Bash
cd Warehouse-Project
```
3. Instale as dependências necessárias:
```Bash
pip install -r requirements.txt
```
4. Inicie a aplicação:
```Bash
streamlit run app.py
```

**Desenvolvido por Vitor Cardoso Balco | Desenvolvedor Back-end | Estudante de Sistemas de Informação**
