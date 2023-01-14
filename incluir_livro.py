from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from tkcalendar import DateEntry
import os
import banco_dados


### definição de cores
azul = "#009"
cinza = "#dde"


caminho = os.path.dirname(__file__)
data_atual = date.today()
ano_atual = data_atual.year


### configuração da janela
def tela_inclusao(self, janela_principal):
    janela_principal.withdraw()
    janela_secundaria = Toplevel(janela_principal)
    janela_secundaria.title("Biblioteca")
    janela_secundaria.minsize(width=680, height=300)
    janela_secundaria.resizable(False, False)
    janela_secundaria.configure(background=cinza, borderwidth=1, relief=GROOVE)
    ### função a ser executada quando a janela é fechada
    def on_closing():
        janela_secundaria.destroy()
        janela_principal.deiconify()
        self.popular(self.treeview, self.label_total_principal)
    janela_secundaria.protocol("WM_DELETE_WINDOW", on_closing)

    Label(janela_secundaria, text="Data Cadastro", bg=cinza, fg=azul, anchor=W).place(x=10, y=10, width=100, height=20)
    dateentry_data_cadastro = DateEntry(janela_secundaria, year=ano_atual, locale='pt_br')
    dateentry_data_cadastro.configure(justify='center')
    dateentry_data_cadastro.place(x=10, y=30, width=100, height=20)

    self.photoimage_imagem = PhotoImage(file=caminho + "\\livro.png", width=120)
    self.label_imagem = Label(janela_secundaria, image=self.photoimage_imagem, bg=cinza, fg=azul)
    self.label_imagem.place(x=10, y=60)

    Label(janela_secundaria, text="Título", bg=cinza, fg=azul, anchor=W).place(x=150, y=10, width=100, height=20)
    entry_titulo = Entry(janela_secundaria)
    entry_titulo.place(x=150, y=30, width=500, height=20)

    Label(janela_secundaria, text="Título Original", bg=cinza, fg=azul, anchor=W).place(x=150, y=60, width=100, height=20)
    entry_titulo_original = Entry(janela_secundaria)
    entry_titulo_original.place(x=150, y=80, width=500, height=20)

    Label(janela_secundaria, text="Autor", bg=cinza, fg=azul, anchor=W).place(x=150, y=110, width=100, height=20)
    entry_autor = Entry(janela_secundaria)
    entry_autor.place(x=150, y=130, width=500, height=20)

    Label(janela_secundaria, text="Editora", bg=cinza, fg=azul, anchor=W).place(x=10, y=160, width=100, height=20)
    entry_editora = Entry(janela_secundaria)
    entry_editora.place(x=10, y=180, width=300, height=20)

    Label(janela_secundaria, text="Edição", bg=cinza, fg=azul, anchor=W).place(x=350, y=160, width=100, height=20)
    entry_edicao = Entry(janela_secundaria, justify='center')
    entry_edicao.place(x=350, y=180, width=50, height=20)

    Label(janela_secundaria, text="Ano Edição", bg=cinza, fg=azul, anchor=W).place(x=440, y=160, width=100, height=20)
    entry_ano_edicao = Entry(janela_secundaria, justify='center')
    entry_ano_edicao.place(x=440, y=180, width=80, height=20)

    Label(janela_secundaria, text="Ano Publicação", bg=cinza, fg=azul, anchor=W).place(x=560, y=160, width=100, height=20)
    entry_ano_publicacao = Entry(janela_secundaria, justify='center')
    entry_ano_publicacao.place(x=560, y=180, width=80, height=20)

    Label(janela_secundaria, text="Formato", bg=cinza, fg=azul, anchor=W).place(x=10, y=210, width=100, height=20)
    combobox_formato = ttk.Combobox(janela_secundaria, values=("Papel","Digital"))
    ### seta o item que aparecerá no combobox como default
    combobox_formato.set("Papel")
    combobox_formato.place(x=10, y=230, width=100, height=20)

    Label(janela_secundaria, text="Situação", bg=cinza, fg=azul, anchor=W).place(x=150, y=210, width=100, height=20)
    combobox_situacao = ttk.Combobox(janela_secundaria, values=("No acervo","Lido", "Lido em parte", "Emprestado", "Doado"))
    ### seta o item que aparecerá no combobox como default
    combobox_situacao.set("No acervo")
    combobox_situacao.place(x=150, y=230, width=100, height=20)

    Button(janela_secundaria, text="Gravar", command=lambda:gravar_dados(), relief=RAISED, overrelief=RIDGE).place(x=550, y=230, width=100, height=30)


    ### montagem do sql para inserção de dados no bd
    def gravar_dados():
        if entry_titulo.get() != "" and entry_autor.get() != "":
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

            vquery = "INSERT INTO livros (titulo, autor, editora, edicao, ano_edicao, situacao, data_cadastro, formato, titulo_original, ano_publicacao) values ('"+vtitulo+"','"+vautor+"','"+veditora+"','"+vedicao+"','"+vanoedicao+"','"+vsituacao+"','"+vdtcadastro+"','"+vformato+"','"+vtitulo_original+"','"+vanopublicacao+"')"

            bd = banco_dados.dml(vquery)

            if bd == "Sucesso":
                messagebox.showinfo(title="Biblioteca", message="Livro cadastrado com sucesso!")
            else:
                messagebox.showerror(title="Biblioteca", message=bd)
            ### limpa os campos
            entry_autor.delete(0, END)
            entry_ano_edicao.delete(0, END)
            entry_ano_publicacao.delete(0, END)
            entry_editora.delete(0, END)
            entry_edicao.delete(0, END)
            entry_titulo.delete(0, END)
            entry_titulo_original.delete(0, END)
            entry_titulo.focus_set()
            return
        else:
            messagebox.showerror(title="Biblioteca", message="Necessário informar no mínimo título e autor.")