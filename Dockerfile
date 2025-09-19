FROM python:3.13.0-slim
COPY main.py /main.py
ENTRYPOINT ["python3", "/main.py"]
