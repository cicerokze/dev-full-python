# dev-full-python
Projeto desenvolvido como avaliação para vaga de Desenvolvedor Full Stack Python (Pleno)

# FastAPI Orders App (v0.1.0)

## Visão Geral

Uma aplicação fullstack FastAPI + Jinja2 SSR para cadastro e listagem de pedidos, utilizando MongoDB, Bulma CSS e HTMX.

## Como Executar Localmente

### Com Docker Compose

```bash
docker-compose up --build
```

### Sem Docker

1. Instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate
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

- Implementar a feature de cadastro