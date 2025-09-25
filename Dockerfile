FROM python:3.13.0-slim
COPY main.py /main.py

ARG FILE_NAME=README.md
ENV FILE_NAME=${FILE_NAME}

RUN pip install click

ENTRYPOINT ["python3", "/main.py"]
CMD ["README.md"]
