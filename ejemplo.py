import threading
import time

def hola_mundo(nombre):
	print("Hola mundo" + nombre)
	time.sleep(5)

if __name__ == '__main__':
	thread = threading.Thread(target = hola_mundo, args = ("Dany",))
	thread.start()
	thread.join()
	print("Hola mundo desde el hilo principal")


