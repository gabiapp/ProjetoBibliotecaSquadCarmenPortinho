from datetime import datetime
import sqlite3
import uuid
from abc import ABC, abstractmethod


class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade


class Livro(ABC):
    def __init__(self, titulo, editora, generos, max_renovacoes):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.max_renovacoes = max_renovacoes
        self.exemplares_disponiveis = []
        self.exemplares_emprestados = []

    def adicionar_exemplar(self, quantidade):
        for _ in range(quantidade):
            exemplar = Exemplar(self)
            self.exemplares_disponiveis.append(exemplar)

    def calcular_qtd_disponiveis(self):
        return len(self.exemplares_disponiveis)

    def calcular_qtd_emprestados(self):
        return len(self.exemplares_emprestados)

    def calcular_qtd_devolvidos(self):
        return len([exemplar for exemplar in self.exemplares_emprestados if exemplar.status == "Devolvido"])

    def emprestar_exemplar(self):
        if self.exemplares_disponiveis:
            exemplar_emprestimo = self.exemplares_disponiveis.pop(0)
            exemplar_emprestimo.emprestar()
            self.exemplares_emprestados.append(exemplar_emprestimo)
            return exemplar_emprestimo
        else:
            return None

    def devolver_exemplar(self, exemplar):
        if exemplar in self.exemplares_emprestados:
            exemplar.devolver()
            self.exemplares_emprestados.remove(exemplar)
            self.exemplares_disponiveis.append(exemplar)

    @abstractmethod
    def funcao_abstrata(self):
        pass


class Exemplar:
    def __init__(self, livro):
        self.id = str(uuid.uuid4())
        self.livro = livro
        self.status = "Disponível"  # Incluímos o atributo "status" e inicializamos como "Disponível"

    def emprestar(self):
        if self.status == "Disponível":
            self.status = "Emprestado"
            return True
        else:
            return False

    def devolver(self):
        self.status = "Disponível"


class Emprestimo:
    def __init__(self, exemplar, usuario):
        self.id = str(uuid.uuid4())
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def emprestar(self):
        if self.exemplar.emprestar():
            self.data_emprestimo = datetime.now()
            return True
        else:
            return False

    def devolver(self):
        if self.exemplar.status == "Emprestado":
            self.exemplar.devolver()
            self.data_devolucao = datetime.now()
            return True
        else:
            return False

    def __str__(self):
        return f"Empréstimo - ID: {self.id}, Livro: {self.exemplar.livro.titulo}, " \
               f"ID do Exemplar: {self.exemplar.id}, " \
               f"Usuário: {self.usuario.nome}, " \
               f"Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {self.data_devolucao}"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos_realizados = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        conexao = sqlite3.connect('biblioteca_poo.db')
        conexao.execute("INSERT INTO Usuario (id, nome, telefone, nacionalidade) VALUES (?,?,?,?)",
                        (usuario.id, usuario.nome, usuario.telefone, usuario.nacionalidade))
        conexao.commit()
        conexao.close()

    def realizar_emprestimo(self, livro, usuario):
        exemplar_emprestimo = livro.emprestar_exemplar()
        if exemplar_emprestimo:
            emprestimo = Emprestimo(exemplar_emprestimo, usuario)
            self.emprestimos_realizados.append(emprestimo)
            return emprestimo
        else:
            return None

    def realizar_devolucao(self, emprestimo):
        emprestimo.exemplar.livro.devolver_exemplar(emprestimo.exemplar)
        emprestimo.data_devolucao = datetime.now()
        self.emprestimos_realizados.remove(emprestimo)
        print(emprestimo) 

    def exibir_estado_exemplares(self):
        for livro in self.livros:
            print(f"\nLivro: {livro.titulo} - Disponiveis: {livro.calcular_qtd_disponiveis()} - Emprestado: {livro.calcular_qtd_emprestados()}") 
            for exemplar in livro.exemplares_disponiveis:
                print(f"Exemplar ID: {exemplar.id}, Status: {exemplar.status}")
            for exemplar in livro.exemplares_emprestados:
                print(f"Exemplar ID: {exemplar.id}, Status: {exemplar.status}")

    def listar_emprestimos(self):
        for emprestimo in self.emprestimos_realizados: 
            print(emprestimo) 


class LivroConcreto(Livro):
    def funcao_abstrata(self):
        pass


# Exemplo de uso
biblioteca = Biblioteca()

# Criar usuários
usuarios = [
    Usuario("Alyne", "123456789", "Italiana"),
    Usuario("Ana Maria", "987654321", "Francesa"),
    Usuario("Cibele", "987654323", "Portuguesa"),
    Usuario("Daniele", "987654322", "Indiana"),
    Usuario("Gessyca", "987654324", "Norueguesa"),
    Usuario("Gabriela", "987654325", "Canadense"),
    Usuario("Renata", "987654326", "chinesa"),
    Usuario("Lívia", "987654327", "Japonesa"),
    Usuario("Laura", "987654328", "Americana"),
    Usuario("Thayná", "987654329", "Brasileira")
]

# Criar livros
livros = [
    LivroConcreto("1984", "Companhia das Letras", ["Distopia"], 3),
    LivroConcreto("O Senhor dos Anéis: A Sociedade do Anel", "Martins Fontes", ["Fantasia"], 4),
    LivroConcreto("Orgulho e Preconceito", "Zahar", ["Romance Clássico"], 5),
    LivroConcreto("Neuromancer", "Aleph", ["Cyberpunk"], 3),
    LivroConcreto("A Menina que Roubava Livros", "Intrínseca", ["Drama Histórico"], 4),
    LivroConcreto(" Uma Breve História da Humanidade", "L&PM Editores", ["Não Ficção/História"], 5),
    LivroConcreto("O Código Da Vinci", "Arqueiro", ["Suspense"], 3),
    LivroConcreto("Flores para Algernon", "Aleph", ["Ficção Científica"], 4),
    LivroConcreto("A Cor Púrpura", "Globo Livros", ["Ficção Literária"], 5),
    LivroConcreto("Maus", "Quadrinhos na Cia", ["Graphic Novel (História em Quadrinhos)"], 3)
]

# Adicionar exemplares aos livros
for livro in livros:
    livro.adicionar_exemplar(5)

# Cadastrar livros na biblioteca
for livro in livros:
    biblioteca.cadastrar_livro(livro)

# Cadastrar usuários na biblioteca
for usuario in usuarios:
    biblioteca.cadastrar_usuario(usuario)

# Exibir estado dos exemplares antes dos empréstimos
biblioteca.exibir_estado_exemplares()

emprestimo = biblioteca.realizar_emprestimo(livros[0], usuarios[0])
emprestimo = biblioteca.realizar_emprestimo(livros[0], usuarios[1])
emprestimo = biblioteca.realizar_emprestimo(livros[0], usuarios[2])
emprestimo = biblioteca.realizar_emprestimo(livros[1], usuarios[3])
emprestimo = biblioteca.realizar_emprestimo(livros[1], usuarios[4])
emprestimo = biblioteca.realizar_emprestimo(livros[2], usuarios[5])
emprestimo = biblioteca.realizar_emprestimo(livros[2], usuarios[6])
emprestimo = biblioteca.realizar_emprestimo(livros[2], usuarios[7])
emprestimo = biblioteca.realizar_emprestimo(livros[2], usuarios[8])
emprestimo = biblioteca.realizar_emprestimo(livros[3], usuarios[9])
emprestimo = biblioteca.realizar_emprestimo(livros[4], usuarios[0])
emprestimo = biblioteca.realizar_emprestimo(livros[4], usuarios[1])
emprestimo = biblioteca.realizar_emprestimo(livros[4], usuarios[2])
emprestimo = biblioteca.realizar_emprestimo(livros[5], usuarios[3])
emprestimo = biblioteca.realizar_emprestimo(livros[5], usuarios[4])
emprestimo = biblioteca.realizar_emprestimo(livros[6], usuarios[5])
emprestimo = biblioteca.realizar_emprestimo(livros[7], usuarios[6])
emprestimo = biblioteca.realizar_emprestimo(livros[7], usuarios[7])
emprestimo = biblioteca.realizar_emprestimo(livros[8], usuarios[8])
emprestimo = biblioteca.realizar_emprestimo(livros[8], usuarios[9])
emprestimo = biblioteca.realizar_emprestimo(livros[8], usuarios[0])
emprestimo = biblioteca.realizar_emprestimo(livros[9], usuarios[1])
emprestimo = biblioteca.realizar_emprestimo(livros[9], usuarios[2])
emprestimo = biblioteca.realizar_emprestimo(livros[9], usuarios[3])
emprestimo = biblioteca.realizar_emprestimo(livros[9], usuarios[4])

    
for _ in range(5):
    biblioteca.realizar_devolucao(biblioteca.emprestimos_realizados[0])

# Exibir estado dos exemplares após os empréstimos
biblioteca.exibir_estado_exemplares()

# Exibir lista de empréstimos realizados
print("\nLista de empréstimos realizados:")
biblioteca.listar_emprestimos()
