from flask import Flask, request, jsonify
from decimal import Decimal, InvalidOperation
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import graphene
from graphene import ObjectType, String, Int, Decimal as GDecimal
from flask_graphql import GraphQLView

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="fornecedores_db",
        user="gabriel",
        password="#800VSea1000@",
        host="localhost",  
        port="5432"
    )
    return conn

class FornecedorType(graphene.ObjectType):
    nome = graphene.String()
    estado = graphene.String()
    custo_kwh = graphene.Float()
    limite_min_kwh = graphene.Int()
    num_clientes = graphene.Int()
    avaliacao_media = graphene.Float()

class Query(ObjectType):
    fornecedores = graphene.List(FornecedorType)
    fornecedor = graphene.Field(FornecedorType, id=Int())

    def resolve_fornecedores(self, info):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM fornecedores")
        fornecedores = cur.fetchall()
        cur.close()
        conn.close()
        return fornecedores

    def resolve_fornecedor(self, info, id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM fornecedores WHERE id = %s", (id,))
        fornecedor = cur.fetchone()
        cur.close()
        conn.close()
        return fornecedor

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao sistema de escolha de fornecedores de energia!"})

@app.route('/consumo', methods=['POST'])
def receber_consumo():
    if request.content_type != 'application/json':
        return jsonify({'erro': 'Content-Type deve ser application/json'}), 415

    dados = request.get_json()
    if not dados or 'consumo_mensal' not in dados:
        return jsonify({'erro': 'Consumo mensal não informado'}), 400
    
    consumo_mensal_str = dados['consumo_mensal']
    
    try:
        consumo_mensal = Decimal(consumo_mensal_str)
        if consumo_mensal <= 0:
            return jsonify({'erro': 'O consumo mensal deve ser maior que zero'}), 400
    except (InvalidOperation, ValueError):
        return jsonify({'erro': 'Consumo mensal inválido. Certifique-se de usar um número válido.'}), 400

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("""
        SELECT * FROM fornecedores
        WHERE limite_min_kwh <= %s
        ORDER BY custo_kwh ASC
    """, (consumo_mensal,))
    
    fornecedores_filtrados = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify({'fornecedores': fornecedores_filtrados}), 200

if __name__ == '__main__':
    app.run(debug=True)