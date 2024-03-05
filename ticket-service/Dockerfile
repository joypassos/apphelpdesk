FROM python:3.8-slim

WORKDIR /ticket-service

RUN pip install flask requests

COPY . .

CMD ["python", "ticket_service.py"]
