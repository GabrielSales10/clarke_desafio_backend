import pytest
import sys
import os
from app import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_graphql_query(client):
    query = '''
        {
            fornecedores {
                nome
                estado
                custo_kwh
            }
        }
    '''
    response = client.post('/graphql', json={'query': query})
    print("Response Status Code:", response.status_code)  
    print("Response Data:", response.data.decode())  
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert 'fornecedores' in data['data']


def test_graphql_fornecedor_query(client):
    query = '''
        {
            fornecedor(id: 1) {
                nome
                estado
                custo_kwh
            }
        }
    '''
    response = client.post('/graphql', json={'query': query})
    print("Response Status Code:", response.status_code) 
    print("Response Data:", response.data.decode())  
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert 'fornecedor' in data['data']
    assert data['data']['fornecedor'] is not None


def test_receber_consumo(client):
    consumo = {'consumo_mensal': '300'}  
    response = client.post('/consumo', json=consumo)
    print("Response Status Code:", response.status_code)  
    print("Response Data:", response.data.decode())  
    assert response.status_code == 200
    data = response.get_json()
    assert 'fornecedores' in data

def test_receber_consumo_com_erro(client):
    consumo = {'consumo_mensal': 'abc'}  
    response = client.post('/consumo', json=consumo)
    print("Response Status Code:", response.status_code) 
    print("Response Data:", response.data.decode()) 
    assert response.status_code == 400
    data = response.get_json()
    assert 'erro' in data


def test_conteudo_invalid(client):
    response = client.post('/consumo', data="consumo_mensal=300", content_type='application/x-www-form-urlencoded')
    print("Response Status Code:", response.status_code)  
    print("Response Data:", response.data.decode())  
    assert response.status_code == 415
    data = response.get_json()
    assert 'erro' in data
