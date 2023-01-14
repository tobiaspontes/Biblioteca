# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from datetime import date
from tkcalendar import DateEntry
import pandas as pd
import openpyxl
import os
import banco_dados
import incluir_livro, alterar_livro, excluir_livro, estatistica


### classe funcoes para abranger todas as funções que o app utilizará
class funcoes():

    ### função popular: preenche o treeview da janela principal
    def popular(self, treeview, label_total_principal):
        ### limpa os campos
        treeview.delete(*treeview.get_children())
        label_total_principal["text"] = ""
        ### monta sql
        vquery = "SELECT id, titulo, autor, editora, edicao FROM livros ORDER BY id"
        ### executa sql e retorna lista de tuplas; cada tupla é um registro do bd
        resultado = banco_dados.dql(vquery)
        ### preenche a treeview com as tuplas e define background de linhas pares com uma cor e linhas ímpares com outra cor
        for i, tupla in enumerate(resultado):
            if i % 2 == 0:
                treeview.insert("", END, values=tupla, tags=('par'))
            else:
                treeview.insert("", END, values=tupla, tags=('impar'))
        ### apresenta o total de registros carregados
        label_total_principal["text"] = f'Total: {len(resultado):,}'.replace(',','.')


    ### chama o módulo estatistica, passando como parâmetro a função (item do menu estatística)
    def estatistica(self, funcao):
        estatistica.tela_estatistica(janela_principal, estilo, funcao) 


    ### função que apresenta tela do item 'Ajuda' do menu
    def sobre(self, janela_principal):
        texto = "Este aplicativo foi desenvolvido em linguagem Python e acessa os dados armazenados em banco de dados SQLite.\n\nTrata-se do registro de livros que compõem a biblioteca de João Tobias, adquiridos ao longo do tempo.\n\nSão registrados dados referentes ao título da obra, autor, editora, edição, ano da edição, título original, ano da publicação,\n\n formato do livro (papel ou digital), situação (no acervo, lido, lido em parte, doado, emprestado), data do cadastro,\n\n data da leitura, se o livro está emprestado para alguém, data do empréstimo e pequena resenha dos livros lidos.\n\nO app foi criado em novembro de 2022."
        ### cria janela de nível acima da janela raiz para apresentar o texto do aplicativo
        janela_secundaria = Toplevel(janela_principal)
        ### configurações da janela
        janela_secundaria.title("Biblioteca")
        janela_secundaria.geometry("750x300")
        janela_secundaria.resizable(False, False)
        ### cursor pode ser: X_cursor, Arrow, plus, hand1, hand2
        janela_secundaria.configure(bg=roxo, cursor="hand2")
        ### relief: "raised", "sunken", "flat", "groove" e "ridge"
        labelframe_quadro = LabelFrame(janela_secundaria, text="Sobre", borderwidth=1, relief=RAISED, bg=cinza)
        labelframe_quadro.pack(padx=10, pady=10)

        ### imagem de ícone pode ser: question, information, error ou warning
        label_imagem_sobre=Label(labelframe_quadro, image="::tk::icons::information", bg=cinza)
        label_imagem_sobre.pack()

        label_texto_sobre=Label(labelframe_quadro, text=texto, font=fc, justify='left', bg=cinza, padx=10, pady=10)
        label_texto_sobre.pack()
    
        button_fechar_sobre=Button(janela_secundaria,text="Fechar", command=janela_secundaria.destroy, width=10, relief=RAISED, overrelief=RIDGE)
        button_fechar_sobre.pack()


    ### função para incluir novo registro
    def novo_livro(self):
        incluir_livro.tela_inclusao(self, janela_principal)

    
    ### função para alterar registro
    def alterar_livro(self):
        alterar_livro.tela_alteracao(self, janela_principal)
    

    ### função para excluir registro        
    def excluir_livro(self):
        excluir_livro.tela_exclusao(self, janela_principal)


    ### função para pesquisar livros por título, autor ou editora
    def pesquisar(self, treeview, vpesquisa, texto_pesquisa, label_total_principal):
        ### limpa a treeview
        treeview.delete(*treeview.get_children())
        ### verifica qual Radiobutton foi marcado e monta sql
        if vpesquisa.get() == "":
            messagebox.showerror(title="ERRO", message="Selecione um campo para pesquisa!")
        elif vpesquisa.get() == "titulo":
            vquery = "SELECT * FROM livros WHERE titulo LIKE '%"+texto_pesquisa.get()+"%' ORDER BY id"
        elif vpesquisa.get() == "autor":
            vquery = "SELECT * FROM livros WHERE autor LIKE '%"+texto_pesquisa.get()+"%' ORDER BY id"
        else:
            vquery = "SELECT * FROM livros WHERE editora LIKE '%"+texto_pesquisa.get()+"%' ORDER BY id"
        ### executa sql e retorna lista de tuplas; cada tupla é um registro do bd
        resultado = banco_dados.dql(vquery)
        ### preenche a treeview com as tuplas
        for i, tupla in enumerate(resultado):
            if i % 2 == 0:
                treeview.insert("", END, values=tupla, tags=('par'))
            else:
                treeview.insert("", END, values=tupla, tags=('impar'))
        ### apresenta o total de registros carregados e limpa o campo para pesquisa
        label_total_principal["text"] = f'Total: {len(resultado)}'
        texto_pesquisa.delete(0, END)


    ### apresenta a ficha completa do livro
    def consultar(self, evento):
        import ficha_livro
        self.item_selecionado = self.treeview.selection()
        self.valores = self.treeview.item(self.item_selecionado, "values")
        if self.valores:
            self.id_selecionado = self.valores[0]
            ficha_livro.registro_completo(self.id_selecionado)
    
    
    ### gera uma planilha com os registros do banco de dados
    def gravar_planilha(self):
        ### monta a query para selecionar todos os registros do banco de dados
        vquery = "SELECT * FROM livros ORDER BY id"
        ### executa sql e retorna lista de tuplas; cada tupla é um registro do bd
        resultado = banco_dados.dql(vquery)
        ### cria dataframe
        livros_cadastrados = pd.DataFrame(resultado, columns=['ID','TÍTULO','AUTOR','EDITORA','EDIÇÃO', 'ANO EDIÇÃO', 'SITUAÇÃO', 'DATA CADASTRO', 'COMENTÁRIO', 'FORMATO', 'DATA LEITURA', 'TÍTULO ORIGINAL', 'ANO PUBLICAÇÃO', 'EMPRÉSTIMO', 'DATA EMPRÉSTIMO'])
        ### salva um arquivo do Excel
        arquivo = asksaveasfilename(defaultextension='.xlsx', filetypes=[('Pasta de Trabalho do Excel', '*.xlsx'), ('Todos Arquivos', '*.*')]) 
        ### descarrega o DataFrame no Excel e cria aba 'livros'
        livros_cadastrados.to_excel(arquivo, sheet_name='livros') 
        ### gera mensagem de sucesso com o local do arquivo
        if arquivo:
            messagebox.showinfo(title="Biblioteca", message=f"Arquivo gravado com sucesso!\nLocal: {arquivo}")


### classe application que é a rotina principal do app; usa como parâmetro a classe funcoes
class application(funcoes):

    ### inicializa o app, criando tela, menu, widgets e populando a treeview
    def __init__(self, janela_principal, estilo):
        self.janela_principal = janela_principal
        self.tela(estilo)
        self.menu(janela_principal)
        self.frames_da_tela(janela_principal)
        self.widgets_frame()
        self.popular(self.treeview, self.label_total_principal)
        ### se algum item da treeview for selecionado, chama a função consultar
        self.treeview.bind("<<TreeviewSelect>>", self.consultar)
        janela_principal.mainloop()


    ### define a tela principal do app
    def tela(self, estilo):
        self.janela_principal.title('Biblioteca')
        self.janela_principal.configure(background=cinza, borderwidth=1, relief=SOLID)
        self.janela_principal.resizable(False, False)
        self.janela_principal.minsize(width=1100, height=510)
        self.estilo = estilo


    ### define o menu
    def menu(self, janela_principal):
        self.barra_menu = Menu(janela_principal)
        self.menu_livros = Menu(self.barra_menu, tearoff=0)
        self.menu_livros.add_command(label="Novo", command=self.novo_livro)
        self.menu_livros.add_command(label="Alterar", command=self.alterar_livro)
        self.menu_livros.add_command(label="Excluir", command=self.excluir_livro)
        self.menu_livros.add_command(label="Gravar Arquivo", command=self.gravar_planilha)
        self.menu_livros.add_separator()
        self.menu_livros.add_command(label="Sair", command=janela_principal.destroy)
        self.barra_menu.add_cascade(label="Livros", menu=self.menu_livros)
        self.menu_estatistica = Menu(self.barra_menu, tearoff=0)
        self.menu_estatistica.add_command(label="Livros Emprestados", command=lambda:self.estatistica("emprestados"))
        self.menu_estatistica.add_command(label="Livros Doados", command=lambda:self.estatistica("doados"))
        self.menu_estatistica.add_command(label="Livros Lidos", command=lambda:self.estatistica("lidos"))
        self.menu_estatistica.add_command(label="Livros Lidos em Parte", command=lambda:self.estatistica("lidos_parte"))
        self.menu_estatistica.add_command(label="Livros Digitais", command=lambda:self.estatistica("digital"))
        self.menu_estatistica.add_command(label="Quantitativo por Situação", command=lambda:self.estatistica("situacao"))
        self.menu_estatistica.add_command(label="Quantitativo por Formato", command=lambda:self.estatistica("formato"))       
        self.menu_estatistica.add_command(label="Quantitativo por Editora", command=lambda:self.estatistica("editora"))
        self.menu_estatistica.add_command(label="Quantitativo por Autor", command=lambda:self.estatistica("autor"))
        self.barra_menu.add_cascade(label="Estatísticas", menu=self.menu_estatistica)
        self.menu_sobre = Menu(self.barra_menu, tearoff=0)
        self.menu_sobre.add_command(label="Sobre", command=lambda:self.sobre(janela_principal))
        self.barra_menu.add_cascade(label="Ajuda", menu=self.menu_sobre)
        self.janela_principal.configure(menu=self.barra_menu)


    ### cria três frames: quadro para a treeview, quadro para pesquisa e quadro para a versão
    def frames_da_tela(self, janela_principal):
        self.labelframe_treeview = LabelFrame(janela_principal, text="LIVROS", bg=cinza)
        self.labelframe_treeview.pack(fill="both", expand="yes", padx=10, pady=10)
        self.labelframe_pesquisar = LabelFrame(janela_principal, text="Pesquisar Livros", bg=cinza)
        self.labelframe_pesquisar.pack(fill="both", expand="yes", padx=10, pady=10)
        self.frame_versao = Frame(janela_principal, bg=preto)
        self.frame_versao.pack(fill="both", expand="yes", padx=10, pady=10)


    ### criação do widgets: treeview, label, entry, button, radiobutton, scrollbar
    def widgets_frame(self):
        ### quadro treeview
        ### selectmode: extended(vários, default), browse(um) e none(nenhum)
        self.treeview = ttk.Treeview(self.labelframe_treeview, columns=('id','titulo','autor','editora','edicao'), show='headings', height=20, selectmode='browse')
        self.treeview.column('id', minwidth=0, width=40, anchor='center')
        self.treeview.column('titulo', minwidth=0, width=500)
        self.treeview.column('autor', minwidth=0, width=350)
        self.treeview.column('editora', minwidth=0, width=170)
        self.treeview.column('edicao', minwidth=0, width=70, anchor='center')
        self.treeview.heading('id', text="ID")
        self.treeview.heading('titulo', text="TÍTULO")
        self.treeview.heading('autor', text="AUTOR")
        self.treeview.heading('editora', text="EDITORA")
        self.treeview.heading('edicao', text="EDIÇÃO")
        ### configurando dois tipos de background para as linhas do treeview
        self.treeview.tag_configure('impar', background=azul2)
        self.treeview.tag_configure('par', background=azul3)
        ### temas (built-in): default, classic, alt, clam, vista, winnative, xpnative
        self.estilo.theme_use("clam") 
        self.estilo.configure('Treeview.Heading', foreground=preto, background=azul1, font=('Calibri', 12, 'bold'))
        self.treeview.grid(row=0, column=0)

        ### barra de rolagem vertical
        self.scrollbar_vertical = ttk.Scrollbar(self.labelframe_treeview, orient="vertical", command=self.treeview.yview)
        self.scrollbar_vertical.grid(row=0, column=1, sticky='nsew')
        self.treeview.configure(yscrollcommand=self.scrollbar_vertical.set)

        ### quadro pesquisa
        self.label_texto_pesquisa = Label(self.labelframe_pesquisar, text="Texto a pesquisar", bg=cinza)
        self.label_texto_pesquisa.pack(side="left")

        self.texto_pesquisa = Entry(self.labelframe_pesquisar, width=25)
        self.texto_pesquisa.pack(side="left", padx=10)

        self.vpesquisa = StringVar()

        self.radiobutton_titulo = Radiobutton(self.labelframe_pesquisar, text="Título", value="titulo", variable=self.vpesquisa, padx=5, pady=5, width=10, bg=cinza)
        self.radiobutton_titulo.pack(side="left", padx=10)

        self.radiobutton_autor = Radiobutton(self.labelframe_pesquisar, text="Autor", value="autor", variable=self.vpesquisa, padx=5, pady=5, width=10, bg=cinza)
        self.radiobutton_autor.pack(side="left", padx=10)

        self.radiobutton_editora = Radiobutton(self.labelframe_pesquisar, text="Editora", value="editora", variable=self.vpesquisa, padx=5, pady=5, width=10, bg=cinza)
        self.radiobutton_editora.pack(side="left", padx=10)

        self.button_pesquisar = Button(self.labelframe_pesquisar, text="Pesquisar", command=lambda: self.pesquisar(self.treeview, self.vpesquisa, self.texto_pesquisa, self.label_total_principal), width=12,relief=RAISED, overrelief=RIDGE)
        self.button_pesquisar.pack(side="left", padx=10)

        self.label_total_principal = Label(self.labelframe_pesquisar, text="", bg=cinza, font=fa, relief=SUNKEN, borderwidth=1, padx=10, pady=3)
        self.label_total_principal.pack(side="left", padx=30)

        self.button_sair = Button(self.labelframe_pesquisar, text="Sair", command=self.janela_principal.destroy, width=12, relief=RAISED, overrelief=RIDGE)
        self.button_sair.pack(side="right", padx=10)

        self.button_mostrar_todos = Button(self.labelframe_pesquisar, text="Mostrar Todos", command=lambda:self.popular(self.treeview, self.label_total_principal), width=12, relief=RAISED, overrelief=RIDGE)
        self.button_mostrar_todos.pack(side="right", padx=10)

        ### quadro versão
        self.label_criador = Label(self.frame_versao, text="Criado por João Tobias", bg=preto, fg=branco)
        self.label_criador.pack(side="left", padx=10)

        self.label_versao = Label(self.frame_versao, text="Versão: 1.0 - novembro de 2022", bg=preto, fg=branco)
        self.label_versao.pack(side="right", padx=10)


### definições de fontes e cores
fa = ("Arial", 10, "bold")
fc = ("Calibri", 10, "bold")
cinza = "#dde"
azul1 = "#add8e6"
azul2 = "#f0f8ff"
azul3 = "#d0e0e3"
preto = "#000"
branco = "#fff"
roxo = "#483d8b"


if __name__=='__main__':
    ### instancia a janela principal
    janela_principal =  Tk()
    ### instancia o estilo
    estilo = ttk.Style()
    ### guarda o caminho da pasta onde estão os arquivos do projeto
    caminho = os.path.dirname(__file__)
    ### guarda a data atual e o ano atual, que será utilizado no tkcalendar   
    data_atual = date.today()
    ano_atual = data_atual.year
    ### inicializa a aplicação
    application(janela_principal, estilo)