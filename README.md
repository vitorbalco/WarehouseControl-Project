# 📦 Sistema de Gestão de Estoque (CLI)

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success.svg)
![Persistence](https://img.shields.io/badge/Database-JSON-orange.svg)

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para consolidar conhecimentos avançados de Lógica de Programação, Arquitetura de Software e Desenvolvimento Backend. O foco principal é otimizar rotinas administrativas de almoxarifado, criando um fluxo de dados robusto, seguro e à prova de falhas em um ambiente de interface de linha de comando (CLI).

## 🧠 Destaques de Lógica e Arquitetura

Como este projeto prioriza a qualidade do código e padrões de mercado, os seguintes pontos foram implementados:

- **Separation of Concerns:** Código estruturado em módulos independentes (`operations.py`, `repository.py`, `authentication.py`), facilitando a manutenção.
- **Fail-Fast e Sanitização (QA):** Uso estratégico de blocos `try-except` para interceptar erros de tipagem, impedindo que o sistema sofra *crash*.
- **Trilha de Auditoria (Audit Trail):** Registro *append-only* em banco de dados local (`logs.json`), gravando data, usuário e movimentações de forma imutável.
- **Controle de Fluxo Restrito:** Lógica que impede a saída de materiais se o saldo solicitado for maior que o disponível no estoque (`estoque.json`).

## 🚀 Funcionalidades

- Autenticação de usuários com bloqueio de segurança após 3 tentativas.
- Cadastro dinâmico de novas entradas (Upsert).
- Saída de materiais com validação cíclica de consistência.
- Geração de relatório consolidado do saldo atual.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Armazenamento:** Arquivos JSON nativos (Persistência I/O)
- **Metodologia:** Scrum e versionamento via Git/GitHub
- **Paradigma:** Programação Estruturada com Modularização

## 💻 Como Executar

Certifique-se de ter o Python instalado em sua máquina.
Clone este repositório:
```bash
git clone [https://github.com/vitorbalco/WarehouseControl-Project.git](https://github.com/vitorbalco/WarehouseControl-Project.git)
```

## Acesse a pasta do projeto e execute:
```Bash
cd WarehouseControl-Project
python main.py
```
**Desenvolvido por Vitor Cardoso Balco | Desenvolvedor Back-end | Estudante de Sistemas de Informação**
