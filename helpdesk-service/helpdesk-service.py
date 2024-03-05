# helpdesk_service.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:5000/users"
TICKET_SERVICE_URL = "http://ticket-service:5000/tickets"

@app.route('/helpdesk', methods=['GET'])
def get_helpdesk_info():
    # Integração com os microserviços de usuário e ticket
    users = requests.get(USER_SERVICE_URL).json()
    tickets = requests.get(TICKET_SERVICE_URL).json()

    # Lógica adicional para processar os dados e fornecer informações do helpdesk
    # ...

    helpdesk_info = {'users': users, 'tickets': tickets}
    return jsonify(helpdesk_info)

if __name__ == '__main__':
    app.run(debug=True)
