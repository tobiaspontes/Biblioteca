from tkinter import *
import banco_dados


###### definições
fa = ("Arial", 10, "bold")
fc = ("Calibri", 10, "bold")
cinza = "#dde"
cinza_escuro = "#bcbcbc"
azul = "#007"
branco = "#fff"
preto = "#000"
violeta = "#b03060"
pastel = "#f0e68c"
roxo = "#cd96cd"


def registro_completo(id):
    ficha = Tk()
    ficha.title("Biblioteca")
    ficha.minsize(width=900, height=700)
    ficha.resizable(False, False)
    ficha.configure(borderwidth=1, relief=SOLID, bg=cinza)

    ###### layout da ficha do livro
    quadro = Frame(ficha, relief=RAISED, borderwidth=2, bg=cinza)
    quadro.pack(fill='both', expand='yes', padx=10, pady=5)

    lbl_id = Label(quadro, text="ID", width=15, anchor=E, bg=cinza, font=fc)
    lbl_id.place(x=10, y=10)
    txt_id = Text(quadro, relief=FLAT, width=5, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_id.place(x=125, y=10)

    lbl_titulo = Label(quadro, text="TÍTULO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_titulo.place(x=10, y=40)
    txt_titulo = Text(quadro, relief=FLAT, width=90, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_titulo.place(x=125, y=40)

    lbl_titulo_original = Label(quadro, text="TÍTULO ORIGINAL", width=15, anchor=E, bg=cinza, font=fc)
    lbl_titulo_original.place(x=10, y=70)
    txt_titulo_original = Text(quadro, relief=FLAT, width=90, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_titulo_original.place(x=125, y=70)

    lbl_autor = Label(quadro, text="AUTOR", width=15, anchor=E, bg=cinza, font=fc)
    lbl_autor.place(x=10, y=100)
    txt_autor = Text(quadro, relief=FLAT, width=90, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_autor.place(x=125, y=100)

    lbl_ano_publicacao = Label(quadro, text="ANO PUBLICAÇÃO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_ano_publicacao.place(x=10, y=130)
    txt_ano_publicacao = Text(quadro, relief=FLAT, width=5, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_ano_publicacao.place(x=125, y=130)

    lbl_data_cadastro = Label(quadro, text="DATA CADASTRO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_data_cadastro.place(x=10, y=160)
    txt_data_cadastro = Text(quadro, relief=FLAT, width=10, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_data_cadastro.place(x=125, y=160)

    lbl_editora = Label(quadro, text="EDITORA", width=15, anchor=E, bg=cinza, font=fc)
    lbl_editora.place(x=10, y=190)
    txt_editora = Text(quadro, relief=FLAT, width=50, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_editora.place(x=125, y=190)

    lbl_edicao = Label(quadro, text="EDIÇÃO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_edicao.place(x=10, y=220)
    txt_edicao = Text(quadro, relief=FLAT, width=5, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_edicao.place(x=125, y=220)

    lbl_ano_edicao = Label(quadro, text="ANO EDIÇÃO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_ano_edicao.place(x=10, y=250)
    txt_ano_edicao = Text(quadro, relief=FLAT, width=5, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_ano_edicao.place(x=125, y=250)

    lbl_formato = Label(quadro, text="FORMATO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_formato.place(x=10, y=280)
    txt_formato = Text(quadro, relief=FLAT, width=15, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_formato.place(x=125, y=280)

    lbl_situacao = Label(quadro, text="SITUAÇÃO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_situacao.place(x=10, y=310)
    txt_situacao = Text(quadro, relief=FLAT, width=15, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_situacao.place(x=125, y=310)

    lbl_data_leitura = Label(quadro, text="DATA LEITURA", width=15, anchor=E, bg=cinza, font=fc)
    lbl_data_leitura.place(x=10, y=340)
    txt_data_leitura = Text(quadro, relief=FLAT, width=10, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_data_leitura.place(x=125, y=340)

    lbl_comentario = Label(quadro, text="COMENTÁRIO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_comentario.place(x=10, y=370)
    txt_comentario = Text(quadro, relief=FLAT, width=100, height=13, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_comentario.place(x=125, y=370)

    lbl_emprestimo = Label(quadro, text="EMPRÉSTIMO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_emprestimo.place(x=10, y=595)
    txt_emprestimo = Text(quadro, relief=FLAT, width=50, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_emprestimo.place(x=125, y=595)

    lbl_data_emprestimo = Label(quadro, text="DATA EMPRÉSTIMO", width=15, anchor=E, bg=cinza, font=fc)
    lbl_data_emprestimo.place(x=10, y=625)
    txt_data_emprestimo = Text(quadro, relief=FLAT, width=10, height=1, font=fa, padx=5, fg=preto, bg=cinza_escuro)
    txt_data_emprestimo.place(x=125, y=625)

    ###### montagem da SQL para buscar os dados do id requerido
    query = "SELECT * FROM livros WHERE id = '"+id+"'"
    # SQL retorna uma lista de um elemento (uma tupla com os dados do registro selecionado)
    resultado = banco_dados.dql(query)

    for i in range(15):
        if resultado[0][i] != None:
            if i == 0: txt_id.insert(END, resultado[0][0])
            if i == 1: txt_titulo.insert(END, resultado[0][1])
            if i == 2: txt_autor.insert(END, resultado[0][2])
            if i == 3: txt_editora.insert(END, resultado[0][3])
            if i == 4: txt_edicao.insert(END, resultado[0][4])
            if i == 5: txt_ano_edicao.insert(END, resultado[0][5])
            if i == 6: txt_situacao.insert(END, resultado[0][6])
            if i == 7: txt_data_cadastro.insert(END, resultado[0][7])
            if i == 8: txt_comentario.insert(END, resultado[0][8])
            if i == 9: txt_formato.insert(END, resultado[0][9])
            if i == 10: txt_data_leitura.insert(END, resultado[0][10])
            if i == 11: txt_titulo_original.insert(END, resultado[0][11])
            if i == 12: txt_ano_publicacao.insert(END, resultado[0][12])
            if i == 13: txt_emprestimo.insert(END, resultado[0][13])
            if i == 14: txt_data_emprestimo.insert(END, resultado[0][14])