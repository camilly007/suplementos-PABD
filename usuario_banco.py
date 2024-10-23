import psycopg2
from backend.Usuario import Usuario

class usuario_banco: 
    def __init__(self):
        self.conexao=psycopg2.connect(dbname="projeto_pabd",user="postgres",password="cams05",host="localhost",port=5432)
        self.cursor=self.conexao.cursor()
        self.conexao.autocommit=True

    def get_user(self,username):
        
        codsql="SELECT * FROM usuario WHERE username ='"+username+"';"
        self.cursor.execute(codsql)
        result=self.cursor.fetchone()

        if result != None: 
            username=result[0]
            senha=result[1]
            codU=result[2]
            usuario=Usuario(username,senha,codU)
        else: 
            usuario=None
        return usuario
