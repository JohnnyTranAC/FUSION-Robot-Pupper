from time import sleep
import os, sys

### Voice conversation starter input
def convoStarter(transcribe):
    if transcribe.find('want to play outside')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/playOut_1.wav')
        print("Pupper does not want to play outside")
        sleep(.5)
        
    elif transcribe.find('want to play inside')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/playIn_1.wav')
        print("Pupper wants to play inside\n")
        sleep(.5)
        
    elif transcribe.find('what time is it')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/time.wav')
        print("Pupper is telling the time\n")
        sleep(.5)
        
    else:
        print("ERROR: Pupper did not hear what you said\n")

### Voice conversation continuer input  
def convoContinue(transcribe):
    if transcribe.find('how come')!=-1 or transcribe.find('why not')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/playOut_2.wav')
        sleep(.5)
        
    elif transcribe.find('I don\'t think')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/playOut_3.wav')
        print("Pupper wants to be vaccinated\n")
        sleep(.5)
        
    elif transcribe.find('okay')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/pant_bark.wav')
        print("Pupper has compromised\n")
        sleep(.5)
        
    elif transcribe.find('what do you want to do')!=-1:
        os.system('omxplayer -o local /home/pi/speech_recognition/sounds/playIn_2.wav')
        print("Pupper wants to play\n")
        sleep(.5)
        
    else:
        print("ERROR: Pupper does not know how to respond\n")

