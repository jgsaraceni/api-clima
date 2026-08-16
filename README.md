# Weather API

Projeto exemplo `weather-api` com FastAPI, Conda e Docker.

Reproduzir ambiente localmente:

```bash
conda env create -f environment.yml
conda activate weather-api
```

Rodar com Docker:

```bash
docker compose up --build
```

Instalação via `pip` (opcional, sem Conda):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Página inicial e uso
--------------------

A aplicação serve uma página HTML explicativa na raiz do site (`/`). Ao abrir a URL raiz no navegador você verá instruções simples sobre como usar a API, um exemplo prático de chamada e uma referência para testar a API na interface interativa do FastAPI.

- A página inicial está disponível em `/` — por exemplo, `http://127.0.0.1:8000/` se você executar com o comando `uvicorn` acima. Se você executar o servidor em outra porta (por exemplo `1234`), use `http://127.0.0.1:1234/`.
- A documentação interativa do FastAPI está em `/docs` (ex.: `http://127.0.0.1:8000/docs`).

Exemplo de chamada direta
------------------------

Para obter a temperatura atual de uma cidade, acesse a rota `GET /temperatura-cidade` com o parâmetro `nome_cidade`. Exemplo:

```
http://127.0.0.1:8000/temperatura-cidade?nome_cidade=Curitiba
```

A resposta retorna apenas o valor numérico da temperatura atual em graus Celsius.

