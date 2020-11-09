import pyttsx3
import speech_recognition as sr

def talk(text):
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-50)
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(text)
	engine.runAndWait()


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: "+ str(e))
	return said.lower()

text = get_audio()
print(text)