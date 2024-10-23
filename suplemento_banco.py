import psycopg2
from backend.Suplemento import Suplemento

class suplemento_banco:
    def __init__(self):
        self.connect=psycopg2.connect(dbname="projeto_pabd",user="postgres",password="cams05",host="localhost",port=5432)
        self.cursor=self.connect.cursor()
        self.connect.autocommit=True

    def get_all_suplementos(self):
        
        codsql=f"SELECT * FROM suplementos"
        self.cursor.execute(codsql)
        result=self.cursor.fetchall()
        lista_suplis=[]


        if result != None: 
            for suplemento in result: 
                tipo=suplemento[0]
                marca=suplemento[1]
                valor=suplemento[2]
                quantidade=suplemento[3]
                ativo=suplemento[5]
                codS=suplemento[4]
                suplemento=Suplemento(tipo,marca,valor,quantidade,ativo,codS)
                lista_suplis.append(suplemento)
        else:
    
            lista_suplis=None
        return lista_suplis
    
    def criate_suplemento(self,tipo,marca,valor,quantidade,status):
        codsql=f"INSERT INTO suplementos(tipo,marca,valor,quantidade,ativo) VALUES ('{tipo}','{marca}',{valor},{quantidade},'{status}')"
        self.cursor.execute(codsql)

    def update_to_false(self,codS):
        codsql=f"UPDATE suplementos SET ativo='false' WHERE cods={codS}"
        self.cursor.execute(codsql)

    def atualizar_suplemento(self,cod,tipo,marca,valor,quantidade):
        codsql=f"UPDATE suplementos SET tipo='{tipo}', marca='{marca}',valor={valor},quantidade ={quantidade} WHERE  cods={cod}"
        self.cursor.execute (codsql)
