import tkinter as tk
from tkinter import messagebox

def exibir_mensagem(nome):
    mensagem = f"Bem-vindo, {nome}!"
    messagebox.showinfo("Mensagem de Boas-Vindas", mensagem)

def obter_nome():
    nome = entrada_nome.get()
    if nome:
        exibir_mensagem(nome)
    else:
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")

janela = tk.Tk()
janela.title("Sistema de Cadastro")


rotulo_nome = tk.Label(janela, text="Nome:")
rotulo_nome.pack(pady=10)

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=10)

botao_enviar = tk.Button(janela, text="Enviar", command=obter_nome)
botao_enviar.pack(pady=10)


janela.mainloop()
