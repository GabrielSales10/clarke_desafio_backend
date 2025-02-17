from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import schema 
from database import get_db_connection  
app = Flask(__name__)
CORS(app)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao sistema de escolha de fornecedores de energia!"})

if __name__ == '__main__':
    app.run(debug=True)
