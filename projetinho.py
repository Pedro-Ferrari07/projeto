import unicodedata
import tkinter as tk


#tirar os acentos (ajuda da ia)
def normalizar(txt):
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    ).lower()
#separar a entrada
def analisar(event=None):
    texto_bruto = entrada.get("1.0", tk.END)
    texto = normalizar(texto_bruto)
    palavras = texto.split()
    
    pontos = 0
    multiplicador = 1
    negacao = False

    for p in palavras:
#verifica intensidade
        if p in ["muito", "demais", "baita", "tri", "extremamente"]:
            multiplicador = 2
            continue
        
        if p in ["pouco", "quase", "mais ou menos"]:
            multiplicador = 0.5
            continue

#verifica negação
        if p in ["nao", "nunca", "jamais", "nem"]:
            negacao = True
            continue

        valor_base = 0

#pesos das palavras de sentimento
        if p in ["perfeito", "perfeita", "excelente", "incrivel", "maravilhoso", "maravilhosa", "fantastico", "fantastica", "otimo", "otima"]:
            valor_base = 2

        elif p in ["feliz", "bem", "bom", "boa", "legal", "faceiro", "faceira", "top", "massa", "dahora", "show", "curti", "gostei", "amei", "sucesso", "brabo", "braba", "zica"]:
            valor_base = 1

        elif p in ["deboa", "tranquilo", "tranquila"]:
            valor_base = 0.5

        elif p in ["horrivel", "pessimo", "pessima", "terrivel", "horrendo", "horrenda"]:
            valor_base = -2

        elif p in ["triste", "ruim", "mal", "atucanado", "atucanada", "estressado", "estressada", "puto", "puta", "irritado", "irritada", "deprimido", "deprimida", "ansioso", "ansiosa", "nervoso", "nervosa", "frustrado", "frustrada", "desanimado", "desanimada", "lixo", "merda"]:
            valor_base = -1

        elif p in ["cansado", "cansada", "chateado", "chateada", "acabado", "acabada"]:
            valor_base = -0.5

#calculo (ajuda da ia)
        if valor_base != 0:
            resultado_palavra = valor_base * multiplicador
            
            if negacao:
                resultado_palavra = -resultado_palavra
                
            pontos += resultado_palavra
            
#resetar depois de usar
            multiplicador = 1
            negacao = False

#atualizacão da interface baseada na pontuação total (ajuda da ia)
    if pontos >= 2:
        tela.config(bg="#004400", text="Perfeito!")
    elif pontos > 0:
        tela.config(bg="#008000", text="Positivo")
    elif pontos == 0:
        tela.config(bg="#444444", text="Neutro")
    elif pontos > -2:
        tela.config(bg="#b22222", text="Negativo")
    else:
        tela.config(bg="#7a0000", text="Péssimo")

#estrutura da janela
janela = tk.Tk()
janela.title("Analisador de Humor")
janela.geometry("300x550")
janela.configure(bg="#222222")

fundo = tk.Frame(janela, bg="#111111")
fundo.place(relx=0.5, rely=0.5, anchor="center", width=260, height=500)

tk.Label(fundo, text="COMO FOI SEU DIA?", fg="white", bg="#111111", font=("Arial", 10, "bold")).pack(pady=15)

entrada = tk.Text(fundo, height=5, width=22, font=("Arial", 10))
entrada.pack(pady=10)

botao = tk.Button(fundo, text="Analisar", command=analisar, width=15, bg="#444444", fg="white")
botao.pack(pady=10)

tela = tk.Label(fundo, bg="#333333", width=20, height=8, fg="white", font=("Arial", 12, "bold"))
tela.pack(pady=20)

janela.bind("<Return>", analisar)
janela.mainloop()



#RESUMO CÓDIGO 8/10
#FEITO POR IA: tirar os acentos da entrada; calculo dos pontos; algumas partes da iterface; e algumas outras funções que aprendi durante o projeto

#POSITIVO:lógica funcional; custumização com girias; interface facil de mexer; o fato de tirar os acentos pois se não ia quebrar 
#NEGATIVO:por ser na base da matematica, acaba sendo falho em alguns sentidos; se o usuário escrever palavras muitos longas não vai ser certeiro, dicionário limitado perto da lingua portuguesa completa