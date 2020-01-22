#FRONTEND
#listen for input
import csv
import speech_recognition as sr

r = sr.Recognizer()   #Speech is recognition
with sr.Microphone() as source:
    print("Which file you want to search")
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source)
    print("listening.......")
try:
    message = r.recognize_google(audio)
    print("You search for: "+message)
    with open('C:\\Automation\\file\\test.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for field in row:
                if field == message:
                    print ("Opening the file %s"%row[1])
                    os.startfile(row[1])
except:
     pass;
