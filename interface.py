import tkinter as tk
from tkinter import filedialog
import pyperclip
import pandas as pd
from unificada import caminho_unificada
from unificada import notas, impostos, caucao#, devolucoes

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename()
    caminho_unificada.set(caminho_arquivo)

def gerar_arquivo():
    # Lógica de geração de arquivo aqui
    # Substitua a mensagem e adicione a lógica real de geração de arquivo.
    mensagem.config(text="Arquivo gerado com sucesso!")

def copiar_notas():
    notas.to_clipboard(index=False, excel=True)
    mensagem.config(text="Notas fiscais copiadas para a área de transferência.")

def copiar_impostos():
    impostos.to_clipboard(index=False, excel=True)
    mensagem.config(text="Impostos retidos copiados para a área de transferência.")

def copiar_caucao():
    caucao.to_clipboard(index=False, excel=True)
    mensagem.config(text="Caução copiada para a área de transferência.")

def copiar_devolucoes():
    devolucoes.to_clipboard(index=False, excel=True)
    mensagem.config(text="Devoluções copiadas para a área de transferência.")

# Criar janela principal
janela = tk.Tk()
janela.title('Gerador de Cargas')

# Criar variável StringVar para o caminho_unificada
caminho_unificada = tk.StringVar()

# Criar campo de entrada
entrada_caminho = tk.Entry(janela, width=30, textvariable=caminho_unificada)
entrada_caminho.grid(row=0, column=0)

# Criar botão para selecionar arquivo
botao_selecionar_arquivo = tk.Button(janela, text='Selecionar Arquivo', command=selecionar_arquivo)
botao_selecionar_arquivo.grid(row=0, column=1)

# Criar botão para gerar arquivo
botao_gerar_arquivo = tk.Button(janela, text='Gerar Arquivo', command=gerar_arquivo)
botao_gerar_arquivo.grid(row=1, column=0, columnspan=2, pady=10)

# Criar rótulo para exibir mensagem
mensagem = tk.Label(janela, text="Selecione o arquivo e clique em gerar")
mensagem.grid(row=2, column=0, columnspan=2, pady=10)

# Criar cópia de Notas
texto_copiar_notas = tk.Label(janela, text="Notas Fiscais: ")
texto_copiar_notas.grid(row=3, column=0)
botao_copiar_notas = tk.Button(janela, text='Copiar', command=copiar_notas)
botao_copiar_notas.grid(row=3, column=1)

# Criar cópia de Impostos retidos
texto_copiar_impostos = tk.Label(janela, text="Impostos Retidos: ")
texto_copiar_impostos.grid(row=4, column=0)
botao_copiar_impostos = tk.Button(janela, text='Copiar', command=copiar_impostos)
botao_copiar_impostos.grid(row=4, column=0)

# Criar cópia de Caução
texto_copiar_caucao = tk.Label(janela, text="Caução: ")
texto_copiar_caucao.grid(row=5, column=0)
botao_copiar_caucao = tk.Button(janela, text='Copiar', command=copiar_caucao)
botao_copiar_caucao.grid(row=5, column=1)

# Criar cópia de Devoluções
texto_copiar_devolucoes = tk.Label(janela, text="Devoluções: ")
texto_copiar_devolucoes.grid(row=6, column=0)
botao_copiar_devolucoes = tk.Button(janela, text='Copiar', command=copiar_devolucoes)
botao_copiar_devolucoes.grid(row=6, column=1)

# Iniciar o loop principal da janela
janela.mainloop()
