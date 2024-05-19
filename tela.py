from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import  messagebox, ttk 
from datetime import datetime

# importando as funçoes da view
from view import *

hoje = datetime.today()

data = hoje.date()

# cores--------------------------------

cor0 = "#2e2d2b"
cor1 = "#feffff"
cor2 = "#4fa882"
cor3 = "#38576b"
cor4 = "#403d3d"
cor5 = "#e06636"
cor6 = "#E9A178"
cor7 = "#3fbfb9"
cor8 = "#263238"
cor9 = "#e9edf5"
cor10 = "#6e8faf"
cor11 = "#f2f4f2"


janela = Tk()
janela.title("")
janela.geometry("770x330")
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


# Frames -----------------------------

frameCima = Frame(janela, width=770, height=50, bg=cor6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=cor4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=cor1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# logo --------------------------------

app_img = Image.open('img/book-shelf.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=cor6, fg=cor1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=cor6, fg=cor1)
app_.place(x=50, y=7)

app_linha= Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
app_linha.place(x=0, y=47)

# Novo usuario
def novo_usuario():

    global save_img
    
    def add():
        first_name = e_p_nome.get()
        last_name = e_sobrenome.get()
        address = e_endereco.get()
        email = e_email.get()
        phone = e_telefone.get()
        
        lista = [first_name, last_name, address, email, phone]
        
        # verificando a integridade da lista
        for i in lista:
            if i == '':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        # inserindo os dandos no banco de dados 
        insert_user(first_name, last_name, address, email, phone)
        
        messagebox.showinfo('Sucesso!', 'Usario inserido com sucesso')
        
        e_p_nome.delete(0,END)
        e_sobrenome.delete(0,END)
        e_endereco.delete(0,END)
        e_email.delete(0,END)
        e_telefone.delete(0,END)
        
    app_ = Label(frameDireita, text='inserir um novo usuario', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha= Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
 
    l_p_nome = Label(frameDireita, text='Primeiro nome*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)  
    e_p_nome = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_p_nome.grid(row=2, column=2, padx=5, pady=5, sticky=NSEW)   

    l_sobrenome = Label(frameDireita, text='Sobrenome*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)  
    e_sobrenome = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_sobrenome.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW) 

    l_endereco = Label(frameDireita, text='Endereço do usuario*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)  
    e_endereco = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_endereco.grid(row=4, column=2, padx=5, pady=5, sticky=NSEW)     

    l_email = Label(frameDireita, text='E-mail do usuario*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)  
    e_email = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_email.grid(row=5, column=2, padx=5, pady=5, sticky=NSEW) 

    l_telefone = Label(frameDireita, text='Telefone do usuario*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_telefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)  
    e_telefone = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_telefone.grid(row=6, column=2, padx=5, pady=5, sticky=NSEW)
    
    # Botão salvar
    save_img = Image.open('img/save.png')
    save_img = save_img.resize((20,20))
    save_img = ImageTk.PhotoImage(save_img)
    save_button = Button(frameDireita, command=add, image=save_img, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    save_button.grid(row=7, column=2, pady=5, sticky=NSEW)
    
    #-------------------------------------------------------------------------------------------------------------------------
    
    # Ver usuarios

# Ver usuários
def ver_usuarios():

    app_ = Label(frameDireita,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=cor3, fg=cor1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_users()

    # Criando uma treeview com barras de rolagem duplas
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para o cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)   

# Novo livro
def novo_livro():
    global save_img
    
    def add():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        ano_publicacao = e_ano_publicacao.get()
        isbn = e_isbn.get()
        
        lista = [titulo, autor, editora, ano_publicacao, isbn]
        
        # verificando a integridade da lista
        for i in lista:
            if i == '':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        # inserindo os dandos no banco de dados 
        insert_book(titulo, autor, editora, ano_publicacao, isbn)
        
        messagebox.showinfo('Sucesso!', 'Livro inserido com sucesso')
        
        e_titulo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano_publicacao.delete(0,END)
        e_isbn .delete(0,END)    

    app_ = Label(frameDireita, text='inserir um novo livro', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha= Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
 
    l_titulo = Label(frameDireita, text='Titulo*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)  
    e_titulo = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_titulo.grid(row=2, column=2, padx=5, pady=5, sticky=NSEW)   

    l_autor = Label(frameDireita, text='Autor*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)  
    e_autor = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_autor.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW) 

    l_editora = Label(frameDireita, text='Editora*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)  
    e_editora = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_editora.grid(row=4, column=2, padx=5, pady=5, sticky=NSEW)     

    l_ano_publicacao = Label(frameDireita, text='Ano de publicacao*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_ano_publicacao.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)  
    e_ano_publicacao = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_ano_publicacao.grid(row=5, column=2, padx=5, pady=5, sticky=NSEW) 

    l_isbn  = Label(frameDireita, text='ISBN*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_isbn .grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)  
    e_isbn  = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_isbn .grid(row=6, column=2, padx=5, pady=5, sticky=NSEW)
    
    # Botão salvar
    save_img = Image.open('img/save.png')
    save_img = save_img.resize((20,20))
    save_img = ImageTk.PhotoImage(save_img)
    save_button = Button(frameDireita, command=add, image=save_img, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    save_button.grid(row=7, column=2, pady=5, sticky=NSEW)

# Ver livros
def ver_livros():
    app_ = Label(frameDireita,text="Todos os livros do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=cor3, fg=cor1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_books()

    # Criando uma treeview com barras de rolagem duplas
    list_header = ['ID','Titulo','Autor','Editora','Ano','ISBN']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para o cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

# Realizar Emprestimo
def realizar_emprestimo():
    global save_img
    
    def add():
        id_user = e_id_usuario.get()
        id_book = e_id_livro.get()

        lista = [id_user, id_book]
        
        # verificando a integridade da lista
        for i in lista:
            if i == '':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        # inserindo os dandos no banco de dados 
        insert_loan(id_user, id_book, data, None)
        
        messagebox.showinfo('Sucesso!', 'O livro foi emprestado com sucesso')
        
        e_id_usuario.delete(0,END)
        e_id_livro.delete(0,END)

        
    app_ = Label(frameDireita, text='Realizar um emprestimo', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha= Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
 
    l_id_usuario = Label(frameDireita, text='ID Usuario*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)  
    e_id_usuario = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_id_usuario.grid(row=2, column=2, padx=5, pady=5, sticky=NSEW)   

    l_id_livro = Label(frameDireita, text='ID livro*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)  
    e_id_livro = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_id_livro.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW) 

    # Botão salvar
    save_img = Image.open('img/save.png')
    save_img = save_img.resize((20,20))
    save_img = ImageTk.PhotoImage(save_img)
    save_button = Button(frameDireita, command=add, image=save_img, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    save_button.grid(row=7, column=2, pady=5, sticky=NSEW)

# Ver os livros emprestados
def ver_livros_emprestados():
    app_ = Label(frameDireita,text="Todos os emprestados no momento",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=cor3, fg=cor1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []

    book_on_loan = get_books_on_loan()

    for book in book_on_loan:
            dado = [f"{book[0]}", f"{book[1]}", f"{book[2]} {book[3]}" , f"{book[4]}", f"{book[5]}"]

            dados.append(dado)        

    # Criando uma treeview com barras de rolagem duplas
    list_header = ['ID','Titulo','Usuario','D.emprestimo','D.devolução']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,175,120,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # Ajustando a largura da coluna para o cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)        

# Devolução do livro
def devolução_do_livro():
    global save_img
    
    def add():
        id_emprestimo = int(e_id_emprestimo.get())
        N_data = e_N_data.get()

        lista = [id_emprestimo, N_data]
        
        # verificando a integridade da lista
        for i in lista:
            if i == '':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        # inserindo os dandos no banco de dados 
        update_loan_return_date(id_emprestimo, N_data)
        
        messagebox.showinfo('Sucesso!', 'A data foi atualizada com sucesso')
        
        e_id_emprestimo.delete(0,END)
        e_N_data.delete(0,END)

        
    app_ = Label(frameDireita, text='Atualizar a data de devolução', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha= Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_id_emprestimo = Label(frameDireita, text='ID Emprestimo*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)  
    e_id_emprestimo = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_id_emprestimo.grid(row=2, column=2, padx=5, pady=5, sticky=NSEW)   

    l_N_data = Label(frameDireita, text='Nova data de devolução*', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_N_data.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)  
    e_N_data = Entry(frameDireita, width=25, justify="left", relief='solid')
    e_N_data.grid(row=3, column=2, padx=5, pady=5, sticky=NSEW) 

    # Botão salvar
    save_img = Image.open('img/save.png')
    save_img = save_img.resize((20,20))
    save_img = ImageTk.PhotoImage(save_img)
    save_button = Button(frameDireita, command=add, image=save_img, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=cor1, fg=cor4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    save_button.grid(row=7, column=2, pady=5, sticky=NSEW)

# Função para controlar o menu
def control(i):
    # Novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função novo usuario
        novo_usuario()
        
    # Ver usuarios
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função para exibir usuários
        ver_usuarios()

    # Ver usuarios
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função novo livro
        novo_livro() 

    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função novo livro
        ver_livros()

    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função novo usuario
        realizar_emprestimo()

    if i == 'ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função novo livro
        ver_livros_emprestados() 

    if i == 'Devolução emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # chamando a função devolução do livro
        devolução_do_livro() 

# Menu --------------------------------

# Novo usuario
img_user = Image.open('img/add.png')
img_user = img_user.resize((18,18))
img_user = ImageTk.PhotoImage(img_user)
b_user = Button(frameEsquerda, command=lambda:control('novo_usuario'), image=img_user, compound=LEFT, anchor=NW, text=' Novo Usuario', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro
img_book = Image.open('img/add.png')
img_book = img_book.resize((20,20))
img_book = ImageTk.PhotoImage(img_book)
b_book = Button(frameEsquerda, command=lambda:control('novo_livro'), image=img_book, compound=LEFT, anchor=NW, text=' Novo Livro', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_book.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver livros
img_books = Image.open('img/books.png')
img_books = img_books.resize((20,20))
img_books = ImageTk.PhotoImage(img_books)
b_books = Button(frameEsquerda, command=lambda:control('ver_livros'), image=img_books, compound=LEFT, anchor=NW, text=' Exibir todos os Livros', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_books.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver ususarios
img_show_user = Image.open('img/user.png')
img_show_user = img_show_user.resize((20,20))
img_show_user = ImageTk.PhotoImage(img_show_user)
b_show_user = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_show_user, compound=LEFT, anchor=NW, text=' Exibir todos os usuarios', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_show_user.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar emprestimo
img_loan = Image.open('img/shopping-cart.png')
img_loan = img_loan.resize((20,20))
img_loan = ImageTk.PhotoImage(img_loan)
b_loan = Button(frameEsquerda, command=lambda:control('realizar_emprestimo'), image=img_loan, compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_loan.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de um empestimo
img_back_loan = Image.open('img/update.png')
img_back_loan = img_back_loan.resize((20,20))
img_back_loan = ImageTk.PhotoImage(img_back_loan)
b_back_loan = Button(frameEsquerda, command=lambda:control('Devolução emprestimo'), image=img_back_loan, compound=LEFT, anchor=NW, text=' Devolução de um empréstimo', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_back_loan.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros em emprestimo
img_now_loan = Image.open('img/magnifying-glass.png')
img_now_loan = img_now_loan.resize((20,20))
img_now_loan = ImageTk.PhotoImage(img_now_loan)
b__now_loan = Button(frameEsquerda, command=lambda:control('ver_livros_emprestados'), image=img_now_loan, compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=cor4, fg=cor1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b__now_loan.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

janela.mainloop()
