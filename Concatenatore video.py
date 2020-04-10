from tkinter import Tk
from tkinter.filedialog import askopenfilename
from moviepy.editor import *


def schermo_iniziale():
	print(' ____________________________________')
	print('|        CONCATENATORE VIDEO         |')
	print('|____________________________________|')
	print('|1. Aggiungi nuovo video             |')
	print('|2. Concatena                        |')	
	print('|0. Esci                             |')
	print('|____________________________________|')


def converti(files):
	videos = []
	for file in files:
		video = VideoFileClip(file) 
		videos.append(video)


	finalrender = concatenate_videoclips(videos)
	nome_file = input("Scegli nome file da salvare: ")
	finalrender.write_videofile(nome_file + '.mp4', codec = 'libx264')

def main():
	files = []
	while(True):
		schermo_iniziale()
		try:
			scelta = int(input())

			if(scelta == 0):
				break
			if(scelta == 1):
				Tk().withdraw() 
				filename = askopenfilename() 
				print(filename)  
				files.append(filename)
			if(scelta == 2 and len(files) >= 2):
				converti(files)
				break
			if(scelta == 2 and len(files) < 2):
				print(' ____________________________________')
				print('|   INSERIRE PRIMA ALMENO DUE VIDEO  |')
				print('|____________________________________|')						
		except:
			print(' ____________________________________')
			print('|***ERRORE INSERIRE VALORE VALIDO*** |')
			print('|____________________________________|')

main()


