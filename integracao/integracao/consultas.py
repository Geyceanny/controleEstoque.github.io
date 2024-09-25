import psycopg2;

con = psycopg2.connect(database="sistema",
                         host="localhost",
                         user="postgres",
                         password="felicidade",
                         port="5432");

#Realizar consulta de marcas
def consulta_marcas():
    cur = con.cursor()
    with con.cursor() as c:
        sql="select * from marcas"
        cur.execute(sql)

        #Metodo fetchaLL(): Retorna todas as linhas obtidas pela consulta na tabela
        res = cur.fetchall()

        #Mostrar os dados retornados
        print(res)

        con.commit()


def consulta_categorias():
    cur = con.cursor()
    with con.cursor() as c:
        sql="select * from categorias"
        cur.execute(sql)

        #Metodo fetchaLL(): Retorna todas as linhas obtidas pela consulta na tabela
        res = cur.fetchall()

        #Mostrar os dados retornados
        print(res)

        con.commit()

def consulta_produtos():
    cur = con.cursor()
    with con.cursor() as c:
        sql="select * from produtos"
        cur.execute(sql)

        #Metodo fetchaLL(): Retorna todas as linhas obtidas pela consulta na tabela
        res = cur.fetchall()

        #Mostrar os dados retornados
        print(res)

        con.commit()


import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("500x400+200+100")
janela.config(bg="lightgrey")
janela.resizable(True,True)

botao_consultamarca = tk.Button(janela, text="Consultar Marcas", command=consulta_marcas, bg='lightblue', fg='black')
botao_consultamarca.pack(pady=50)

botao_consultacategoria = tk.Button(janela, text="Consultar Categorias", command=consulta_categorias, bg='lightblue', fg='black')
botao_consultacategoria.pack(pady=50)

botao_consultaproduto = tk.Button(janela, text="Consultar Produtos", command=consulta_produtos, bg='lightblue', fg='black')
botao_consultaproduto.pack(pady=50)

#Exibir a janela
janela.mainloop()

con.close()


