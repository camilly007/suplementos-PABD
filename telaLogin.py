import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.usuario_banco import usuario_banco
from frontend.telaHome import run


def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    ub=usuario_banco()
    result=ub.get_user(usuario)
    
    if result != None and result.senha==senha: 
        run()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

janela=tk.Tk()
janela.title("Tela de Login")
janela.geometry ("500x300")
label_nome=tk.Label(janela, text = "tela de login suplements", font=('arial'))
label_nome.pack(pady=5)

label_usuario = tk.Label(janela, text="username:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)

janela.mainloop()
