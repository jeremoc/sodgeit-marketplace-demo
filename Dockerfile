FROM python:3.13.0-slim
COPY main.py /main.py
RUN pip install click
ENTRYPOINT ["python3", "/main.py", "README.md"]
