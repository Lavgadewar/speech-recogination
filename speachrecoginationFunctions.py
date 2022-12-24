from __future__ import print_function
import pyaudio
import wave
import datetime
import speech_recognition as sr
import pyttsx3

dataToBespoken = ["india is an independent country","delhi is the capital of india"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 for male voice,1 for female voice

#  function to convert text to speach
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

# creates unique name for wave file
now=datetime.datetime.now()
new_now=now.strftime("%y%m%d%H%M%S")
userAudioFileName = "voice"+ str(new_now) +".wav" # name of the wave file

# paramaters for voice recording

FRAMES_PER_BUFFER = 3200
FORMATE = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# for recording the voice of the user in wave file

def recording():
    
 p = pyaudio.PyAudio()

 stream=p.open(
    format=FORMATE,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
 )
 print("Listening...")
 seconds=5
 frames =[]
 for i in range(0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    data=stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
 stream.stop_stream()
 stream.close()
 p.terminate()
 
 # saveing the frames object in wave file

 obj = wave.open( userAudioFileName,"wb")
 obj.setnchannels(CHANNELS)
 obj.setsampwidth(p.get_sample_size(FORMATE) )
 obj.setframerate(RATE)
 obj.writeframes(b"".join(frames))
 obj.close()

# for converting wave audio into text

def recognizing():
    sound= str(userAudioFileName) # wave file name as inpur for recognizer

    r = sr.Recognizer()
    with sr.AudioFile(sound) as source:
      
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("recognizing...")
        outputText = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {outputText}\n")

    except Exception as e:
        print(e)

        print("say that again plese....")
        return "None"
    return outputText 
