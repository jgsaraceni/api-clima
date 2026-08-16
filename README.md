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


Página inicial e uso
--------------------

A aplicação serve uma página HTML explicativa na raiz do site (`/`). Ao abrir a URL raiz no navegador você verá instruções simples sobre como usar a API, um exemplo prático de chamada e uma referência para testar a API na interface interativa do FastAPI.

- A página inicial está disponível em `/` — por exemplo, `http://146.235.55.187:1234/` se você executar com o comando `uvicorn` acima. Se você executar o servidor em outra porta (por exemplo `1234`), use `http://146.235.55.187:1234/`.
- A documentação interativa do FastAPI está em `/docs` (ex.: `http://146.235.55.187:1234/docs`).

Exemplo de chamada direta
------------------------

Para obter a temperatura atual de uma cidade, acesse a rota `GET /temperatura-cidade` com o parâmetro `nome_cidade`. Exemplo:

```
http://146.235.55.187:1234/temperatura-cidade?nome_cidade=Curitiba
```

A resposta retorna apenas o valor numérico da temperatura atual em graus Celsius.

