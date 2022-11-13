from __future__ import print_function
import pyaudio
import wave
import datetime
import speech_recognition as sr
import pyttsx3

from speachrecoginationFunctions import *

    
for i in dataToBespoken :
    speak(i)
    print(i)  # printing first value in the dataToBespoken
    recording() # recording the audio of user
    outputText = recognizing().lower() # converting the audio of user into text
    for  dataToBespoken in i: 
             
     if i == outputText : # checking if the user audio text matching with dataToBespoken
           print("correct pronunciation") 
           speak("correct pronunciation") 
           break
     else  :
            print("incorrect pronunciation please repeat again") 
            speak("incorrect pronunciation please repeat again")
            recording()
            outputText = recognizing().lower()