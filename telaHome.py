import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.suplemento_banco import suplemento_banco

def tabela_suplementos():
    janela = tk.Tk()
    janela.title("Tabela de Suplementos")
    janela.geometry("600x300")

    tree = ttk.Treeview(janela, columns=("tipo", "marca", "valor", "quantidade", "status", "codigo"), show='headings')
    tree.heading("tipo", text="Tipo")
    tree.heading("marca", text="Marca")
    tree.heading("valor", text="Valor")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("status", text="Status")
    tree.heading("codigo", text="Código")

    tree.column('tipo',width=100)
    tree.column('marca',width=100)
    tree.column('valor',width=100)
    tree.column('quantidade',width=100)
    tree.column('status',width=100)
    tree.column('codigo',width=100)

    sb = suplemento_banco() 
    dados = sb.get_all_suplementos()
    
    for item in dados:
        if item.ativo!=False:
            tree.insert("", tk.END, values=(item.tipo,item.marca,item.valor,item.quantidade,item.ativo,item.codS))
    tree.pack()
    janela.mainloop()
    
def criar():
    global entry_tipo
    global entry_marca
    global entry_valor
    global entry_quantidade

    tipo=entry_tipo.get()
    marca=entry_marca.get()
    valor=entry_valor.get()
    quantidade=entry_quantidade.get()
    status='true'

    sb=suplemento_banco()
    try:
        supli=sb.criate_suplemento(tipo,marca,valor,quantidade,status)
        messagebox.showinfo('certo','suplemento adicionado')
    except:
        messagebox.showerror('errado','impossivel adicionar suplemento')
    
def adicionar_suplemento():

    global entry_tipo
    global entry_marca
    global entry_valor
    global entry_quantidade
    janela = tk.Tk()
    janela.title("Tabela de Suplementos")
    janela.geometry("600x300")

    label_tipo=tk.Label(janela,text='tipo')
    label_tipo.pack()

    entry_tipo=tk.Entry(janela)
    entry_tipo.pack()

    label_marca=tk.Label(janela,text='marca')
    label_marca.pack()

    entry_marca=tk.Entry(janela)
    entry_marca.pack()

    label_valor=tk.Label(janela,text='valor')
    label_valor.pack()

    entry_valor=tk.Entry(janela)
    entry_valor.pack()

    label_quantida=tk.Label(janela,text='quantidade')
    label_quantida.pack()

    entry_quantidade=tk.Entry(janela)
    entry_quantidade.pack()

    botao=tk.Button(janela,text='adicionar',command=criar)
    botao.pack()

def vender_suplemento():
    global entry_cod
    janela = tk.Tk()
    janela.title("Tabela de Suplementos")
    janela.geometry("600x300")
    label_cod=tk.Label(janela,text='digite o codigodo suplemento para vender')
    label_cod.pack()
    entry_cod=tk.Entry(janela)
    entry_cod.pack()
    botao_vender=tk.Button(janela,text='vender suplemento', command=vender)
    botao_vender.pack(pady=4)
    janela.mainloop()
def vender():
    global entry_cod

    codS=entry_cod.get()
    sb=suplemento_banco()
    try:
        venda=sb.update_to_false(codS)
        messagebox.showinfo('certo','vendido com sucesso')
    except:
        messagebox.showerror('errado',"impossivel vender")

def atualizar_suplemento():

    global entry_tipo
    global entry_marca
    global entry_valor
    global entry_quantidade
    global entry_cod
    janela=tk.Tk()
    janela.geometry("500x300")

    label_cod=tk.Label(janela,text='digite o codigo do produto que você deseja atualizar')
    label_cod.pack()

    entry_cod=tk.Entry(janela)
    entry_cod.pack()
    label_tipo=tk.Label (janela,text="tipo")
    label_tipo.pack()

    entry_tipo=tk.Entry(janela)
    entry_tipo.pack()

    label_marca=tk.Label(janela,text='marca')
    label_marca.pack()

    entry_marca=tk.Entry(janela)
    entry_marca.pack()

    label_valor=tk.Label(janela,text='valor')
    label_valor.pack()

    entry_valor=tk.Entry(janela)
    entry_valor.pack()

    label_quantida=tk.Label(janela,text='quantidade')
    label_quantida.pack()

    entry_quantidade=tk.Entry(janela)
    entry_quantidade.pack()

    botao=tk.Button(janela,text='adicionar',command=atualizar)
    botao.pack()
    janela.mainloop()

def atualizar():
    global entry_tipo
    global entry_marca
    global entry_valor
    global entry_quantidade
    global entry_cod

    tipo=entry_tipo.get()
    marca=entry_marca.get()
    valor=entry_valor.get()
    quantidade=entry_quantidade.get()
    codigo=entry_cod.get()

    sb=suplemento_banco()
    try:
        atualizar=sb.atualizar_suplemento(codigo,tipo,marca,valor,quantidade)
        messagebox.showinfo("certo","atualizado com sucesso")
    except:
        messagebox.showerror("erro","impossivel atualizar")


def run():
    janela=tk.Tk()
    janela.title('life style suplements:')
    janela.geometry("500x300")

    botao=tk.Button(janela,text='ver suplementos', command=tabela_suplementos)
    botao.pack(pady=4)

    botao_criar=tk.Button(janela,text='adicionar suplemento',command=adicionar_suplemento)
    botao_criar.pack(pady=4)

    botao_vender=tk.Button(janela,text='vender suplemento',command=vender_suplemento)
    botao_vender.pack(pady=4)

    botao_atualizar=tk.Button(janela,text='atualizar suplemento',command=atualizar_suplemento)
    botao_atualizar.pack(pady=4)


    janela.mainloop()