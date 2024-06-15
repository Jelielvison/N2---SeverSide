from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import gerador
import json
import random


vetor_rand = gerador.vetor_randomizado

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/tabela_valores'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ValueModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, value):
        self.value = value

# Garantir que o contexto da aplicação esteja ativo ao criar as tabelas
with app.app_context():
    db.create_all()

def insert_values_in_batches(vetor_randomizado, batch_size=50000):
    for i in range(0, len(vetor_randomizado), batch_size):
        batch = vetor_randomizado[i:i+batch_size]
        value_objects = [ValueModel(value=value) for value in batch]
        with app.app_context():
            db.session.bulk_save_objects(value_objects)
            db.session.commit()
    print("Valores inseridos com sucesso!")

@app.route('/enviar_valores', methods=['POST'])
def enviar_valores():

    # Inserir vetor randomizado no banco de dados
    insert_values_in_batches(vetor_rand)

    return jsonify({'message': 'Valores enviados com sucesso!'})

@app.route('/mostrar_valores', methods=['GET'])
def mostrar_valores():
    valores = ValueModel.query.all()
    valores_json = [{'id': valor.id, 'value': valor.value} for valor in valores]
    return jsonify({'valores': valores_json})

if __name__ == '__main__':
    app.run(debug=True)
