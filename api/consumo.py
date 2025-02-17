from flask import request, jsonify
from decimal import Decimal, InvalidOperation
from .db import get_db_connection

def handler(request):
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
