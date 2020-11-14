import pyttsx3
import speech_recognition as sr
import sys
import webbrowser
import pyowm
import os
import time

os.environ['TZ'] = 'US/Eastern'
time.tzset()
time.ctime()
owm = pyowm.OWM("your OpenWeather key here")
observation = owm.weather_at_place("21911")
w = observation.get_weather()
temperature = w.get_temperature('fahrenheit')
text = ''
while 'shut down' not in text:
	print('\033[1;31;40m Jarvis ready, say a command \n')
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
	print('\033[1;32;40m %s \n' % text)
	
	if ('weather' in text):
		print('yes sir, it is currently ', int(temperature['temp']), 'degrees outside in Port Deposit, Maryland')
	#elif ()
	else:
		continue
sys.exit()
