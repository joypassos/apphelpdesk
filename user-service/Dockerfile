# user-service/Dockerfile
FROM python:3.8-slim

WORKDIR /user_service


# Instalação de dependências diretamente no Dockerfile
RUN pip install flask requests

COPY . .

CMD ["python", "user_service.py"]
