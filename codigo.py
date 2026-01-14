#Bobliotecas = pacotes de código
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
time.sleep(2)

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

# 4° Passo: Cadastrar um produto
pyautogui.click(x=707, y=432) #Vai clicar no campo do código
pyautogui.write("MOLO000251")
pyautogui.press("tab") #Para passar para o próximo campo

#Para cadastrar a marca
pyautogui.write("Logitech")
pyautogui.press("tab")

#Para cadastrar o tipo
pyautogui.write("Mouse")
pyautogui.press("tab")

#Pra cadastrar a categoria
pyautogui.write("Logitech")
pyautogui.press("tab")

#para cadastrar o preço
pyautogui.write("Mouse")
pyautogui.press("tab")

#Para cadastrar o custo
pyautogui.write("Clonados")
pyautogui.press("tab")

#Para cadastrar 



















