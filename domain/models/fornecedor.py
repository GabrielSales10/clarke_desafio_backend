class Fornecedor:
    def __init__(self, nome, estado, custo_kwh, limite_min_kwh, num_clientes, avaliacao_media):
        self.nome = nome
        self.estado = estado
        self.custo_kwh = custo_kwh
        self.limite_min_kwh = limite_min_kwh
        self.num_clientes = num_clientes
        self.avaliacao_media = avaliacao_media
