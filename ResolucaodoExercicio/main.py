from datetime import datetime
import sqlite3
import uuid
from abc import ABC, abstractmethod

conexao = sqlite3.connect('biblioteca_poo.db')
cursor = conexao.cursor()


class LivroAbstrato(ABC):
  @abstractmethod
  def __init__(self, titulo, autor, editora, genero, qtd_exemplares):
      self.titulo = titulo
      self.autor = autor
      self.editora = editora
      self.genero = genero
      self.qtd_exemplares = qtd_exemplares

  @abstractmethod
  def cadastrar_livro(self, conexao, titulo, autor, editora, genero, qtd_exemplares):
      pass

  @abstractmethod
  def emprestar(self, conexao, titulo, id_usuario, data_emprestimo, data_devolucao):
      pass

  @abstractmethod
  def devolver(self, conexao, titulo, data_devolucao):
      pass
  
class Livro(LivroAbstrato):
    def __init__(self, titulo, autor, editora, genero, qtd_exemplares):
        super().__init__(titulo, autor, editora, genero, qtd_exemplares)
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.genero = genero
        self.qtd_exemplares = qtd_exemplares

    #função que adiciona livro
    def cadastrar_livro(self, titulo, autor, editora, genero, qtd_exemplares):
        cursor.execute("INSERT INTO Livro(titulo, autor, editora, genero, qtd_exemplares)\
                VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, genero, qtd_exemplares))
        conexao.commit() #registra mudança
        conexao.close() #fecha conexão

   #funcão que realiza empréstimo
    def emprestar(self, titulo, id_usuario, data_emprestimo, data_devolucao):
      cursor = conexao.cursor()
      cursor.execute("SELECT qtd_exemplares FROM Livro WHERE titulo = ?", (titulo,))
      livro = cursor.fetchone()

      if livro is None or livro[0] <= 0:
          print("Não existem mais exemplares disponíveis, por favor, busque por outro título")
      else:
          cursor.execute("INSERT INTO emprestimos(titulo, id_usuario, data_emprestimo, data_devolucao) VALUES(?, ?, ?, ?)", (titulo, id_usuario, data_emprestimo, data_devolucao))
          cursor.execute('UPDATE Livro SET qtd_exemplares = qtd_exemplares - 1 WHERE titulo = ?', (titulo,))
          conexao.commit()
          conexao.close()


    #função que atualiza data de devolução de empréstimo
    def devolver(self, titulo, data_devolucao):
        cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE titulo = ?", (data_devolucao, titulo) )
        cursor.execute('UPDATE Livro SET qtd_exemplares = qtd_exemplares + 1 WHERE titulo = ?', (titulo,))
        conexao.commit()
        conexao.close()


class Biblioteca:

    def cadastrar_usuario(self, id, nome, nacionalidade, telefone):
        conexao = sqlite3.connect('biblioteca_poo.db')
        conexao.execute("INSERT INTO Usuario (id, nome, nacionalidade, telefone) VALUES (?,?,?,?)",(id, nome, nacionalidade, telefone))
        conexao.commit()
        conexao.close()

    #função que lista todos os livros cadastrados
    def listar_livros(self):
        livros = conexao.execute("SELECT * FROM Livro").fetchall()
        print(livros)
        conexao.close()

    #funcão que exibe lista de livros emprestados
    def historico_emprestimos(self):
        result = cursor.execute("SELECT Livro.titulo, Usuario.nome, Emprestimos.data_emprestimo, Emprestimos.data_devolucao\
                                        FROM Livro\
                                        INNER JOIN Emprestimos ON Livro.titulo = Emprestimos.titulo\
                                        INNER JOIN Usuario ON Usuario.id = Emprestimos.id_usuario\
                                        WHERE Emprestimos.data_devolucao IS NOT NULL").fetchall()
        #conexao.execute('UPDATE Livro SET exemplares = exemplares + 1 WHERE id = ?', (id,))
        conexao.close()
        print(result)


biblioteca_womakers = Biblioteca()
livro_01 = Livro("", "", "", "", "")

menu  = '''------------Biblioteca------------
1- Cadastrar usuário
2- Cadastrar livros
3- Emprestar livros
4- Devolver livros
5- Listar livros
6- Historico de emprestimos
'''

print(menu)
opcao = input("Digite a opção desejada: ")


if opcao == "1":
  print("Ok vamos cadastar um novo user")
  id = str(uuid.uuid4())
  nome = input("Digite seu nome: ")
  nacionalidade = input("Digite sua nacionalidade: ")
  telefone = input("Digite seu telefone: ")
  biblioteca_womakers.cadastrar_usuario(id, nome, nacionalidade, telefone)

elif opcao == "2":
  print("Ok vamos cadastar um novo livro")
  titulo = input("Qual o titulo do livro: ")
  autor = input("Digite o nome do autor do livro: ")
  editora = input("Digite o nome da editora do livro: ")
  genero = input("Digite o genero do livro: ")
  qtd_exemplares = int(input("Digite a quantidade de exemplares: "))
  livro_01.cadastrar_livro(titulo, autor, editora, genero, qtd_exemplares)

elif opcao == "3":
  print("Ok qual voce quer emprestado")
  titulo = input("Digite o título do livro: ")
  id_usuario = input("Insira o id do usuario: ")
  data_emprestimo = input("Digite a data de emprestimo: ")
  data_devolucao = input("Digite a data de devolução: ")
  livro_01.emprestar(titulo, id_usuario, data_emprestimo, data_devolucao)

elif opcao == "4":
  print("Qual voce vai devolver?")
  titulo = input("Digite o título do livro emprestado: ")
  data_devolucao = input("Insira a data de devolução: ")
  livro_01.devolver(titulo, data_devolucao)

  
elif opcao == "5":
  print("Ok são nossos livros")
  biblioteca_womakers.listar_livros()

elif opcao == "6":
  print("Ok esse é nosso historico")
  biblioteca_womakers.historico_emprestimos()

else:
  print("Essa opção não existe")