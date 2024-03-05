# user_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    # Lógica para buscar usuários no banco de dados PostgreSQL
    # ...

    # Exemplo: retornando usuários fictícios
    users = [{'id': 1, 'name': 'Usuário 1'}, {'id': 2, 'name': 'Usuário 2'}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
