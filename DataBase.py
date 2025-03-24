import sqlite3

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Credenciais(
    Id INTEGER NOT NULL PRIMARY KEY,        
    Nome TEXT NOT NULL,
    Empresa TEXT NOT NULL,
    Setor TEXT NOT NULL,
    TipoCredencial TEXT NOT NULL,       
    Validade DATE NOT NULL
);
""")


print("conectado")