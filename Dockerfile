FROM python:3.13.0-slim
COPY hello.py /hello.py
ENTRYPOINT ["python3", "/main.py"]
