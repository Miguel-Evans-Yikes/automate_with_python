import pyautogui as pg
from time import sleep

string = str
def get_position():
	return tuple(pg.position())


#posição do like: (924, 605)

def like():
	return pg.click(924, 605)

#usado para pressionar duas ou mais teclas do teclado
def select_content(first_key: string, second_key:string):
	return pg.hotkeys(first_key,second_key)

def move_cursor_to(x_coord, y_coord):
	return pg.moveTo(x_coord, y_coord)

def click(x, y):
	return pg.click(x,y)

def write_stuff(text):
	return pg.typewrite(text)


#usado para pressionar apenas uma tecla do teclado
def press(key: string):
	return pg.press(key)

def select_text(xi,yi,xf,yf):
	pg.doubleClick(xi,yi)
	pg.moveTo(xf,yf)

def check_page():
	for n in range(80):
		click(1357, 720)

#manter tecla pressionada e soltá-la.
def hold_key(kdown:string=None,kup:string=None):
	if kdown != None:
		pg.keyDown(kdown)
	elif kup != None:
		pg.keyDown(kdown)
	else:
		return None









if __name__=='__main__':
	#print(get_position())
	"""for n in range(1000):
		sleep(5)
		like()
		
	"""
	click(1356, 257) #clica na barra lateral
	"""
	sleep(5)
	click(327, 190)	 #clica no primeiro post
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(20)
	click(1356, 257)	#coloca na primeira posição da barra lateral

	click(676, 200) #clica no segundo post 
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(20)
	click(1356, 257)	#coloca na primeira posição da barra lateral
	sleep(5)

	click(321, 490)  #clica no terceiro post 
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(20)
	click(1356, 257)	#coloca na primeira posição da barra lateral
	sleep(5)

	click(672, 492)  #clica no quarto post
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(20)
	click(1356, 257)	#coloca na primeira posição da barra lateral
	sleep(5)"""


	click(1361, 429)	#coloca na segunda posição da barra lateral
	sleep(5)
	click(322, 208)  #clica no quinto post
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(5)
	click(669, 193) #clica no sexto post
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(5)
	click(319, 498)  #clica no sétimo post
	sleep(30)
	click(24, 65) #clica no botão voltar
	sleep(5)
	click(656, 495)  #clica no oitavo post
	pg.alert('finalizado!')

	
	


	"""click(1354, 377) #clica na barra lateral
				
				sleep(5)
				click(1354, 483) #clica na barra lateral
				
				sleep(5)
				click(1357, 600) #clica na barra lateral
	"""

	#posição da primeira parte da barra lateral (1356, 257)

	#posição do primeiro post (327, 190)

	#posição do segundo post (676, 200)

	#posição do terceiro post (321, 490)

	#posição do quarto post (672, 492)
	
	#posição da segunda parte da barra lateral (1354, 377)
	
	#posição do quinto post (322, 208)  

	#posição do sexto post (669, 193)
	
	#posição do sétima post (319, 498)
	
	#posição do oitavo post (656, 495)
	
	#posição da terceira parte da barra lateral (1354, 483)
	
	#posição do nono post (328, 218)
	
	#posição do décimo post (666, 218)
	
	#posição do eleven post (324, 523)
	
	#posição do twelve post (658, 527)

	#posição da terceira parte da barra lateral (1357, 600)

	#posição do thirteen post (328, 179)

	#posição do fourteen post (659, 180)

	





