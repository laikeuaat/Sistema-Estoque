import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import customtkinter as ctk
from tkinter import messagebox
from infraestrutura.repositorio_usuario import (
    RepositorioUsuario,
)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def cadastrar_usuario():
    def salvar_cadastro():
        email = email_var.get()
        senha = senha_var.get()

        if not email or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            repositorio = RepositorioUsuario()
            repositorio.inserir_usuario(email, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            cadastro_toplevel.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    # Criar nova janela para cadastro
    cadastro_toplevel = ctk.CTkToplevel(root)
    cadastro_toplevel.title("Cadastro")
    cadastro_toplevel.geometry("600x400")

    frame_cadastro = ctk.CTkFrame(
        cadastro_toplevel, fg_color="white", corner_radius=15, width=350, height=250
    )
    frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

    titulo = ctk.CTkLabel(
        frame_cadastro, text="Cadastro", font=("Arial", 35, "bold"), text_color="black", width= 500, height= 100
    )
    titulo.pack(pady=10)

    email_var = ctk.StringVar()
    senha_var = ctk.StringVar()

    email_label = ctk.CTkLabel(
        frame_cadastro, text="E-mail:", font=("Arial", 12), text_color="black"
    )
    email_label.pack(anchor="w", padx=100)
    email_entry = ctk.CTkEntry(
        frame_cadastro,
        textvariable=email_var,
        width=300,
        height=55,
        border_width=1,
        corner_radius=30,
        fg_color="#D9D9D9",
    )
    email_entry.pack(pady=9)

    senha_label = ctk.CTkLabel(
        frame_cadastro, text="Senha:", font=("Arial", 12), text_color="black"
    )
    senha_label.pack(anchor="w", padx=100)
    senha_entry = ctk.CTkEntry(
        frame_cadastro,
        textvariable=senha_var,
        width=300,
        height=55,
        fg_color="#D9D9D9",
        corner_radius=30,
        border_width=1,
        show="*",
    )
    senha_entry.pack(pady=9)

    botao_salvar = ctk.CTkButton(
        frame_cadastro,
        text="Salvar",
        command=salvar_cadastro,
        width=100,
        height=50,
        corner_radius=20,
    )
    botao_salvar.pack(pady=10)


root = ctk.CTk()
root.title("Login")
root.attributes("-fullscreen", True)  # Janela em tela cheia

# Frame central maior e branco
frame = ctk.CTkFrame(root, fg_color="white", corner_radius=15, width=734, height=612)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Ícone superior
icon = ctk.CTkLabel(frame, text="\U0001f310", font=("Arial", 30), text_color="black")
icon.pack(pady=(20, 10))

# Título
titulo = ctk.CTkLabel(
    frame, text="Login", font=("Britannic Bold", 55, "bold"), text_color="#272626", width=600
)
titulo.pack(pady=10)


def login():
    email = email_var.get()
    senha = senha_var.get()

    if not email or not senha:
        messagebox.showinfo("erro", "preencha todos os campos!")

    try:
        repositorio = RepositorioUsuario()
        usuario = repositorio.buscar_usuario(email, senha)

        if usuario:
            messagebox.showinfo("Sucesso", "Login Bem sucedido")
        else:
            messagebox.showinfo("Erro", "Usuário ou Senha inválidos")
    except Exception as e:
        print(f"Erro ao realizar login: {e}")


email_var = ctk.StringVar()
senha_var = ctk.StringVar()

email_label = ctk.CTkLabel(
    frame, text="E-mail:", font=("Berlin Sans FB", 15), text_color="black"
)
email_label.pack(anchor="w", padx=85)
email_entry = ctk.CTkEntry(
    frame,
    textvariable=email_var,
    text_color="black",
    width=410,
    height=55,
    corner_radius=30,
    fg_color="#D9D9D9",
    border_width=1,
)
email_entry.pack(pady=10)

senha_label = ctk.CTkLabel(frame, text="Senha:", font=("Berlin Sans FB", 15), text_color="black")
senha_label.pack(anchor="w", padx=85)
senha_entry = ctk.CTkEntry(
    frame,
    textvariable=senha_var,
    width=410,
    text_color="black",
    height=55,
    corner_radius=30,
    show="*",
    fg_color="#D9D9D9",
    border_width=1,
)
senha_entry.pack(pady=10)

# Esqueci minha senha
forgot_pass = ctk.CTkLabel(
    frame,
    text="Esqueci minha senha",
    font=("Berlin Sans FB", 15, "underline"),
    text_color="#272626",
    cursor="hand2",
)
forgot_pass.pack(pady=10)


login_btn = ctk.CTkButton(
    frame,
    text="Entrar",
    font=("Britannic Bold", 20),
    command=login,
    width=100,
    height=50,
    corner_radius=20,
    fg_color="#272626",
)
login_btn.pack(pady=10)


cadastro_btn = ctk.CTkButton(
    frame,
    text="Cadastrar",
    command=cadastrar_usuario,
    font=("Britannic Bold", 20),
    width=100,
    height=50,
    corner_radius=20,
    fg_color="#108120",
)
cadastro_btn.pack(pady=10)

root.mainloop()
