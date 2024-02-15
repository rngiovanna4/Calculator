import tkinter as tk
from math import sqrt
from re import findall

calculadora = "" #variável de expressão
#Criando o Layout
root = tk.Tk()
root.geometry("300x275")
root.configure(background="light blue")
root.title('Calculadora')
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#Criando as funções

def adicionar(symbol):
    '''Essa função adiciona os digitos a tela da calculadora'''
    global calculadora
    calculadora += str(symbol) #concatenação os dígitos
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculadora)
    return

def porcentagem():
    global calculadora
    print(calculadora)
    simbolo = findall("[+-/*]",calculadora)[0]
    list = calculadora.split(simbolo)
    inteiro = float(list[0])
    parte = float(list[1])
    porcentagem = (inteiro/100)*parte
    resultado = str(inteiro)+simbolo+str(porcentagem)
    resultado = eval(resultado)
    deletar()
    adicionar(resultado)



def avaliar_calculo():
    """Essa função impede calculos problemáticos como divisão por zero"""
    global calculadora
    try: 
        calculadora = str(eval(calculadora))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculadora)
    except:
        '''limpa o terminal e apresentar a mensagem de erro'''
        deletar()
        text_result.insert(1.0, "Error")

def deletar():
    '''Essa função limpa a tela da calculadora'''
    global calculadora
    calculadora = ""
    text_result.delete(1.0, "end")

def raiz(calculadora):
    calculadora = sqrt(float(calculadora))
    deletar()
    adicionar(calculadora)
    

'''Cada expressão a seguir representa uma tecla da calculadora. Seu nome, seu simbolo, sua posição e sua configuração.'''

bnt_limpa = tk.Button(root, text=str("C"), fg = "orange", command=lambda:  deletar(), width=5, font=("Arial", 14))
bnt_limpa.grid(row=1, column=1) 

bnt_porcentagem = tk.Button(root, text=str("%"), command=porcentagem, width=5, font=("Arial", 14))
bnt_porcentagem.grid(row=1, column=2)

bnt_raiz = tk.Button(root, text=str("√"), command=lambda: raiz(calculadora), width=5, font=("Arial", 14))
bnt_raiz.grid(row=1, column=3)


bnt_delete = tk.Button(root, text=str("⌫"), fg="red",command=lambda:  deletar(), width=5, font=("Arial", 14))
bnt_delete.grid(row=1, column=4)

bnt_7 = tk.Button(root, text=str(7), command=lambda: adicionar(7), width=5, font=("Arial", 14))
bnt_7.grid(row=2, column=1)

bnt_8 = tk.Button(root, text=str(8), command=lambda: adicionar(8), width=5, font=("Arial", 14))
bnt_8.grid(row=2, column=2)

bnt_9 = tk.Button(root, text=str(9), command=lambda: adicionar(9), width=5, font=("Arial", 14))
bnt_9.grid(row=2, column=3)

bntmais = tk.Button(root, text='+', bg = "DarkTurquoise", command=lambda: adicionar('+'), width=5, font=("Arial", 14))
bntmais.grid(row=2, column=4)

bnt_4 = tk.Button(root, text=str(4), command=lambda: adicionar(4), width=5, font=("Arial", 14))
bnt_4.grid(row=3, column=1)

bnt_5 = tk.Button(root, text=str(5), command=lambda: adicionar(5), width=5, font=("Arial", 14))
bnt_5.grid(row=3, column=2)

bnt_6 = tk.Button(root, text=str(6), command=lambda: adicionar(6), width=5, font=("Arial", 14))
bnt_6.grid(row=3, column=3)

bnt_menos = tk.Button(root, text='-', bg = "DarkTurquoise", command=lambda: adicionar('-'), width=5, font=("Arial", 14))
bnt_menos.grid(row=3, column=4)

bnt_1 = tk.Button(root, text=str(1), command=lambda: adicionar(1), width=5, font=("Arial", 14))
bnt_1.grid(row=4, column=1)

bnt_2 = tk.Button(root, text=str(2), command=lambda: adicionar(2), width=5, font=("Arial", 14))
bnt_2.grid(row=4, column=2)

bnt_3 = tk.Button(root, text=str(3), command=lambda: adicionar(3), width=5, font=("Arial", 14))
bnt_3.grid(row=4, column=3)

bnt_vezes = tk.Button(root, text=str("x"), bg = "DarkTurquoise", command=lambda: adicionar("*"), width=5, font=("Arial", 14))
bnt_vezes.grid(row=4, column=4)

bnt_0= tk.Button(root, text=str(0), command=lambda: adicionar(0), width=5, font=("Arial", 14))
bnt_0.grid(row=5, column=1)

bnt_ponto= tk.Button(root, text=str(","), command=lambda: adicionar("."), width=5, font=("Arial", 14))
bnt_ponto.grid(row=5, column=2)

bnt_igual= tk.Button(root, text= ("="), bg="mediumspringgreen", command=avaliar_calculo, width=5, font=("Arial", 14))
bnt_igual.grid(row=5, column=3)

bnt_divisão= tk.Button(root, text=str("÷"), bg = "DarkTurquoise", command=lambda: adicionar("/"), width=5, font=("Arial", 14))
bnt_divisão.grid(row=5, column=4)


root.mainloop()