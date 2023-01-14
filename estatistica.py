from tkinter import *
from tkinter import ttk
import banco_dados

###### definições de fontes e cores
fa12 = ("Arial", 12, "bold")
fc = ("Calibri", 10, "bold")
cinza = "#dde"
azul1 = "#add8e6"
azul2 = "#f0f8ff"
azul3 = "#d0e0e3"
preto = "#000"
branco = "#fff"
roxo = "#483d8b"


### configurações da janela
def tela_estatistica(janela_principal, estilo, funcao):
    janela_principal.withdraw()
    janela_secundaria = Toplevel(janela_principal)
    janela_secundaria.title("Biblioteca")
    janela_secundaria.resizable(False, False)
    janela_secundaria.configure(bg=roxo, cursor="hand2")
    ### função a ser executada quando a janela é fechada
    def on_closing():
        janela_secundaria.destroy()
        janela_principal.deiconify()
    janela_secundaria.protocol("WM_DELETE_WINDOW", on_closing)

    frame_quadro = Frame(janela_secundaria, borderwidth=1, relief=RAISED, bg=cinza)
    frame_quadro.pack(padx=10, pady=10)

    match funcao:

        case "situacao":
            resultado = qtde_por_situacao()
            janela_secundaria.geometry("350x200")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('situacao','quantidade'), show='headings', height=5, selectmode='browse')
            treeview_estatistica.column('situacao', minwidth=0, width=180)
            treeview_estatistica.column('quantidade', minwidth=0, width=130, anchor='center')
            treeview_estatistica.heading('situacao', text="Situação")
            treeview_estatistica.heading('quantidade', text="Quantidade")
            texto_parcial = "Total Livros: "

        case "formato":
            resultado = qtde_por_formato()
            janela_secundaria.geometry("350x150")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('formato','quantidade'), show='headings', height=2, selectmode='browse')
            treeview_estatistica.column('formato', minwidth=0, width=180)
            treeview_estatistica.column('quantidade', minwidth=0, width=130, anchor='center')
            treeview_estatistica.heading('formato', text="Formato")
            treeview_estatistica.heading('quantidade', text="Quantidade")
            texto_parcial = "Total Livros: "

        case "editora":
            resultado = editoras()
            janela_secundaria.geometry("400x320")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('editora','quantidade'), show='headings', height=11, selectmode='browse')
            treeview_estatistica.column('editora', minwidth=0, width=200)
            treeview_estatistica.column('quantidade', minwidth=0, width=130, anchor='center')
            treeview_estatistica.heading('editora', text="Editora")
            treeview_estatistica.heading('quantidade', text="Quantidade")
            texto_parcial = "Total Livros: "

        case "autor":
            resultado = autores()
            janela_secundaria.geometry("400x320")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('autor','quantidade'), show='headings', height=11, selectmode='browse')
            treeview_estatistica.column('autor', minwidth=0, width=200)
            treeview_estatistica.column('quantidade', minwidth=0, width=130, anchor='center')
            treeview_estatistica.heading('autor', text="Autor")
            treeview_estatistica.heading('quantidade', text="Quantidade")
            texto_parcial = "Total Livros: "

        case "emprestados":
            resultado = livros_emprestados()
            janela_secundaria.geometry("1000x300")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('id','titulo', 'autor', 'emprestimo', 'dt_emprestimo'), show='headings', height=10, selectmode='browse')
            treeview_estatistica.column('id', minwidth=0, width=50, anchor='center')
            treeview_estatistica.column('titulo', minwidth=0, width=400)
            treeview_estatistica.column('autor', minwidth=0, width=200)
            treeview_estatistica.column('emprestimo', minwidth=0, width=150)
            treeview_estatistica.column('dt_emprestimo', minwidth=0, width=150, anchor='center')
            treeview_estatistica.heading('id', text="ID")
            treeview_estatistica.heading('titulo', text="Título")
            treeview_estatistica.heading('autor', text="Autor")
            treeview_estatistica.heading('emprestimo', text="Emprestimo")
            treeview_estatistica.heading('dt_emprestimo', text="Data do Empréstimo")
            texto_parcial = "Total Livros Emprestados: "

        case "lidos":
            resultado = lidos()
            janela_secundaria.geometry("800x500")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('id','titulo', 'autor', 'dt_leitura'), show='headings', height=20, selectmode='browse')
            treeview_estatistica.column('id', minwidth=0, width=50, anchor='center')
            treeview_estatistica.column('titulo', minwidth=0, width=300)
            treeview_estatistica.column('autor', minwidth=0, width=250)
            treeview_estatistica.column('dt_leitura', minwidth=0, width=150, anchor='center')
            treeview_estatistica.heading('id', text="ID")
            treeview_estatistica.heading('titulo', text="Título")
            treeview_estatistica.heading('autor', text="Autor")
            treeview_estatistica.heading('dt_leitura', text="Data Leitura")
            texto_parcial = "Total Livros Lidos: "

        case "lidos_parte":
            resultado = lidos_parte()
            janela_secundaria.geometry("700x500")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('id','titulo', 'autor'), show='headings', height=20, selectmode='browse')
            treeview_estatistica.column('id', minwidth=0, width=50, anchor='center')
            treeview_estatistica.column('titulo', minwidth=0, width=300)
            treeview_estatistica.column('autor', minwidth=0, width=300)
            treeview_estatistica.heading('id', text="ID")
            treeview_estatistica.heading('titulo', text="Título")
            treeview_estatistica.heading('autor', text="Autor")
            texto_parcial = "Total Livros Lidos em Parte: "

        case "doados":
            resultado = doados()
            janela_secundaria.geometry("900x500")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('id','titulo', 'autor', 'comentario'), show='headings', height=20, selectmode='browse')
            treeview_estatistica.column('id', minwidth=0, width=50, anchor='center')
            treeview_estatistica.column('titulo', minwidth=0, width=300)
            treeview_estatistica.column('autor', minwidth=0, width=200)
            treeview_estatistica.column('comentario', minwidth=0, width=300)
            treeview_estatistica.heading('id', text="ID")
            treeview_estatistica.heading('titulo', text="Título")
            treeview_estatistica.heading('autor', text="Autor")
            treeview_estatistica.heading('comentario', text="Comentário")
            texto_parcial = "Total Livros Doados: "

        case "digital":
            resultado = digital()
            janela_secundaria.geometry("700x500")
            treeview_estatistica = ttk.Treeview(frame_quadro, columns=('id','titulo', 'autor'), show='headings', height=20, selectmode='browse')
            treeview_estatistica.column('id', minwidth=0, width=50, anchor='center')
            treeview_estatistica.column('titulo', minwidth=0, width=300)
            treeview_estatistica.column('autor', minwidth=0, width=300)
            treeview_estatistica.heading('id', text="ID")
            treeview_estatistica.heading('titulo', text="Título")
            treeview_estatistica.heading('autor', text="Autor")
            texto_parcial = "Total Livros Digitais: "

    ### configura cores alternadas nas linhas do treeview
    treeview_estatistica.tag_configure('odd', background=azul2)
    treeview_estatistica.tag_configure('even', background=azul3)
    ### define tema do treeview
    estilo.theme_use("clam")
    estilo.configure('Treeview.Heading', foreground=preto, background=azul1, font=fc)
    treeview_estatistica.grid(row=0, column=0)

    ### barra de rolagem vertical, exceto para as funções de situação e formato
    if funcao != "situacao" and funcao != "formato":
        vertical_scrollbar_geral = ttk.Scrollbar(frame_quadro, orient="vertical", command=treeview_estatistica.yview)
        vertical_scrollbar_geral.grid(row=0, column=1, sticky='nsew')
        treeview_estatistica.configure(yscrollcommand=vertical_scrollbar_geral.set)

    ### código para definir o valor informado em total para cada função
    contador = 0
    for i, tupla in enumerate(resultado):
        if i % 2 == 0: treeview_estatistica.insert("", END, values=tupla, tags=('even',))
        else: treeview_estatistica.insert("", END, values=tupla, tags=('odd',))
        if funcao != "lidos" and funcao != "lidos_parte" and funcao != "digital" and funcao != "doados" and funcao != "emprestados":
            contador += tupla[1]
        else:
            contador += 1   
    lbl_resultado = Label(frame_quadro, text="", bg=preto, fg=branco, font=fa12, relief=SUNKEN, borderwidth=1, padx=10, pady=3)
    lbl_resultado.grid(row=1, column=0, sticky='nsew', pady=10, padx=10)
    lbl_resultado["text"] = f'{texto_parcial}{contador:,}'.replace(',','.')


    ### apresenta a ficha completa do livro
    def consultar(evento):
        import ficha_livro
        item_selecionado = treeview_estatistica.selection()
        valores = treeview_estatistica.item(item_selecionado, "values")
        if valores:
            id_selecionado = valores[0]
            ficha_livro.registro_completo(id_selecionado)
    
    ### ao selecionar um livro, abre sua ficha
    treeview_estatistica.bind("<<TreeviewSelect>>", consultar)


def qtde_por_situacao():
    vquery = "SELECT situacao, COUNT(*) FROM livros GROUP BY situacao"
    resultado = banco_dados.dql(vquery)
    return resultado


def qtde_por_formato():
    vquery = "SELECT formato, COUNT(*) FROM livros GROUP BY formato"
    resultado = banco_dados.dql(vquery)
    return resultado


def emprestados():
    vquery = "SELECT titulo, emprestimo, data_emprestimo FROM livros WHERE situacao = 'Emprestado'"
    resultado = banco_dados.dql(vquery)
    return resultado


def doados():
    vquery = "SELECT id, titulo, autor, comentario FROM livros WHERE situacao = 'Doado' ORDER BY titulo"
    resultado = banco_dados.dql(vquery)
    return resultado


def lidos():
    vquery = "SELECT id, titulo, autor, data_leitura FROM livros WHERE situacao = 'Lido' ORDER BY titulo"
    resultado = banco_dados.dql(vquery)
    return resultado


def lidos_parte():
    vquery = "SELECT id, titulo, autor FROM livros WHERE situacao = 'Lido em parte' ORDER BY titulo"
    resultado = banco_dados.dql(vquery)
    return resultado


def digital():
    vquery = "SELECT id, titulo, autor FROM livros WHERE formato = 'Digital' ORDER BY titulo"
    resultado = banco_dados.dql(vquery)
    return resultado


def editoras():
    vquery = "SELECT editora, COUNT(*) AS 'QTDE' FROM livros GROUP BY editora ORDER BY QTDE DESC"
    resultado = banco_dados.dql(vquery)
    return resultado


def autores():
    vquery = "SELECT autor, COUNT(*) AS 'QTDE' FROM livros GROUP BY autor ORDER BY QTDE DESC"
    resultado = banco_dados.dql(vquery)
    return resultado


def livros_emprestados():
    vquery = "SELECT id, titulo, autor, emprestimo, data_emprestimo FROM livros WHERE data_emprestimo NOT NULL AND data_emprestimo <> ''"
    resultado = banco_dados.dql(vquery)
    return resultado