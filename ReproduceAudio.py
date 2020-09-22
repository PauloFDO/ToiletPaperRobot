import vlc
import os
import time

def play_audio(stringWithFile):
	print("audios to play: "+stringWithFile)
	audios = stringWithFile.split(',')
	
	for audio in range(len(audios)):
		currentDirectory = os.getcwd()
		fullpath = currentDirectory + "/Audios/"+audios[audio]+".mp3"
		player = vlc.MediaPlayer(fullpath)
		player.play()
		time.sleep(1)
		duration = player.get_length() / 1000
		time.sleep(duration)
