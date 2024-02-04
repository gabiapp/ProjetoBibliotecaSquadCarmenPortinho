import sqlite3
conexao = sqlite3.connect('biblioteca.db')

type(conexao)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE livro( idlivro INTEGER PRIMARY KEY , titulo VARCHAR(100), editora VARCHAR(100), max_renovacao INTEGER)')

cursor.execute('CREATE TABLE exemplar( idexemplar INTEGER PRIMARY KEY, FOREIGN KEY (idlivro) REFERENCES livro(idlivro), status VARCHAR(10))')

cursor.execute('CREATE TABLE usuario( idusuario INTEGER PRIMARY KEY, telefone VARCHAR (12), nacionalidade VARCHAR(20))')

cursor.execute('CREATE TABLE autor_livro( FOREIGN KEY (idlivro) REFERENCES livro(idlivro), id_autor INTEGER PRIMARY KEY )')

cursor.execute('CREATE TABLE genero_livro( FOREIGN KEY (idlivro) REFERENCES livro(idlivro), id_genero INTEGER PRIMARY KEY)')

cursor.execute('CREATE TABLE historico ( id_historico INTEGER PRIMARY KEY, FOREIGN KEY (idusuario) REFERENCES usuario(idusuario), FOREIGN KEY (idexemplar) REFERENCES exemplar(idexemplar), data_emprestimo DATE NOT NULL, data_devolucao DATE NOT NULL, quantidade_renovacao INTERGER)')

cursor.execute('CREATE TABLE usuario( FOREIGN KEY (id_autor) REFERENCES autor_livro(id_autor), nome VARCHAR (100))')

cursor.execute('CREATE TABLE genero( OREIGN KEY (id_genero) REFERENCES genero_livro(id_genero), descricao VARCHAR (100))')


conexao.commit() 
conexao.close
