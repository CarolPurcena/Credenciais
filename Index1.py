import customtkinter
from PIL import Image
import DataBase
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# =========================== JANELA ==========================

pagina_inicial = customtkinter.CTk()
pagina_inicial.title("Credenciais")
pagina_inicial.resizable(width=False, height=False)
pagina_inicial.geometry("400x400")
pagina_inicial.iconbitmap(default=("imgs/OmniLogo.ico"))

# =============== IMAGENS ===============
logo = customtkinter.CTkImage(Image.open("imgs/Omni.png"), size=(250,150))

# ============== WIDGETS ==================
LogoLabel = customtkinter.CTkLabel(pagina_inicial, image=logo, text=None)

def Cadastro():
    # REMOVER PAGINA ANTERIOR
    CadastrarBotao.place(x=5000, y=5000)
    LogoLabel.place(x=55, y=250)

    # ============================
    pagina_inicial.geometry("800x700")
    pagina_inicial.title("Cadastro de Credenciais")

    # ================ Listas ===================
    tipo_credenciais = ("Temporária", "Permanente", "Visitante")
    empresas = ("Omni Táxi Aéreo", "Maricá Offshore", "MR&Services", "Quality Digital", "SR Oliveira Maciel", "Vee One", )
    setores = ("Administrativo", "Atendimento", "Coordenação de Voo", "CTM", "Lavadores", "Limpeza", "Manutenção",  "Manutenção Predial", "Mecânico", "Motorista", "Operações", "Suprimentos", "TI")

    # ================== WIDGETS ================
    NomeText = customtkinter.CTkLabel(pagina_inicial, text='Nome:', font=("Arial", 25))
    NomeEntry = customtkinter.CTkEntry(pagina_inicial, width=270, height=8, font=("Arial", 15))
    EmpresaText = customtkinter.CTkLabel(pagina_inicial, text="Empresa:", font=("Arial", 25))
    EmpresaEntry = customtkinter.CTkOptionMenu(pagina_inicial, values=empresas, width=270, font=("Arial", 15))
    SetorText = customtkinter.CTkLabel(pagina_inicial, text="Setor:", font=("Arial", 25))
    SetorEntry = customtkinter.CTkOptionMenu(pagina_inicial, values=setores, width=270, font=("Arial", 15))
    Tipo_credencialText = customtkinter.CTkLabel(pagina_inicial, text="Credencial:", font=("Arial", 25))
    Tipo_credencialEntry = customtkinter.CTkOptionMenu(pagina_inicial, values=tipo_credenciais, width=270,  font=("Arial", 15))
    ValidadeText = customtkinter.CTkLabel(pagina_inicial, text="Validade:",  font=("Arial", 25))
    ValidadeEntry = customtkinter.CTkEntry(pagina_inicial, width=270, font=("Arial", 15), height=8)

    # ================= FUNÇÕES =================
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

    # ================== BOTÕES ================
    Cadastrar_CredencialBotao = customtkinter.CTkButton(pagina_inicial, text="Cadastrar credencial", width=162.5,command=Cadastrar_credencial)

    # ================= WIDGETS NA TELA ===============
    NomeText.place(x=350, y=170)
    NomeEntry.place(x=490, y=175)
    EmpresaText.place(x=350, y=240)
    EmpresaEntry.place(x=490, y=240)
    SetorText.place(x=350, y=310)
    SetorEntry.place(x=490, y=310)
    Tipo_credencialText.place(x=350, y=380)
    Tipo_credencialEntry.place(x=490, y=380)
    ValidadeText.place(x=350, y=450)
    ValidadeEntry.place(x=490, y=455)
    Cadastrar_CredencialBotao.place(x=475, y=590)

CadastrarBotao = customtkinter.CTkButton(pagina_inicial, text="Cadastro", command=Cadastro)

VerificarBotao = customtkinter.CTkButton(pagina_inicial, text="Verificar Credencial")

# ============= WIDGETS NA TELA =================

LogoLabel.place(x=70, y=30)
CadastrarBotao.place(x=135, y=200)

# ========== RODAR A JANELA ==========

pagina_inicial.mainloop()