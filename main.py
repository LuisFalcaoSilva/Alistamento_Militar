import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# === Funções de Banco de Dados ===
def conectar_banco():
    con = sqlite3.connect("alistamento.db")
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sexo TEXT CHECK(sexo IN ('MASCULINO', 'FEMININO')),
        ano_nascimento INTEGER,
        idade INTEGER,
        situacao_alistamento TEXT,
        multa REAL DEFAULT 0,
        data_conversa TEXT DEFAULT (datetime('now'))
    )
    ''')
    con.commit()
    return con, cur

def inserir_usuario(nome, sexo, ano_nasc, idade, situacao, multa):
    con, cur = conectar_banco()
    cur.execute('''
    INSERT INTO usuarios (nome, sexo, ano_nascimento, idade, situacao_alistamento, multa, data_conversa)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, sexo, ano_nasc, idade, situacao, multa, datetime.now().isoformat()))
    con.commit()
    con.close()

def carregar_dados():
    con, cur = conectar_banco()
    cur.execute("SELECT * FROM usuarios")
    dados = cur.fetchall()
    con.close()
    return dados

def excluir_usuario(id_):
    con, cur = conectar_banco()
    cur.execute("DELETE FROM usuarios WHERE id = ?", (id_,))
    con.commit()
    con.close()

def limpar_tudo():
    con, cur = conectar_banco()
    cur.execute("DELETE FROM usuarios")
    con.commit()
    con.close()

# === Funções de Lógica ===
def calcular_situacao(sexo, ano_nasc):
    idade = 2025 - ano_nasc
    if sexo == "FEMININO":
        return idade, "Não aplicável", 0
    if idade == 18:
        return idade, "Ano do alistamento", 0
    elif idade < 18:
        return idade, "A alistar", 0
    else:
        multa = (idade - 18) * 10
        return idade, "Fora do prazo", multa

# === Funções da Interface ===
def adicionar_usuario():
    nome = entry_nome.get().strip().upper()
    sexo = combo_sexo.get().strip().upper()
    ano = entry_ano.get().strip()

    if not nome or not sexo or not ano:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    try:
        ano_nasc = int(ano)
    except ValueError:
        messagebox.showerror("Erro", "O ano de nascimento deve ser um número.")
        return

    idade, situacao, multa = calcular_situacao(sexo, ano_nasc)
    inserir_usuario(nome, sexo, ano_nasc, idade, situacao, multa)
    atualizar_tabela()
    messagebox.showinfo("Sucesso", f"{nome} salvo com sucesso!")
    entry_nome.delete(0, tk.END)
    entry_ano.delete(0, tk.END)

def atualizar_tabela():
    for linha in tree.get_children():
        tree.delete(linha)
    for user in carregar_dados():
        tree.insert("", "end", values=user)

def excluir_selecionado():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
        return
    id_ = tree.item(selecionado)["values"][0]
    excluir_usuario(id_)
    atualizar_tabela()
    messagebox.showinfo("Sucesso", "Usuário excluído!")

def limpar_historico():
    if messagebox.askyesno("Confirmação", "Deseja apagar TODO o histórico?"):
        limpar_tudo()
        atualizar_tabela()
        messagebox.showinfo("Histórico limpo", "Todos os registros foram apagados.")

# === Interface Tkinter ===
janela = tk.Tk()
janela.title("ASCE - Sistema de Alistamento Militar")
janela.geometry("850x600")
janela.configure(bg="#2c3e50")

titulo = tk.Label(janela, text="SISTEMA DE ALISTAMENTO MILITAR", font=("Arial", 18, "bold"), fg="white", bg="#2c3e50")
titulo.pack(pady=10)

frame_form = tk.Frame(janela, bg="#34495e", padx=10, pady=10)
frame_form.pack(pady=10, fill="x")

tk.Label(frame_form, text="Nome:", bg="#34495e", fg="white").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Sexo:", bg="#34495e", fg="white").grid(row=0, column=2, padx=5)
combo_sexo = ttk.Combobox(frame_form, values=["MASCULINO", "FEMININO"], width=15)
combo_sexo.grid(row=0, column=3, padx=5)

tk.Label(frame_form, text="Ano de Nascimento:", bg="#34495e", fg="white").grid(row=0, column=4, padx=5)
entry_ano = tk.Entry(frame_form, width=10)
entry_ano.grid(row=0, column=5, padx=5)

btn_add = tk.Button(frame_form, text="Adicionar", bg="#27ae60", fg="white", command=adicionar_usuario)
btn_add.grid(row=0, column=6, padx=10)

# === Tabela ===
frame_tabela = tk.Frame(janela)
frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)

colunas = ("ID", "Nome", "Sexo", "Ano Nasc.", "Idade", "Situação", "Multa", "Data")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

tree.pack(fill="both", expand=True)

# === Botões inferiores ===
frame_botoes = tk.Frame(janela, bg="#2c3e50")
frame_botoes.pack(pady=10)

btn_excluir = tk.Button(frame_botoes, text="Excluir Selecionado", bg="#e74c3c", fg="white", command=excluir_selecionado)
btn_excluir.grid(row=0, column=0, padx=10)

btn_limpar = tk.Button(frame_botoes, text="Limpar Histórico", bg="#f39c12", fg="white", command=limpar_historico)
btn_limpar.grid(row=0, column=1, padx=10)

btn_atualizar = tk.Button(frame_botoes, text="Atualizar Tabela", bg="#2980b9", fg="white", command=atualizar_tabela)
btn_atualizar.grid(row=0, column=2, padx=10)

# === Inicialização ===
atualizar_tabela()
janela.mainloop()
