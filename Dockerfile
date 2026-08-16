FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml && conda clean -afy

COPY app ./app

# Ensure conda env binaries are on PATH
ENV PATH /opt/conda/envs/weather-api/bin:$PATH

EXPOSE 8000

CMD ["conda", "run", "--no-capture-output", "-n", "weather-api", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
