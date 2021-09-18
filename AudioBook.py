#download your book as txt file and then save it as "MyBook" along with your code file.
import pyttsx3 as py
speaker=py.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
speaker.setProperty('rate',150)
a=open("MyBook.txt")
while(a.readline()!=None):
     text=a.readline()
     print(text)
     speaker.say(text)
     speaker.runAndWait()
