from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import os
import banco_dados


### definição de fontes e cores
fa12 = ("Arial", 12, "bold")
fa = ("Arial", 10)
vermelho = "#f72a19"
azul = "#009"
cinza = "#dde"


caminho = os.path.dirname(__file__)
data_atual = date.today()
ano_atual = data_atual.year


### configuração da janela
def tela_alteracao(self, janela_principal):
    janela_principal.withdraw()
    janela_secundaria = Toplevel(janela_principal)
    janela_secundaria.title("Biblioteca")
    janela_secundaria.minsize(width=680, height=600)
    janela_secundaria.resizable(False, False)
    janela_secundaria.configure(background=cinza, borderwidth=1, relief=GROOVE)
    ### função a ser executada quando a janela é fechada
    def on_closing():
        janela_secundaria.destroy()
        janela_principal.deiconify()
        self.popular(self.treeview, self.label_total_principal)
    janela_secundaria.protocol("WM_DELETE_WINDOW", on_closing)

    frame_pesquisa = Frame(janela_secundaria, bg=cinza, borderwidth=1, relief=SUNKEN)
    frame_pesquisa.place(relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.08)
    frame_dados = Frame(janela_secundaria, bg=cinza, borderwidth=1, relief=SUNKEN)
    frame_dados.place(relx= 0.01, rely= 0.1, relwidth=0.98, relheight= 0.8)

    Label(frame_pesquisa, text="Informe o ID", bg=cinza, fg=azul, anchor=W).place(x=10, y=10, width=100, height=20)
    entry_id_pesquisa = Entry(frame_pesquisa, justify='center')
    entry_id_pesquisa.place(x=110, y=10, width=50, height=20)
    entry_id_pesquisa.focus_set()
    
    Button(frame_pesquisa, text="Pesquisar", command=lambda:pesquisar_id(self), relief=RAISED, overrelief=RIDGE).place(x=200, y=10, width=100, height=30)
    Label(frame_pesquisa, text="ALTERAÇÃO DE LIVRO", bg=cinza, fg=vermelho, font=fa12).place(x=380, y=10, width=200, height=20)  

    Label(frame_dados, text="Data Cadastro", bg=cinza, fg=azul, anchor=W).place(x=10, y=10, width=100, height=20)
    dateentry_data_cadastro = DateEntry(frame_dados, year=ano_atual, locale='pt_br')
    dateentry_data_cadastro.configure(justify='center')
    dateentry_data_cadastro.delete(0, "end")
    dateentry_data_cadastro.place(x=10, y=30, width=100, height=20)

    self.photoimage_imagem = PhotoImage(file=caminho + "\\livro.png", width=120)
    self.label_imagem = Label(frame_dados, image=self.photoimage_imagem, bg=cinza, fg=azul)
    self.label_imagem.place(x=10, y=60)

    Label(frame_dados, text="Título", bg=cinza, fg=azul, anchor=W).place(x=150, y=10, width=100, height=20)
    entry_titulo = Entry(frame_dados)
    entry_titulo.place(x=150, y=30, width=500, height=20)

    Label(frame_dados, text="Título Original", bg=cinza, fg=azul, anchor=W).place(x=150, y=60, width=100, height=20)
    entry_titulo_original = Entry(frame_dados)
    entry_titulo_original.place(x=150, y=80, width=500, height=20)

    Label(frame_dados, text="Autor", bg=cinza, fg=azul, anchor=W).place(x=150, y=110, width=100, height=20)
    entry_autor = Entry(frame_dados)
    entry_autor.place(x=150, y=130, width=500, height=20)

    Label(frame_dados, text="Editora", bg=cinza, fg=azul, anchor=W).place(x=10, y=160, width=100, height=20)
    entry_editora = Entry(frame_dados)
    entry_editora.place(x=10, y=180, width=300, height=20)

    Label(frame_dados, text="Edição", bg=cinza, fg=azul, anchor=W).place(x=350, y=160, width=100, height=20)
    entry_edicao = Entry(frame_dados, justify='center')
    entry_edicao.place(x=350, y=180, width=50, height=20)

    Label(frame_dados, text="Ano Edição", bg=cinza, fg=azul, anchor=W).place(x=440, y=160, width=100, height=20)
    entry_ano_edicao = Entry(frame_dados, justify='center')
    entry_ano_edicao.place(x=440, y=180, width=80, height=20)

    Label(frame_dados, text="Ano Publicação", bg=cinza, fg=azul, anchor=W).place(x=560, y=160, width=100, height=20)
    entry_ano_publicacao = Entry(frame_dados, justify='center')
    entry_ano_publicacao.place(x=560, y=180, width=80, height=20)

    Label(frame_dados, text="Formato", bg=cinza, fg=azul, anchor=W).place(x=10, y=210, width=100, height=20)
    combobox_formato = ttk.Combobox(frame_dados, values=("Papel","Digital"))
    combobox_formato.place(x=10, y=230, width=100, height=20)

    Label(frame_dados, text="Situação", bg=cinza, fg=azul, anchor=W).place(x=180, y=210, width=100, height=20)
    combobox_situacao = ttk.Combobox(frame_dados, values=("No acervo","Lido", "Lido em parte", "Emprestado", "Doado"))
    combobox_situacao.place(x=180, y=230, width=100, height=20)

    Label(frame_dados, text="Data Leitura", bg=cinza, fg=azul, anchor=W).place(x=350, y=210, width=100, height=20)
    dateentry_data_leitura = DateEntry(frame_dados, year=ano_atual, locale='pt_br')
    dateentry_data_leitura.configure(justify='center')
    dateentry_data_leitura.delete(0, "end")
    dateentry_data_leitura.place(x=350, y=230, width=100, height=20)

    Label(frame_dados, text="Data Empréstimo", bg=cinza, fg=azul, anchor=W).place(x=540, y=210, width=100, height=20)
    dateentry_data_emprestimo = DateEntry(frame_dados, year=ano_atual, locale='pt_br')
    dateentry_data_emprestimo.configure(justify='center')
    dateentry_data_emprestimo.delete(0, "end")
    dateentry_data_emprestimo.place(x=540, y=230, width=100, height=20)

    Label(frame_dados, text="Empréstimo", bg=cinza, fg=azul, anchor=W).place(x=10, y=260, width=100, height=20)
    entry_emprestimo = Entry(frame_dados)
    entry_emprestimo.place(x=10, y=280, width=600, height=20)

    Label(frame_dados, text="Comentário", bg=cinza, fg=azul, anchor=W).place(x=10, y=310, width=100, height=20)
    text_comentario = Text(frame_dados, font=fa)
    text_comentario.place(x=10, y=330, width=640, height=140)

    Button(janela_secundaria, text="Limpar", command=lambda:limpar(self), relief=RAISED, overrelief=RIDGE).place(x=180, y=550, width=100, height=30)

    Button(janela_secundaria, text="Alterar", command=lambda:alterar_dados(self), relief=RAISED, overrelief=RIDGE).place(x=420, y=550, width=100, height=30)

    ### coloca o foco no campo de id para pesquisa
    entry_id_pesquisa.focus_force()


    ### monta a sql para alterar registro no bd
    def alterar_dados(self):
        if entry_id_pesquisa.get() != "" and entry_titulo.get() != "" and entry_autor.get() != "":
            vid = entry_id_pesquisa.get()
            vdtcadastro = dateentry_data_cadastro.get()
            vtitulo = entry_titulo.get()
            vtitulo_original = entry_titulo_original.get()
            vautor = entry_autor.get()
            veditora = entry_editora.get()
            vedicao = entry_edicao.get()
            vanoedicao = entry_ano_edicao.get()
            vanopublicacao = entry_ano_publicacao.get()
            vformato = combobox_formato.get()
            vsituacao = combobox_situacao.get()
            vdtleitura = dateentry_data_leitura.get()
            vdtemprestimo = dateentry_data_emprestimo.get()
            vemprestimo = entry_emprestimo.get()
            vcomentario = text_comentario.get('1.0', END)

            vquery = "UPDATE livros SET titulo='"+vtitulo+"', autor='"+vautor+"', editora='"+veditora+"', titulo_original='"+vtitulo_original+"', edicao='"+vedicao+"', ano_edicao='"+vanoedicao+"', ano_publicacao='"+vanopublicacao+"', situacao='"+vsituacao+"', formato='"+vformato+"', data_leitura='"+vdtleitura+"', data_emprestimo='"+vdtemprestimo+"', emprestimo='"+vemprestimo+"', comentario='"+vcomentario+"', data_cadastro='"+vdtcadastro+"' WHERE id='"+vid+"'"

            banco_dados.dml(vquery)

            messagebox.showinfo(title="Biblioteca", message="Livro atualizado com sucesso!")
            limpar(self)
            return
        else:
            messagebox.showerror(title="Biblioteca", message="Necessário informar, no mínimo, ID,  título e autor.")


    ### pesquisa registro no bd pelo id
    def pesquisar_id(self):
        id_registro = entry_id_pesquisa.get()
        if id_registro == "":
            messagebox.showwarning(title="Biblioteca", message="Informe o ID do livro!")
            return

        ### montagem da SQL para buscar os dados do id requerido
        vquery = "SELECT * FROM livros WHERE id = '"+id_registro+"'"

        ### SQL retorna uma lista de um elemento (uma tupla com os dados do registro selecionado)
        resultado = banco_dados.dql(vquery)
        if len(resultado) == 0:
            messagebox.showinfo(title="Biblioteca", message="Registro não localizado!")
            return
        if resultado[0][1] != None: entry_titulo.insert(END, resultado[0][1])
        if resultado[0][2] != None: entry_autor.insert(END, resultado[0][2])
        if resultado[0][3] != None: entry_editora.insert(END, resultado[0][3])
        if resultado[0][4] != None: entry_edicao.insert(END, resultado[0][4])
        if resultado[0][5] != None: entry_ano_edicao.insert(END, resultado[0][5])
        if resultado[0][6] != None: combobox_situacao.insert(END, resultado[0][6])
        if resultado[0][7] != None: dateentry_data_cadastro.insert(END, resultado[0][7])
        if resultado[0][8] != None: text_comentario.insert(END, resultado[0][8])
        if resultado[0][9] != None: combobox_formato.insert(END, resultado[0][9])
        if resultado[0][10] != None: dateentry_data_leitura.insert(END, resultado[0][10])
        if resultado[0][11] != None: entry_titulo_original.insert(END, resultado[0][11])
        if resultado[0][12] != None: entry_ano_publicacao.insert(END, resultado[0][12])
        if resultado[0][13] != None: entry_emprestimo.insert(END, resultado[0][13])
        if resultado[0][14] != None: dateentry_data_emprestimo.insert(END, resultado[0][14])


    ### limpa os campos
    def limpar(self):
        entry_titulo.delete(0, END)
        entry_autor.delete(0, END)
        entry_editora.delete(0, END)
        entry_edicao.delete(0, END)
        entry_ano_edicao.delete(0, END)
        entry_ano_publicacao.delete(0, END)
        combobox_situacao.delete(0, END)
        combobox_formato.delete(0, END)
        dateentry_data_cadastro.delete(0, END)
        dateentry_data_leitura.delete(0, END)
        dateentry_data_emprestimo.delete(0, END)
        text_comentario.delete('1.0', END)
        entry_emprestimo.delete(0, END)               
        entry_titulo_original.delete(0, END)
        entry_id_pesquisa.delete(0, END)
        entry_id_pesquisa.focus_set()