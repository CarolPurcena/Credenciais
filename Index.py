import customtkinter
from PIL import Image
import DataBase
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# =========== JANELAS ============
pagina_cadastro = customtkinter.CTk()
pagina_cadastro.geometry("800x700")
pagina_cadastro.resizable(width=False, height=False)

pagina_cadastro.iconbitmap(default="imgs/OmniLogo.ico")

# =================== IMAGENS ===============
logo = customtkinter.CTkImage(Image.open("imgs/Omni.png"), size=(250,150))

# ================ Listas ===================
tipo_credenciais = ("Temporária", "Permanente", "Visitante")
empresas = ("Omni Táxi Aéreo", "Maricá Offshore", "MR&Services", "Quality Digital", "SR Oliveira Maciel", "Vee One", )
setores = ("Administrativo", "Atendimento", "Coordenação de Voo", "CTM", "Lavadores", "Limpeza", "Manutenção",  "Manutenção Predial", "Mecânico", "Motorista", "Operações", "Suprimentos", "TI")

# ========== Widgets na Tela ===============

LogoLabel = customtkinter.CTkLabel(pagina_cadastro, image=logo, text=None)

NomeText = customtkinter.CTkLabel(pagina_cadastro, text='Nome:', font=("Arial", 25))

NomeEntry = customtkinter.CTkEntry(pagina_cadastro, width=270, height=8)

EmpresaText = customtkinter.CTkLabel(pagina_cadastro, text="Empresa:", font=("Arial", 25))

EmpresaEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=empresas, width=270, font=("Arial", 15))

SetorText = customtkinter.CTkLabel(pagina_cadastro, text="Setor:", font=("Arial", 25))

SetorEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=setores, width=270, font=("Arial", 15))

Tipo_credencialText = customtkinter.CTkLabel(pagina_cadastro, text="Credencial:", font=("Arial", 25))

Tipo_credencialEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=tipo_credenciais, width=270,  font=("Arial", 15))

ValidadeText = customtkinter.CTkLabel(pagina_cadastro, text="Validade:",  font=("Arial", 25))

ValidadeEntry = customtkinter.CTkEntry(pagina_cadastro, width=270, font=("Arial", 15))

def Cadastrar_credencial():
    Nome = NomeEntry.get()
    Empresa = EmpresaEntry.get()
    Setor = SetorEntry.get()
    Tipo_de_credencial = Tipo_credencialEntry.get()
    Validade = ValidadeEntry.get()

    DataBase.cursor.execute("""
    INSERT INTO Credenciais(Nome, Empresa, Setor, TipoCredencial, Validade) VALUES(?,?,?,?,?)
""", (Nome, Empresa, Setor, Tipo_de_credencial, Validade))
    DataBase.conn.commit()
    messagebox.showinfo(title="Credencial cadastrada", message="Credencial cadastrada com sucesso!")


CadastrarBotao = customtkinter.CTkButton(pagina_cadastro, text="Cadastrar credencial", width=162.5,command=Cadastrar_credencial)

# =============== Widgets na tela ==============

LogoLabel.place(x=55, y=250)
NomeText.place(x=350, y=170)
NomeEntry.place(x=490, y=175)
EmpresaText.place(x=350, y=240)
EmpresaEntry.place(x=490, y=240)
SetorText.place(x=350, y=310)
SetorEntry.place(x=490, y=310)
Tipo_credencialText.place(x=350, y=380)
Tipo_credencialEntry.place(x=490, y=380)
ValidadeText.place(x=350, y=450)
ValidadeEntry.place(x=490, y=450)
CadastrarBotao.place(x=475, y=590)

# ========== Rodar a janela ====================
pagina_cadastro.mainloop()