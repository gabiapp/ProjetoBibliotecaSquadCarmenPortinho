'''
TABLE livros( idlivro INTEGER NOT NULL, 
titulo VARCHAR (100) NOT NULL, 
descricao VARCHAR (100) NOT NULL, 
idexemplar INTEGER NOT NULL, 
id_autor VARCHAR (100) NOT NULL , 
id_genero VARCHAR (100) NOT NULL, 
status VARCHAR (10) NOT NULL, 
editora VARCHAR(100) NOT NULL, 
PRIMARY KEY (idlivro))')
'''

import sqlite3

#conectando
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

'''#Cadastrando livros
def novo_livro(id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora):
    cursor.execute('INSERT INTO livros(idlivro ,titulo, descricao, idexemplar, id_autor, id_genero, status, editora) VALUES(?, ?, ?, ?, ?,?,?,?)', (id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora))

id = int(input("Qual id do livro? "))
titulo = input("Digite o nome do livro: ")
id_autor = input("Digite o nome do autor: ")
descricao = input("De uma descrição do livro: ")
id_exemplar = int(input("Digite a quantidade de exemplares: "))
id_genero = input("Qual genero do livro? ")
status = input("Qual o Status do livro(disponivel/indisponivel): ")
editora = input("Qual a editora do livro? ")

novo_livro(id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora)'''

#Cadastrando usuario
def novo_user(id ,nome, telefone, nacionalidade):
    cursor.execute('INSERT INTO usuario(idusuario ,nome, telefone, nacionalidade) VALUES(?, ?, ?, ?)', (id ,nome, telefone, nacionalidade))

id = int(input("Qual id do usuario? "))
nome = input("Digite o nome do usuario: ")
telefone = input("Digite seu numero de telefone com DDD: ")
nacionalidade = input("Digite sua nacionalidade: ")

novo_user(id ,nome, telefone, nacionalidade)

conexao.commit() 
conexao.close