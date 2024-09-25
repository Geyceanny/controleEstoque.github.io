from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.uic.properties import QtCore

import psycopg2
from colorama import Cursor

con = psycopg2.connect(database="sistema",
                         host="localhost",
                         user="postgres",
                         password="felicidade",
                         port="5432");

def cadastro_marcas():
    linha1 = tela_cadastro_marcas.lineEdit_4.text().strip()
    cur = con.cursor()
    if (linha1 is not None and linha1 !=''):
        dados=(str(linha1))
        marca_existente = "select nome from marcas where nome ilike '%s'"
        cur.execute(marca_existente % dados)
        cur.fetchall()
        existe = cur.rowcount
        if existe>0:
            QMessageBox.about(tela_cadastro_marcas, "Alerta", "Essa marca já existe !")
        else:
            try:
                sql="INSERT INTO marcas (nome) VALUES ('%s')"
                dados = (str(linha1))
                cur.execute(sql % dados)
                con.commit()
                QMessageBox.about(tela_cadastro_marcas, "Sucesso", "Marca cadastrada com sucesso !")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Erro ao conectar com o banco de dados.")
            finally:
                tela_cadastro_marcas.lineEdit_4.setText("")
                tela_cadastro_marcas.close();
    else:
        QMessageBox.about(tela_cadastro_categorias,"Alerta","Nome da marca não pode ser em branco !")

    #Limpar os campos após enviar os dados
    #tela_cadastro_marcas.lineEdit_4.setText("")
    #Fechar a tela após cadastrar
    tela_cadastro_marcas.close()

def carregar_marcas():
    cur = con.cursor()
    sql_marcas = "select id,nome from marcas order by nome"
    cur.execute(sql_marcas)
    marcas_lidas = cur.fetchall()
    marcas_dic = dict(marcas_lidas)
    tela_cadastro_produtos.comboBox.clear()
    tela_cadastro_produtos.comboBox.addItems(marcas_dic.values())

def tela_cadastro_marcas():
    tela_cadastro_marcas.show()

def cadastro_categorias():
    linha1 = tela_cadastro_categorias.lineEdit_5.text().strip()
    cur = con.cursor()

    if (linha1 is not None and linha1 !=''):
        dados=(str(linha1))
        categoria_existente = "select nome from categorias where nome ilike '%s'"
        cur.execute(categoria_existente % dados)
        cur.fetchall()
        existe = cur.rowcount
        if existe>0:
            QMessageBox.about(tela_cadastro_categorias, "Alerta", "Essa categoria já existe !")
        else:
            try:
                sql="INSERT INTO categorias (nome) VALUES ('%s')"
                dados = (str(linha1))
                cur.execute(sql % dados)
                con.commit()
                QMessageBox.about(tela_cadastro_categorias, "Sucesso", "Categoria cadastrada com sucesso !")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Erro ao conectar com o banco de dados.")
            finally:
                tela_cadastro_categorias.lineEdit_5.setText("")
                tela_cadastro_categorias.close()
    else:
        QMessageBox.about(tela_cadastro_categorias,"Alerta","Nome da categoria não pode ser em branco !")


def carregar_categorias():
    cur = con.cursor()
    sql_categorias = "select id,nome from categorias order by nome"
    cur.execute(sql_categorias)
    categorias_lidas = cur.fetchall()
    categorias_dic = dict(categorias_lidas)
    tela_cadastro_produtos.comboBox_2.clear()
    tela_cadastro_produtos.comboBox_2.addItems(categorias_dic.values())

def tela_cadastro_categorias():
    tela_cadastro_categorias.show()

def cadastro_produtos():
    carregar_categorias()
    carregar_marcas()
    linha1 = tela_cadastro_produtos.lineEdit.text().strip()
    print("Linha 1 ok")
    linha2 = tela_cadastro_produtos.comboBox.text()
    print("Linha 2 ok")
    linha3 = tela_cadastro_produtos.comboBox_2.text()
    print("Linha 3 ok")
    linha4 = tela_cadastro_produtos.lineEdit_2.text()
    linha5 = tela_cadastro_produtos.lineEdit_3.text()

    cur = con.cursor()
    if (linha1 is not None and linha1 != ''):
        dados = (str(linha1))
        produto_existente = "select nome from produtos where nome ilike '%s'"
        cur.execute(produto_existente % dados)
        cur.fetchall()
        produto_existe = cur.rowcount
        if produto_existe > 0:
            QMessageBox.about(tela_cadastro_produtos, "Alerta", "Esse produto já existe !")
        else:
            try:
                    sql="INSERT INTO produtos (nome,id_marca,id_categoria,estoque,valor_venda,data_cadastro) VALUES ('%s','%s','%s','%s','%s',now())"
                    dados = (str(linha1),str(values[linha2]),str(values[linha3]),str(linha4),str(linha5))
                    cur.execute(sql % dados)
                    con.commit()
                    QMessageBox.about(tela_cadastro_categorias, "Sucesso", "Produto cadastrado com sucesso !")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Erro ao conectar com o banco de dados.")
            finally:
                #tela_cadastro_produtos.lineEdit.setText("")
                tela_cadastro_produtos.close()
    else:
        QMessageBox.about(tela_cadastro_produtos, "Alerta", "Nome do produto não pode ser em branco !")
    #Limpar os campos após enviar os dados
    #tela_cadastro_produtos.lineEdit.setText("")
    #tela_cadastro_produtos.lineEdit_2.setText("")
    #tela_cadastro_produtos.lineEdit_3.setText("")
        tela_cadastro_produtos.close();


def tela_cadastro_produtos():
    tela_cadastro_produtos.show()
    carregar_marcas()
    carregar_categorias()


def tela_consulta_produtos():
    tela_consulta_produtos.show()
    cur = con.cursor()
    sql = "select p.id,p.nome,p.estoque,p.data_cadastro,c.nome,m.nome,p.preco_venda from produtos p inner join marcas m on p.id_marca = m.id inner join categorias c on p.id_categoria = c.id order by p.nome"
    cur.execute(sql)
    dados_lidos = cur.fetchall()

    tela_consulta_produtos.tableWidget.setRowCount(len(dados_lidos))
    tela_consulta_produtos.tableWidget.setColumnCount(7)
    for i in range(0,len(dados_lidos)):
        for j in range(0,7):
            tela_consulta_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    #Parte para pesquisar o produto, mas ainda não consegui implementar
    #produtos = "select nome from produtos"
    #nome_produto = QStandardItemModel(len(produtos),1)
    #nome_produto.setHorizontalHeaderLabels(['nome'])

    #for linha, produto in enumerate(produtos):
    #    elemento = QStandardItem(produto)
    #    nome_produto.setItem(linha,0, elemento)

    #result = QSortFilterProxyModel()
    #result.setSourceModel(nome_produto)
    #result.setFilterKeyColumn(0)
    #result.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)



app=QtWidgets.QApplication([])
tela_principal=uic.loadUi("tela_principal.ui")
tela_principal.pushButton.clicked.connect(tela_cadastro_marcas)
tela_principal.pushButton_2.clicked.connect(tela_cadastro_categorias)
tela_principal.pushButton_3.clicked.connect(tela_cadastro_produtos)
tela_principal.pushButton_5.clicked.connect(tela_consulta_produtos)
tela_cadastro_marcas=uic.loadUi("cadastro_marcas.ui")
tela_cadastro_marcas.pushButton_2.clicked.connect(cadastro_marcas)

tela_cadastro_categorias=uic.loadUi("cadastro_categorias.ui")
tela_cadastro_categorias.pushButton_3.clicked.connect(cadastro_categorias)

tela_cadastro_produtos=uic.loadUi("cadastro_produtos.ui")
tela_cadastro_produtos.pushButton.clicked.connect(cadastro_produtos)


tela_consulta_produtos=uic.loadUi("consulta_produtos.ui")
#tela_consulta_produtos.tableWidget.setModel(result)
#tela_consulta_produtos.lineEdit.textChanged.connect(result.setFilterRegExp)

tela_principal.show()
app.exec()