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

#Cadastrando livros
# def novo_livro(id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora):
#     cursor.execute('INSERT INTO livros(idlivro ,titulo, descricao, idexemplar, id_autor, id_genero, status, editora) VALUES(?, ?, ?, ?, ?,?,?,?)', (id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora))

# id = int(input("Qual id do livro? "))
# titulo = input("Digite o nome do livro: ")
# id_autor = input("Digite o nome do autor: ")
# descricao = input("De uma descrição do livro: ")
# id_exemplar = int(input("Digite a quantidade de exemplares: "))
# id_genero = input("Qual genero do livro? ")
# status = input("Qual o Status do livro(disponivel/indisponivel): ")
# editora = input("Qual a editora do livro? ")

# novo_livro(id ,titulo, descricao, id_exemplar, id_autor, id_genero, status, editora)

'''#Cadastrando usuario
def novo_user(id ,nome, telefone, nacionalidade):
    cursor.execute('INSERT INTO usuario(idusuario ,nome, telefone, nacionalidade) VALUES(?, ?, ?, ?)', (id ,nome, telefone, nacionalidade))

id = int(input("Qual id do usuario? "))
nome = input("Digite o nome do usuario: ")
telefone = input("Digite seu numero de telefone com DDD: ")
nacionalidade = input("Digite sua nacionalidade: ")

novo_user(id ,nome, telefone, nacionalidade)'''

from datetime import datetime, timedelta

# def emprestar_livro(id_usuario, id_livro):

#         data_emprestimo = datetime.now().strftime('%Y-%m-%d')
#         data_devolucao = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

#         cursor.execute('UPDATE livros SET status=?, idexemplar=idexemplar-1 WHERE idlivro=?', ('emprestado', id_livro))
#         cursor.execute('INSERT INTO historico (idusuario, data_emprestimo, idexemplar, data_devolucao, quantidade_renovacao) VALUES (?, ?, ?, ?, 0)', (id_usuario, data_emprestimo, id_livro, data_devolucao))
#         conexao.commit()

#         print("Livro emprestado com sucesso!")

# id_usuario = int(input("Digite o ID do usuário: "))
# id_livro_emprestado = int(input("Digite o ID do livro a ser emprestado: "))
# emprestar_livro(id_usuario, id_livro_emprestado) 


# def devolver_livro(id_usuario, id_livro):

#         data_devolucao = datetime.now().strftime('%Y-%m-%d')
#         cursor.execute('UPDATE livros SET status=?, idexemplar=idexemplar+1 WHERE idlivro=?', ('disponivel', id_livro))
#         cursor.execute('UPDATE historico SET data_devolucao=? WHERE idexemplar=? AND idusuario=? AND data_devolucao IS NULL', (data_devolucao, id_livro, id_usuario))
  

#         print("Livro devolvido com sucesso!")

# id_usuario_devolucao = int(input("Digite o ID do usuário: "))
# id_livro_devolvido = int(input("Digite o ID do livro a ser devolvido: "))
# devolver_livro(id_usuario_devolucao, id_livro_devolvido)

def excluir_livro_por_id(id_livro):
   
    
        cursor.execute('DELETE FROM livros WHERE idlivro = ?', (id_livro,))
        
        print("Livro excluído com sucesso!")


id_livro = int(input("Digite o ID do livro para excluir: "))
excluir_livro_por_id(id_livro)

conexao.commit() 
conexao.close