FROM python:3.9-slim
WORKDIR /worker
COPY . Shuffle_1_1
RUN test ! -e Shuffle_1_1/requirements.txt || pip install --no-cache-dir -r Shuffle_1_1/requirements.txt
ENTRYPOINT "Shuffle_1_1/shuffle.py"
