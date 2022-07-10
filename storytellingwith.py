import pyttsx3






Narrator = pyttsx3.init()
voices = Narrator.getProperty("voices")

Narrator.setProperty("voice", voices[0].id)
Narrator.say(" is tom cruise the best? ")


Narrator.say(" I CANT DENY THAT")


Narrator.runAndWait()


