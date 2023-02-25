from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import asyncio 
import pyautogui as pyg
import clipboard



"""
	Esse problema consiste em ir até o site do mairo vergara e capturar o conteúdo
	de um dos phrasal verbs.

	passo 1: navegar até o site e encontrar a página referente aos phrasal verbs

	passo 2: clicar no local do phrasal verb

	passo 3: selecionar o conteúdo e salvar em um .txt
"""

#primeira etapa

def navigate(url: str):
	driver = webdriver.Firefox()
	return driver.get(url)

def click(x_coord,y_coord):
	return pyg.click(x_coord,y_coord)

def click_element():
	return 1

def clickAndNext():
	for n in range(20):
		pyg.click(1357,709)
	pyg.click(463,172)

def click_scroll():
	# lugar do primeiro set: x=1358, y=284
	for n in range(2):
		pyg.click(1358,284,interval=0.25)
	sleep(2)
	# lugar do segundo set: x=1356, y=389
	for n in range(2):
		pyg.click(1358,389,interval=0.25)
	sleep(2)
	# lugar do terceiro set: x=1356, y=501
	for n in range(3):
		pyg.click(1358,501,interval=0.25)
	sleep(2)	
	# lugar do quarto set: x=1357, y=604
	for n in range(4):
		pyg.click(1358,604,interval=0.25)
	sleep(2)

	#volta para a home da scrollbar
	for n in range(5):
		pyg.click(1354,102,interval=0.25)
	sleep(10)
	return click_scroll()

def click_post():
	#primeiro post: x=333, y=201
	pyg.click(1358,284,interval=0.25)
	sleep(0.25)
	pyg.click(333,201)
	select_text()
	#segundo post: x=682, y=200
	#terceiro post: x=327, y=486
	#quarto post: x=673, y=491

	#penúltimo post: x=333, y=201
	#último post: x=682, y=200
	return 1 

def drag_bar():

	pyg.mouseDown(button="left")

def select_text():
	#início do conteúdo do post: x=179, y=343
	#aisle de término de conteúdo: x=832, y=526
	sleep(10)
	pyg.click(179,343, interval=0.25)
	pyg.keyDown('shift')
	for n in range(4):
		pyg.click(1358,501,interval=0.25)
	sleep(10)
	pyg.click(832,526)
	pyg.keyUp('shift')
	#pyg.hotkey("ctrl","a")
	sleep(0.25)
	pyg.hotkey("ctrl","c")

	content = clipboard.paste()
	
	with open('C:/Users/Miguel/Desktop/run_in.txt','wt', encoding='utf-8') as file:
		file.write(content)
	
	pyg.alert("ARQUIVO CRIADO E SALVO !")

def get_position():
	#botão inferior da scrowbar: x=1357, y=716 ou um pouco fora x=1356, y=709
	#botão de next 1: x=364, y=172
	#botão de next 2: x=397, y=173
	#botão de next 3: x=429, y=172
	#botão de next 4: x=463, y=172
	#  .
	#  .
	#  .
	#botão de next 61: x=429, y=172
	
	#botão de next 62: x=397, y=171
	#botão de next 63: desnecessário

	print(pyg.position())


if __name__ == '__main__':
	#navigate('https://www.mairovergara.com/category/phrasal-verbs')
	#get_position()
	#click(463,172)

	"""for n in range(30):
		clickAndNext()
		sleep(10)
	pyg.alert("FINALIZADO !")
	"""

	#click_scroll()
	click_post()

	