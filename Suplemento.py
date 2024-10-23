class Suplemento:
    def __init__(self,tipo,marca,valor,quantidade,codS,ativo=None):
        self.tipo=tipo
        self.marca=marca
        self.valor=valor
        self.quantidade=quantidade
        self.ativo=ativo
        self.codS=codS
        

    def __str__(self):
        return f'Tipo: {self.tipo}\nMarca: {self.marca}\nValor: {self.valor}\nQuantidade: {self.quantidade}\nCodigo: {self.codS}\nStatus: {self.ativo}'