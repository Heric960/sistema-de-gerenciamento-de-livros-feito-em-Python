import sqlite3

# Conectar ao banco de dados
def connect():
    con = sqlite3.connect('dados.db')
    return con

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)", 
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir novos usuários    
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)", 
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para exibir os livros
def get_books():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM livros")
    books = c.fetchall()
    conn.close()
    return books

# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", 
                 (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para exibir todos os livros emprestados             
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Função para exibir os usuários
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Função para deletar o conteúdo de uma tabela
def delete_all_from_table(table_name):
    conn = connect()
    conn.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()

# Função para atualizar a data de devolução
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

   
