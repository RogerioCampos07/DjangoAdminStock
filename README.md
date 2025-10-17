# Django Admin Stock

Um sistema de gestão de estoque robusto e funcional, construído inteiramente sobre a interface de administração do Django.

## Visão Geral

O **`django-admin-stock`** oferece uma solução centralizada para o controle de produtos, fornecedores e o fluxo de estoque. A automação inteligente via `signals` garante que cada movimentação (entrada, saída ou ajuste) atualize o saldo de estoque em tempo real, proporcionando dados precisos e confiáveis.

### Principais Funcionalidades

- **Gestão de Catálogo**: Cadastro de produtos, categorias, marcas e lotes.
- **Gestão de Fornecedores**: Gerenciamento de fornecedores e seus representantes.
- **Controle de Movimentações**: Registro detalhado de todas as entradas, saídas e ajustes de estoque.
- **Estoque Automatizado**: O saldo de estoque é atualizado automaticamente e é somente leitura, prevenindo inconsistências.
- **Validação de Dados**: Regras de negócio implementadas para garantir a integridade dos dados, como a validação de estoque negativo.

## Estrutura do Projeto

O projeto segue uma arquitetura modular para facilitar a manutenção e escalabilidade:

- **`core`**: Configurações centrais do projeto Django.
- **`supplier`**: Gerencia fornecedores e seus contatos.
- **`product`**: Gerencia produtos, categorias, marcas e lotes.
- **`movement_stock`**: Registra todas as movimentações de estoque. A criação de um registro aqui dispara um `signal` que atualiza o inventário.
- **`inventory`**: Mantém o saldo atual de cada produto/lote. Os dados são somente leitura e gerenciados automaticamente pelos `signals`.

## Primeiros Passos

Siga estas instruções para configurar e executar o projeto em seu ambiente de desenvolvimento.

### Pré-requisitos

- **Python** (versão `3.12` ou superior)
- **Poetry** (para gerenciamento de dependências)

### Guia de Instalação

1.**Clone o repositório:**
    ```bash
    git clone https://github.com/RogerioCampos07/DjangoAdminStock.git
    cd DjangoAdminStock
    ```

2.**Configure as variáveis de ambiente:**
    Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`.
    ```bash
    cp .env.example .env
    ```
    Abra o arquivo `.env` e **gere uma nova `SECRET_KEY`**. Você pode usar o comando abaixo para gerar uma:
    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

3.**Instale as dependências:**
    O Poetry criará um ambiente virtual e instalará todas as dependências listadas no `pyproject.toml`.
    ```bash
    poetry install
    ```

4.**Ative o ambiente virtual:**
    ```bash
    source .venv/bin/activate
    ```

5.**Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.**Crie um superusuário:**
    Você usará este usuário para acessar o painel de administração.
    ```bash
    python manage.py createsuperuser
    ```

7.**Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

Pronto! A aplicação estará rodando em `http://127.0.0.1:8000/`.

## Como Utilizar

O fluxo de trabalho do sistema foi projetado para ser intuitivo e segue uma ordem lógica de cadastro.

1.**Acesse o painel de administração:**
    Vá para `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.

2.**Cadastre os dados básicos:**
    - **Produtos > Categorias de Produtos**
    - **Produtos > Marcas**

3.**Cadastre os Fornecedores:**
    - **Supplier > Fornecedores**
    - **Supplier > Representantes** (associando-os a um fornecedor)

4.**Cadastre seus Produtos:**
    - Em **Produtos > Produtos**, crie novos itens, associando-os a categorias, marcas e fornecedores.

5.**Gerencie o Estoque:**
    - Use **Movimentos de Estoque > Adicionar** para registrar entradas, saídas ou ajustes.
    - O painel de **Estoque** será atualizado automaticamente e serve apenas para consulta.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto, criar uma branch para sua feature e abrir um Pull Request.
