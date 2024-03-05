FROM python:3.8-slim

WORKDIR /helpdesk_service

RUN pip install flask requests

COPY . .

CMD ["python", "helpdesk_service.py"]
