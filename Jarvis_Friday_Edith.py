import pyttsx3


Friday = pyttsx3.init()

voices = Friday.getProperty("voices")

Friday.setProperty("voice", voices[1].id)
speech = input ("Say Something:")
Friday.say(speech)
Friday.say("My Name is Friday")

Jarvis = pyttsx3.init()
voices = Jarvis.getProperty("voices")

Jarvis.setProperty("voice", voices[0].id)
Jarvis.say("Hello Friday!")


Jarvis.say("My name is Jarvis.")

Jarvis.say("Together, we are the core Artificial Intelligence network created by Mr Tony Stark")



Edith = pyttsx3.init()
voices = Edith.getProperty("voices")
Edith.setProperty("voice", voices[2].id)

Edith.say("Hello, I am Edith.")







Friday.runAndWait()
Jarvis.runAndWait()
Edith.runAndWait()


