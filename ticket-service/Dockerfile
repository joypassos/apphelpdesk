FROM python:3.8-slim

WORKDIR /ticket_service

RUN pip install flask requests

COPY . .

CMD ["python", "ticket_service.py"]
