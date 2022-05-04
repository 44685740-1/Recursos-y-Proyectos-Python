#pip install curses-2048 este es el pip que si pude instalar en la biblioteca de pypip
#despues de instalar lo de la linea de arriba si me dejo usar pip install windows-curses y lo instalo
#este pregrama se ejecuta en el cmc de windows
#para encortrar la ruta de nuestro archivo entramos a el icono de las carpetas y en la parte de la ruta escribimos cmd y eso hace que se nos copie la ruta al cmd y solo tenemos que agregar el nombre del archivo
import curses
from curses import wrapper

def start_screen(stdscr):
    #el indice significa la ubicacion de filas y columnas respectivamente
    #se puede sobrescribir sobre otro texto si tengo dos o mas ubicaciones o lineas de texto
    #si quiero poner color al texto pongo: curses.color_pair(indice deseado)
    stdscr.clear()
    stdscr.addstr("welcome to the speed typing test ")
    #la \n sirve para que se muestre el texto en la linea por debajo alt + 92 opara hcer la barra invertida
    stdscr.addstr("\npress any keey to start ")
    stdscr.refresh()
    stdscr.getkey


def wpm_test(stdscr):
    target_text = "hola esto es solo un poco de texto por parte de ahuitz para que lo copies y ver tu rapidez"
    current_text = []
    
    

    while True:
        time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)