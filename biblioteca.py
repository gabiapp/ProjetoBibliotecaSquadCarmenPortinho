import sqlite3
conexao = sqlite3.connect('biblioteca.db')

type(conexao)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE livros( idlivro INTEGER NOT NULL, titulo VARCHAR (100) NOT NULL, descricao VARCHAR (100) NOT NULL, idexemplar INTEGER NOT NULL, id_autor VARCHAR (100) NOT NULL , id_genero VARCHAR (100) NOT NULL, status VARCHAR (10) NOT NULL, editora VARCHAR(100) NOT NULL, PRIMARY KEY (idlivro))')

#cursor.execute('CREATE TABLE usuario( idusuario INTEGER NOT NULL, nome VARCHAR (100) NOT NULL, telefone VARCHAR (12) NOT NULL, nacionalidade VARCHAR(20) NOT NULL, PRIMARY KEY (idusuario))')

#cursor.execute('CREATE TABLE historico ( id_historico INTEGER NOT NULL, data_emprestimo DATE NOT NULL, data_devolucao DATE NOT NULL, quantidade_renovacao INTERGER NOT NULL, PRIMARY KEY id_historico, FOREIGN KEY(idusuario) REFERENCER usuario(idusuario), FOREIGN KEY(idexemplar) REFERENCER livro(idexemplar))')

#cursor.execute('DROP TABLE livro')


conexao.commit() 
conexao.close
