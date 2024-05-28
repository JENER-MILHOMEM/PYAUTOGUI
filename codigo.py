import pyautogui as py
import time
import pandas as pd
py.PAUSE = 1

py.press("win")
py.write("chorme")
py.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
py.press("enter")
py.click(x=753, y=374)
time.sleep(1)
py.write("jener")
time.sleep(1)
py.press("tab")
time.sleep(0.5)
py.write("fran1414")
py.press("enter")
tabela = pd.read_csv("produtos.csv") 
print(tabela)
for linha in tabela.index:
    py.click(x=718, y=257)
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preço = tabela.loc[linha , "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    py.write(str(codigo))
    py.press("tab")
    py.write(str(marca))
    py.press("tab")
    py.write(str(tipo))
    py.press("tab")
    py.write(str(categoria))
    py.press("tab")
    py.write(str(preço))
    py.press("tab")
    py.write(str(custo))
    py.press("tab")
    if not pd.isna(obs):
        py.write(str(obs))
    py.click(x=885, y=910)
    py.scroll(5000)



