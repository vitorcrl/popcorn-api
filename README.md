
# Popcorn API

Este projeto é uma API para gerenciar pipocas, sabores, pedidos, produção e pontos de venda, utilizando FastAPI, SQLAlchemy e SQLite.

## Requisitos

- **Python 3.8+**
- **Poetry**: para gerenciar dependências e ambientes virtuais.

## Configuração

### 1. Instalar Dependências

Primeiro, certifique-se de que o [Poetry](https://python-poetry.org/docs/#installation) está instalado. Em seguida, rode o comando para instalar as dependências do projeto:

```bash
poetry install
```

### 2. Ativar o Ambiente Virtual

Ative o ambiente virtual criado pelo Poetry. Existem duas maneiras de fazer isso:

- **Método 1:** Deixe o Poetry gerenciar o ambiente virtual automaticamente:

```bash
poetry shell
```

- **Método 2:** Ativar o ambiente manualmente (caso prefira usar o ambiente virtual do sistema):

```bash
source $(poetry env info --path)/bin/activate
```

### 3. Variáveis de Ambiente

Você pode configurar variáveis de ambiente utilizando um arquivo `.env`. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DATABASE_URL=sqlite:///./test.db
```

### 4. Aplicar Migrações

Se você estiver utilizando Alembic para migrações de banco de dados, siga os passos abaixo para configurar e rodar as migrações.

1. **Inicializar Alembic (caso ainda não tenha feito):**

```bash
poetry run alembic init alembic
```

2. **Configurar `alembic.ini`:**

Edite o arquivo `alembic.ini` para apontar para o seu banco de dados SQLite (ou outro que esteja utilizando). Por exemplo:

```ini
sqlalchemy.url = sqlite:///./test.db
```

3. **Criar uma migração:**

```bash
poetry run alembic revision --autogenerate -m "Initial migration"
```

4. **Aplicar as migrações:**

```bash
poetry run alembic upgrade head
```

### 5. Iniciar o Servidor

Para rodar a API, use o comando:

```bash
poetry run start
```

Isso vai iniciar o servidor Uvicorn com o `--reload` ativado, permitindo que mudanças no código sejam refletidas sem precisar reiniciar manualmente.

### 6. Acessar a Documentação da API

Uma vez que o servidor estiver rodando, você pode acessar a documentação interativa da API no Swagger, indo até:

```
http://127.0.0.1:8000/docs
```

## Testes

### Configurar Testes

Se estiver utilizando o `pytest` para os testes, certifique-se de que ele está instalado (adicionando ao `pyproject.toml`, se necessário):

```bash
poetry add pytest --dev
```

### Rodar os Testes

Execute os testes com o seguinte comando:

```bash
poetry run pytest
```

Certifique-se de que os testes estão em uma pasta chamada `tests/`, seguindo as convenções de teste do `pytest`.

## Contribuindo

Se quiser contribuir, sinta-se à vontade para enviar pull requests. Siga os padrões de codificação estabelecidos e mantenha os testes atualizados.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
```

### Configurações adicionais:
- **Ativação do ambiente Python manualmente:** Agora o README inclui um comando para ativar o ambiente virtual manualmente caso necessário.
- **Migrações e Inicialização do Servidor:** Incluí a configuração para rodar o Alembic e iniciar o servidor utilizando o script que você configurou no `pyproject.toml`.
