## FastAPI Gerenciador de Pedidos (v1.0.0)

Aplicação API desenvolvida com:
- FastAPI
- MongoDB
- Jinja2 SSR
- Bulma CSS
- HTMX

## Descrição

Uma aplicação fullstack FastAPI + Jinja2 SSR para cadastro e listagem de pedidos, utilizando MongoDB, Bulma CSS e HTMX.

## Como Executar Localmente

### Com Docker Compose

```bash
docker-compose up --build
```

### Sem Docker

1. Instale as dependências:
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```
2. Inicie o MongoDB (localmente ou via Docker).
3. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

## Estrutura do Projeto

- `/api`: Todos os endpoints RESTful, separados da lógica SSR.
- `/frontend`: Todas as rotas SSR, templates e arquivos estáticos.
- `/features`: Lógica de negócio, repositórios, casos de uso e schemas — orientado a features e reutilizável tanto pela API quanto pelo SSR.
- `/core`: Utilitários compartilhados, configurações e injeção de dependências.
- `/infra`: Infraestrutura, Docker, scripts.
- `main.py`: Faz o mount dos routers da API e SSR, serve arquivos estáticos e inicializa a aplicação.

## Próximos Passos

- Implementar o Frontend com requisições à API e MongoDB

## Documentação (Swagger)

**GET** http://localhost:8000/docs

![API - Documentação](/docs/order_manager.png)
