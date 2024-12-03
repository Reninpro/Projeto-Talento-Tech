import tkinter as tk
from cachorro import Cachorro
from gato import Gato
from tkinter import messagebox
from tkinter import ttk


list = []

def cadastro_animal():
    nome = entrynome.get()
    idade = entryidade.get()
    raca = entryrace.get()
    animal = vartipo.get()
    
    if nome == "":
        messagebox.showerror("Erro nome", "O nome do animal precisa ser preenchido corretamente")
        return
    if idade == "" or not idade.isdigit(): 
        messagebox.showerror("Erro idade", "A idade do animal deve ser preenchida corretamente")
        return
    if raca == "":
        messagebox.showerror("Erro raça", "A raça/porte do animal precisa ser preenchida")
        return

    idade = int(idade)

    if animal == "Gato":
        g = Gato(nome, idade, raca)
        messagebox.showinfo("Cadastro", f"Gato {nome} cadastrado com sucesso.")
        salvar(g)
    else:
        c = Cachorro(nome, idade, raca)
        messagebox.showinfo("Cadastro", f"Cachorro {nome} cadastrado com sucesso.")
        salvar(c)

def salvar(obj):
    list.append(obj)

def atualizarlistabox():
    listbox.delete(0, tk.END)
    for obj in list:
        listbox.insert(tk.END, obj.mostrar())

janela = tk.Tk()
janela.title("Animais")
janela.geometry("650x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

screen = ttk.Notebook(janela)
screen.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(screen)
for i in range(4):
    tab1.rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

nome = tk.Label(tab1, text="Nome: ", font=("Arial", 15))
nome.grid(row=0, column=0, sticky="w")
entrynome = tk.Entry(tab1, font=("Times New Roman", 15))
entrynome.grid(row=0, column=1, sticky="w", pady=5)

idade = tk.Label(tab1, text="Idade:", font=("Arial", 15))
idade.grid(row=1, column=0, sticky="w", pady=5)
entryidade = tk.Entry(tab1, font=("Times New Roman", 15))
entryidade.grid(row=1, column=1, sticky="w")

race = tk.Label(tab1, text="Raça/Porte: ", font=("Arial", 15))
race.grid(row=2, column=0, sticky="w", pady=5)
entryrace = tk.Entry(tab1, font=("Times New Roman", 15))
entryrace.grid(row=2, column=1, sticky="w")

vartipo = tk.StringVar(value="Gato")
tk.Label(tab1, text="Qual é seu animal: ", font=("Arial", 15)).grid(row=3, column=0, sticky="w")
tk.Radiobutton(tab1, text="Gato", variable=vartipo, value="Gato").grid(row=3, column=1, sticky="w")
tk.Radiobutton(tab1, text="Cachorro", variable=vartipo, value="Cachorro").grid(row=3, column=2, sticky="w")

tk.Button(tab1, font=("Arial", 15), text="Enviar", command=cadastro_animal).grid(row=4, column=1, sticky="nsew")

tab2 = ttk.Frame(screen)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

listbox = tk.Listbox(tab2)
listbox.config(font=("Arial", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("Arial", 15), background="#ADD8E6", command=atualizarlistabox).grid(row=1, column=0, sticky="nsew")

screen.add(tab1, text="Cadastro de animais")
screen.add(tab2, text="Lista de animais")

janela.mainloop()