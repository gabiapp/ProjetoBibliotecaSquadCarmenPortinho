import sqlite3
conexao = sqlite3.connect('biblioteca.db')

type(conexao)
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE livros( idlivro INTEGER NOT NULL, titulo VARCHAR (100) NOT NULL, descricao VARCHAR (100) NOT NULL, idexemplar INTEGER NOT NULL, id_autor VARCHAR (100) NOT NULL , id_genero VARCHAR (100) NOT NULL, status VARCHAR (10) NOT NULL, editora VARCHAR(100) NOT NULL, PRIMARY KEY (idlivro))')

#cursor.execute('CREATE TABLE usuario( idusuario INTEGER NOT NULL, nome VARCHAR (100) NOT NULL, telefone VARCHAR (12) NOT NULL, nacionalidade VARCHAR(20) NOT NULL, PRIMARY KEY (idusuario))')

#cursor.execute('CREATE TABLE historico ( idhistorico INTEGER NOT NULL, idusuario INTEGER NOT NULL, data_emprestimo DATE NOT NULL, idexemplar INTEGER NOT NULL, data_devolucao DATE NOT NULL, quantidade_renovacao INTEGER NOT NULL, PRIMARY KEY (idhistorico), FOREIGN KEY(idusuario) REFERENCES usuario(idusuario), FOREIGN KEY(idexemplar) REFERENCES livro(idexemplar))')

#cursor.execute('DROP TABLE usuario')

conexao.commit() 
conexao.close

