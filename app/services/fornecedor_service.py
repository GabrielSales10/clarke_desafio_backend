from infrastructure.repositories.fornecedor_repository import FornecedorRepository
from domain.models.fornecedor import Fornecedor

class FornecedorService:
    @staticmethod
    def get_fornecedores():
        fornecedores_data = FornecedorRepository.get_all_fornecedores()
        return [Fornecedor(**f) for f in fornecedores_data]

    @staticmethod
    def get_fornecedor(id):
        fornecedor_data = FornecedorRepository.get_fornecedor_by_id(id)
        if fornecedor_data:
            return Fornecedor(**fornecedor_data)
        return None

    @staticmethod
    def get_fornecedores_por_consumo(consumo_mensal):
        fornecedores_data = FornecedorRepository.get_fornecedores_by_consumo(consumo_mensal)
        return [Fornecedor(**f) for f in fornecedores_data]
