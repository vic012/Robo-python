'''Aqui importamos o pacote pyautogui
ela é uma biblioteca que fornece funções
que permitem automatizar rotinas no seu
navegador'''
import pyautogui as pyg
''' -- Aqui chamamos o pacote de "pyg", então
Sempre que você ver PYG nesse código, quer dizer que
estou usando o pyautogui (Mas vocês pode usar qualquer nome)'''
from time import sleep
'''Também precisamos de uma outra biblioteca
chamada "time". Dessa biblioteca pegaremos apenas uma função
que é o sleep que por sua vez, basicamente, nos ajuda a dizer
para o programa esperar um tempo determinado que queremos,
por isso o from time (do módulo time) import sleep (quero só o sleep)
Em outras palavras: (do módulo time quero só a função sleep)'''

''' ### IMPORTANTE ### 
Se ao executar (import pyautogui) no seu código aparecer
O erro:
      'Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
       ModuleNotFoundError: No module named 'pyautogui'"
Você precisa instalar pelo PIP INTALL o módulo pyautogui
Siga esse link para instalar o módulo:
( https://pypi.org/project/PyAutoGUI/ )
'''       

def PesquiNoGoogle():
	#Aqui usaremos um método do "PYG" chamado prompt, ele abre uma janela
	#na tela que permite o usuário interagir com o programa digitando algo
	#vamos pedir para ele digitar o que deseja pesquisar e em seguida
	#armazenaremos o texto do usuário em uma variável chamada de "texto"
	texto = pyg.prompt('Qual site você deseja pesquisar no Google!')
	#Queremos que o programa seja inteligente, ou seja
	#Se você for no google, não digitar nada, e teclar enter
	#O google vai retornar algum resultado? Claro que não.
	#Por isso colocaremos algumas condições para o nosso usuário

	#Teremos as seguintes condições:
	
	#Enquanto ele digitar "nada" no prompt e clicar em "OK", uma mensagem de erro deve aparecer
	while (texto == ''):
		pyg.alert('Por favor, insira algum texto!')
		texto = pyg.prompt('Qual site você deseja pesquisar no Google!')
	#Se ele apenas clicar em "Cancel" o sistema deve ser encerrado imediatamente
	if (texto == None):
		exit()

	#Somente se o usuário digitar algo e clicar em "ok" o sistema deve pesquisar
	#Se essa condição for abedecida, os demais passos serão executados

	#Agora vamos recorrer a algumas funcionalidades do PyAutoGui

	#Aqui vamos pedir ao programa para "Pressionar" a tecla do windows
	#Para isso usaremos o método pyautogui.press('nome da tecla'), nesse
	#caso "win".
	pyg.press('win')
	#Outro método que podemos usar do "PYG" é o write que nos permite digitar
	#algo, e junto a ele passaremos um argumento - que define um intervalo entre
	#cada letra do texto digitado. 
	pyg.write('google', interval = 0.5)
	#Depois que a digitação é finalizada a tecla "Enter" será pressionada.
	pyg.press('Enter')

	#Não sei se você percebeu, mas a partir desse momento (se você usar o
	#google em seu PC) será iniciado, geralmente precisamos esperar que o
	#navegador seja aberto, para isso vamos usar a função sleep com (5 segundos)
	#Assim as próximas linhas somente serão executados após esse tempo
	sleep(5)

	#Agora com o navegador aberto, o programa digitará o texto do usuário
	#na barra de navegação e em seguida filtrará os resultados da consulta
	pyg.write(texto, interval = 0.5)
	pyg.press('Enter')

PesquiNoGoogle()


# Link da documentação do PyAutoGui:
# https://pyautogui.readthedocs.io/en/latest/index.html
# Link da documentção do time:
# https://docs.python.org/3/library/time.html