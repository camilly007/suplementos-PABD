class Usuario:
    def __init__(self, username, senha, codU):
        self.username = username 
        self.senha=senha
        self.codU=codU
    def __str__(self):
        return f"Nome:{self.username}\nSenha:{self.senha}\nCodigo: {self.codU}"
    