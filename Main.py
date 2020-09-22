import ReproduceAudio
import SpeechRecognision
import Motor
import threading

speech_recognision = SpeechRecognision
reproduce_audio = ReproduceAudio

def audio_answer_to_command(givenCommand):

	if 'clean' in givenCommand:
		return 'clean'

		
	return 'none'
	
def motor_answer_to_command(givenCommand):
	if 'clean' in givenCommand:
		return 'forward'

	
	return 'none'
	
def take_command_actions(audio_answer, motor_answer):
	
	if 'none' not in audio_answer:
		reproduce_audio.play_audio(motor_answer)
		        
	
	if 'none' not in motor_answer:
		Motor.Commands(motor_answer,2)
	
def wait_for_command():
	while(True):
		command = speech_recognision.voice_recognition()
		audio_answer = audio_answer_to_command(command)
		motor_answer = motor_answer_to_command(command)
	
		take_command_actions(audio_answer,motor_answer)

wait_for_command()
