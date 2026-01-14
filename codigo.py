#Bibliotecas = pacotes de código
#pip install pyautogui 
# Passo a passo
# 1° Passo: Entrar no sistema da empresa
# 2° Passo: Fazer login
# 3° Passo: Abrir a base de dados
# 4° Passo cadastrar um produto
# 5° Passo: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time

#pyautogui.click -> Clica
#pyautogui.write -> Escreve um texto
#pyautogui.press -> Aperta uma tecla
#pyautogui.hotkey -> Aperta um atalho (hotkey)
pyautogui.PAUSE = 2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1° passo: Entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

#Digitar o site da empresa e deu Enter para entar no mesmo
pyautogui.write(link)
pyautogui.press("enter")

#Fazer uma pausa maior para o site carregar, levando em consideração a internet
#Importe a biblioteca time
time.sleep(3)

# 2° Fazer login 
pyautogui.click(x=549, y=606)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #Usado para passar para o próximo campo
pyautogui.write("sua senha muito muito muito dificilima")
pyautogui.press("tab") #Usado para passar para o próximo botão
pyautogui.press("enter")

#Fazer uma pausa maior para o site carregar, levando em consideração a internet 
time.sleep(3)

# 3° Passo: Abrir a base de dados
#Instalar a biblioteca Pandas openpyxl (pip install pandas openpyxl)
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # 4° Passo: Cadastrar um produto
    pyautogui.click(x=707, y=432) #Vai clicar no campo do código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") #Para passar para o próximo campo

    #Para cadastrar a marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #Para cadastrar o tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #Pra cadastrar a categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #para cadastrar o preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #Para cadastrar o custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #Para escrever uma observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") #Usado para ir para o botão de enviar

    pyautogui.press("enter") # Clica no botão enviar

    #Depois do produto ser cadastrado tenho que voltar para o início da tela
    pyautogui.scroll(5000)

# 5° Passo: Repetir o passo 4 até acabar a lista de produto


#NaN = Not a Number = Valor Vazio


