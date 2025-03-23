import customtkinter
from PIL import Image

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

NomeText = customtkinter.CTkLabel(pagina_cadastro, text='Digite o nome do funcionário:', font=("Arial", 25))

NomeEntry = customtkinter.CTkEntry(pagina_cadastro, width=325)

EmpresaText = customtkinter.CTkLabel(pagina_cadastro, text="Qual a empresa do funcionário?", font=("Arial", 25))

EmpresaEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=empresas, width=325, font=("Arial", 15))

SetorText = customtkinter.CTkLabel(pagina_cadastro, text="Setor:", font=("Arial", 25))

SetorEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=setores, width=325, font=("Arial", 15))

Tipo_credencialText = customtkinter.CTkLabel(pagina_cadastro, text="Qual o tipo de credencial?", font=("Arial", 25))

Tipo_credencialEntry = customtkinter.CTkOptionMenu(pagina_cadastro, values=tipo_credenciais, width=325,  font=("Arial", 15))

ValidadeText = customtkinter.CTkLabel(pagina_cadastro, text="Digite a validade:",  font=("Arial", 25))

ValidadeEntry = customtkinter.CTkEntry(pagina_cadastro, width=325)


# =============== Widgets na tela ==============

LogoLabel.place(x=285, y=10)
NomeText.place(x=250, y=190)
NomeEntry.place(x=250, y=230)
EmpresaText.place(x=250, y=280)
EmpresaEntry.place(x=250, y=320)
SetorText.place(x=250, y=370)
SetorEntry.place(x=250, y=410)
Tipo_credencialText.place(x=250, y=460)
Tipo_credencialEntry.place(x=250, y=500)
ValidadeText.place(x=250, y=550)
ValidadeEntry.place(x=250, y=590)

# ========== Rodar a janela ====================
pagina_cadastro.mainloop()