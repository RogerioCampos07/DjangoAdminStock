# DjangoAdminStock

Um sistema de gerenciamento de estoque simples e eficiente, administrado via painel Django Admin.

## Visão Geral

Este projeto visa fornecer uma solução robusta e fácil de usar para controle de estoque, com foco na interface de administração do Django para gestão completa de produtos, entradas, saídas e relatórios.

## Roadmap do Projeto

Este é o nosso plano de desenvolvimento para o DjangoAdminStock.

### Fase 1: Core do Sistema (Concluído)

- [x] Configuração inicial do projeto Django e Poetry.
- [ ] Modelos básicos para Produtos (Nome, Preço, SKU, etc.).
- [ ] Registro dos modelos no Django Admin.
- [ ] Integração com Docker Compose (Django, PostgreSQL).

### Fase 2: Gestão de Inventário (Em Andamento)

- [ ] Modelos para Entrada de Estoque (Fornecedor, Quantidade, Data).
- [ ] Modelos para Saída de Estoque (Cliente, Quantidade, Data).
- [ ] Lógica para atualização automática do estoque total ao registrar entradas/saídas.
- [ ] Interface administrativa para gerenciar Entradas e Saídas.

### Fase 3: Funcionalidades Avançadas (Próximo)

- [ ] Relatórios básicos de estoque (Produtos com baixo estoque, Movimentação por período).
- [ ] Funcionalidade de busca e filtro aprimorados no Admin.
- [ ] Geração de PDF/CSV para relatórios.

### Ideias Futuras

- Integração com leitores de código de barras.
- Notificações de baixo estoque.
- Histórico de preços.
- IA - Agentes para analise de estoque.
