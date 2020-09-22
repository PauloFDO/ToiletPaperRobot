import speech_recognition as sr  

def voice_recognition():
	said = ''
	while(True):
		try:
			# get audio from the microphone                                                                       
			r = sr.Recognizer()                                                                              
			with sr.Microphone() as source:                                                                       
				print("Speak:")                                                                                   
				audio = r.listen(source, phrase_time_limit=1.5)  
			
			said = r.recognize_google(audio)
			print('You said: '+ said)
			break
		except Exception:
			pass
	
	return said
