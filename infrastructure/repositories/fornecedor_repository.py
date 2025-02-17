from ..database import get_db_connection

class FornecedorRepository:
    @staticmethod
    def get_all_fornecedores():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM fornecedores")
        fornecedores = cur.fetchall()
        cur.close()
        conn.close()
        return fornecedores

    @staticmethod
    def get_fornecedor_by_id(fornecedor_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM fornecedores WHERE id = %s", (fornecedor_id,))
        fornecedor = cur.fetchone()
        cur.close()
        conn.close()
        return fornecedor

    @staticmethod
    def get_fornecedores_by_consumo(consumo_mensal):
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
        return fornecedores_filtrados
