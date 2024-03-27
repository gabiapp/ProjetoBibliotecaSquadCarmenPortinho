# Feedback
Relatório da análise do projeto da squad Carmen Portinho, com os pontos de acertos e de melhorias.

## Sumário
1. [Apresentação](#apresentacao)
2. [Banco de dados](#banco-de-dados)
3. [Orientação a objetos](#orientacao-a-objetos)

## Apresentação
Tudo bem, gente? Meu nome é Eduardo, sou bacharel em Ciência da Computação, mestrando em Engenharia de Software e dev no time de portfólio-web na globo, e foi um imenso prazer analisar o projeto de vocês, que já adianto, arrasaram demais. Eu tentei contribuir o máximo possível para o projeto e para a evolução de vocês, saibam que estão no caminho certo e acredito que esse é o momento que vai favorecer muito a maturidade técnica da squad como um todo. Caso tenham quaisquer dúvidas, podem entrar em contato comigo (eduardo.jose@g.globo), ou mesmo deixar algum comentário pelo github, por alguma issue, algo do tipo, fica a critério de vocês, mas saibam que estou a disposição.

## Banco de dados

### Aspecto geral
A modelagem final do banco de dados foi muito boa, vocês conseguiram abstrair bem a composição da biblioteca, sem redundância de dados, o que é bem positivo. Além disso, também encontrei espaço para uma evolução que eu vou descrever mais a frente, sendo um aprofundamento na modelagem e não correção.

### Ótima nomenclatura
 Comentando sobre a definição do banco no README e no código, vi que vocês mudaram o nome de `historico` para `emprestimos`, o que eu apoio totalmente. Isso porque a tabela `emprestimos` implicitamente já é o histórico, porém, `emprestimos` já diz a natureza da entidade dentro do sistema de forma direta. Em contrapartida, a tabela `historico` pode ser ampla, podemos ter diversos históricos em uma base de dados, o que pode dificultar o escalamento do projeto ou mesmo a modelagem em bancos mais complexos.

### Alcançando um maior detalhamento e desacoplamento

#### Mudança de abordagem
Durante a análise, eu encontrei um ótimo ponto de evolução na modelagem que vocês podem explorar, que inclusive exploraram. Isso porque na definição do README, vocês tinha abstraído a ideia de `Exemplar` referente a cada exemplar disponível de cada livro, e nesse projeto, essa informação é utilizada para realizar os empréstimos, dizendo se o livro estaria disponível ou não para ser emprestado. Ao invés dessa abordagem, vocês seguiram uma abordagem mais simplificada, mantendo apenas um contador de exemplares na própria tabela `Livro`, e isso está corretíssimo, até porque essa forma já resolve a necessidade do projeto, e esse é o objetivo.

#### Aprofundando o desacoplamento

Voltando a nossa ótica para a abordagem inicial, da tabela de `Exemplar`, podemos aprofundar nos benefícios que ela traz e porque ela representa uma evolução na modelagem do projeto. Quando abstraímos uma tabela, relacionando o `Livro` com a sua unidade física, a gente cria uma camada de desacoplamento, que traz algumas consequências. A primeira delas é a possibilidade de armazenar mais informações, por exemplo, estado da unidade, ano de publicação e se está emprestado. Em contraponto, a gente acaba gerando uma problema de performance na hora de consultar, já que dessa forma, precisaríamos executar `queries` com `COUNT(*)` para sabermos, por exemplo:
 - Quantidade de exemplares
 - Exemplares emprestados
 - Exemplares disponíveis

Para resolver esse problema, poderíamos manter contadores na tabela de `Livro`, atualizando eles a cada unidade criada/emprestada/removida, melhorando muito o custo de consulta. Em um primeiro momento, parece que só dificultamos a implementação da abordagem anterior, já que mantemos os contadores. Porém, nesse caso, teremos os contadores associados com informações adicionais sobre cada unidade, fornecendo, por exemplo, um caminho mais simples para escalar o projeto, principalmente quando levamos para o mundo real, que os softwares sempre estão evoluindo, até porque eles são nada além de ferramentas para as pessoas, e as ferramentas tem que se adequar ao nosso uso e evolução.

### Concluindo a análise da modelagem
Como eu tinha dito, a modelagem do banco realmente está muito boa, então:
 - Meus Parabéns à todas! 🎉

Inclusive foi difícil achar pontos que eu poderia contribuir para evolução dela. Apesar disso, vocês ganharam um ponto que pode ser explorado para evoluir ainda mais a modelagem e eu espero que isso inclusive abra os horizontes para vocês trabalharem pensando mais profundamente nos conceitos de desacoplamento, que apesar de trazer complexidade na estrutura do projeto em que se está trabalhando, fornece muitos benefícios a longo e curto prazo, e não existe nada melhor que trabalhar com um legado bem feito, e querendo ou não, tudo uma hora vai virar legado, e isso não precisa ser sinônimo de defasagem.

## Orientação a objetos
### Visão inicial
Seguindo a análise para o código do projeto, de cara, eu encontrei um código bem organizado e com uma ótima legibilidade. Com isso, eu precisei analisar mais fundo e encontrei alguns pontos para discutirmos. Sendo um pouco mais direto, eu pude encontrar pontos de correção e de evolução, que vamos expandir nos próximos tópicos.

### Quebra do Princípio da Responsabilidade Única (SOLID)
Ao observar a classe `Livro`, eu pude notar uma quebra no princípio da responsabilidade única. Isso se refere a existência dos métodos de empréstimo dentro da classe `Livro`. A classe, em sua definição, se responsabiliza por representar a entidade Livro, e fornecer métodos que podem gerenciá-la. O comportamento de emprestar e devolver, é de uma entidade que recebe um `Livro` e associa com um `Usuario`, dessa forma fica claro que, não é responsabilidade da classe `Livro` e sim da classe `Biblioteca` que recebe os usuários e os associam com os livros. Corrigindo isso, estamos normalizando o projeto com os princípios SOLID, e como benefícios temos: melhoria na legibilidade, coesão no código, encapsulamento, que por fim, contribuem para uma melhor manutenabilidade do projeto a longo e curto prazo.

### Problema de nomenclatura
Na classe `Livro` temos um problema de nomenclatura. Isso porque, ela acaba transmitindo a ideia que a classe `Livro` vai cadastrar um livro, contrariando a sua verdadeira função, que é persistir ele mesmo no banco de dados, além de que `cadastrar_livro` acaba sendo redudante, já que o método já está na classe `Livro`. Então, como sugestão de nomenclatura, podemos usar `salvar()`. Assim, novamente, contribuimos para uma melhor manutenabilidade do código, conseguindo um cenário mais direto do que o método se propõe a fazer.

### Evitando a utilização de if, elif e elses seguidos
Nesse ponto, é importante ressaltarmos a abordagem que foi utilizada para entender qual função o usuário vai acessar através do prompt, que foi a utilização de condições `if` para mapear qual função foi escolhida. Em primeiro lugar, é importante dizer que, não é uma abordagem errada, ela resolve o problema que é proposto. Entretanto, é uma solução com pouco espaço para escalamento, que caso aconteça ou mesmo, a estrutura já seja grande, torna difícil a tarefa de entender o que cada comando faz. Dessa forma, eu propõe a utilização de um design pattern como Command. Nele, a gente define uma classe que vai funcionar como um direcionar de cada comando para sua respectiva função. Assim, temos um código muito bem escalável e ganhamos uma maior legibilidade na hora de entender o que cada comando realiza. Dessa forma, eu vou deixar o pseudocódigo abaixo para vocês entenderam como funcionaria a implementação desse pattern. Vale lembrar que existem diferentes níveis de abstração na hora de implementar, a que eu vou apresentar, é uma abstração mais simples:

```python
class Command:
    # Inicializa o dict de comandos
    def __init__(self):
        self.commands = {}

    # Adiciona o comando e a respectiva função no dict
    def add(self, key, callback):
        if callable(callback):
            self.commands[key] = callback
        else:
            raise ValueError("Callback deve ser uma função")

    # Executa o comando, caso exista, a partir da função armazenada no dict
    def run(self, key):
        if key in self.commands:
            self.commands[key]()
        else:
            raise Exception("Comando não existe")

# Exemplo de utilização
def criaUsuario():
    # Aqui ficam todas os passos para criar um usuário

menu  = '''------------Biblioteca------------
1- Cadastrar usuário
2- Cadastrar livros
3- Emprestar livros
4- Devolver livros
5- Listar livros
6- Historico de emprestimos
'''

command = Command()
command.add('1', criarUsuario)

print(menu)
opcao = input("Digite a opção desejada: ")
command.run(opcao)
```

Dessa forma, a gente não precisa criar várias condições, a leitura fica mais direta, a complexidade de consulta é menor, sendo O(1), mesmo que para poucas opções, a diferença seja praticamente zero, sendo assim, o maior benefício é que, dessa forma, temos uma coleção de comandos muito mais escalável e legível, representando assim, uma ótima evolução.

### Evolução na divisão das responsabilidades
A divisão de responsabilidade não se limita apenas aos princípios SOLID, mas entra também na estrutura dos arquivos. Nesse projeto vocês possuem a oportunidade de separar os componentes do código em arquivos. Por exemplo, é nítido que `Livro` e `Biblioteca` são classes que representam as entidades do sistema, sendo assim, modelos de dados, ou seja, aqui entra o conceito de `models`. Com isso, vocês poderiam separar cada uma das entidades em um arquivo, ficando dessa forma:
  - `ResolucaodoExercicio`
    - `models`
      - `Livro.py`
      - `Biblioteca.py`
    - `modules`
      - `Menu.py`
    - `main.py`

Vocês devem ter notado a criação do arquivo `Menu.py` e existe um propósito. Basicamente, dessa forma que estruturamos, podemos importar os `models` e o módulo dentro do `main.py`, e nesse aquivo, que seria o ponto de entrada da aplicação, a gente realiza a "orquestração" dos nossos componentes do sistema. Dentro `Menu.py` a gente realizaria a definição dos comandos do prompt, associando com as funções respectivas.

Notem que esse tópico, é apenas um passo para evoluir a estutura do projeto que vocês elaboraram e não corrigir, ela traz diversos benefícios, que novamente, contribuem para uma melhor qualidade de manutenção. Além disso, no próprio desenvolvimento, a gente tem uma organização que facilita na hora de codificar os componentes e associá-los, já que, temos "pontos de referência" onde cada um está.

## Conclusão
Vocês brilharam muito nesse projeto, espero que os pontos que eu trouxe ajudem vocês a brilharem cada vez mais. Discutimos pontos muito interessantes para o nosso dia a dia, design patterns, encapsulamento, princípios de orientação a objetos, estruturamento de diretório e separação de conceitos. Lembrem-se que a vida de pessoa desenvolvedora é uma evolução constante, sempre teremos algo para estudar e crescer, tanto como pessoa quanto profissional, e é isso que nos motiva e nos move cada dia. Espero que vocês tenham gostado, novamente, quaisquer dúvidas, mandem pra mim pelo e-mail (eduardo.jose@g.globo) ou pelo GitHub.

Vamos juntos! ❤️

Link de apoio sobre design patterns: https://refactoring.guru/