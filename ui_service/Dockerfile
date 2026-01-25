FROM python:3.10-slim

# Mettre à jour pip d'abord
RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 --retries 5 -r requirements.txt

# Streamlit séparément avec miroir rapide
RUN pip install --no-cache-dir --default-timeout=100 --retries 5 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    streamlit

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
