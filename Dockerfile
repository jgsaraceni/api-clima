FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

COPY app ./app

EXPOSE 8000

CMD ["conda", "run", "--no-capture-output", "-n", "weather-api", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
