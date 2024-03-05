# ticket_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    # Lógica para buscar tickets no banco de dados PostgreSQL
    # ...

    # Exemplo: retornando tickets fictícios
    tickets = [{'id': 1, 'title': 'Problema 1'}, {'id': 2, 'title': 'Problema 2'}]
    return jsonify(tickets)

if __name__ == '__main__':
    app.run(debug=True)
