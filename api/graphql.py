import graphene
from graphene import ObjectType, Int
from flask_graphql import GraphQLView
from .db import get_db_connection
from psycopg2.extras import RealDictCursor

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

def handler(request):
    schema = graphene.Schema(query=Query)
    view = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    return view(request)
