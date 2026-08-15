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
