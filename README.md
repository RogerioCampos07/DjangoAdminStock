# DjangoAdminStock

## Sobre o Projeto

Este é o **`django-admin-stock`**, um sistema de gestão de estoque construído sobre o **Admin do Django**. O objetivo é ter uma ferramenta simples e funcional para controlar produtos, fornecedores e o fluxo de estoque de forma centralizada.

A estrutura do projeto é modular, com apps bem definidos para facilitar a organização e manutenção:

- **`supplier`**: Gerencia fornecedores e seus contatos.
- **`product`**: Gerencia produtos, categorias e marcas.
- **`movement_stock`**: Gerencia as entradas e saídas de produtos.
- **`inventory`**: Gerencia o estoque atual de cada produto.

---

## Requisitos do Sistema

- **Linux**: Nosso ambiente de desenvolvimento e produção.
- **Python 3.13.3**
- **Poetry**
- **Docker** (opcional, para a fase de deploy)

---

## Configuração e Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/RogerioCampos07/DjangoAdminStock.git
cd django-admin-stock
```

### 2. Instale as dependências com Poetry

```bash
poetry install
```

Este comando lê o arquivo `pyproject.toml`, instala todas as dependências e cria um ambiente virtual isolado.

### 3. Ative o ambiente virtual

```bash
source ./venv/bin/activate
```

Isso ativa o ambiente virtual criado pelo Poetry, permitindo executar os comandos do Django.

### 4. Execute as migrações do banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Com o servidor rodando, acesse `http://localhost:8000/admin/` no navegador e faça login com o superusuário criado.

---

## Como Usar

O projeto é inteiramente baseado no painel de administração do Django. Siga a ordem de cadastro:

1. Acesse o painel em `http://localhost:8000/admin/`.
2. Cadastre **Categorias de Produto** e **Marcas**.
3. Cadastre os **Fornecedores** e, em seguida, seus **Representantes Comerciais**.
4. Crie os **Produtos** associando-os às categorias, marcas e fornecedores.
5. Use o painel de **Movimentação de Estoque** para registrar as entradas e saídas; o painel de **Estoque** é atualizado automaticamente.

---

## Contribuindo

Sinta-se à vontade para contribuir seguindo o fluxo padrão:

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b feature/minha-melhoria`.
3. Implemente mudanças e faça commit: `git commit -am 'Adiciona uma melhoria top'`.
4. Envie a branch: `git push origin feature/minha-melhoria`.
5. Abra um Pull Request.

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
