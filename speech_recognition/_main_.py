import speech_recognition as sr
from actions import action

r = sr.Recognizer()
m = sr.Microphone()
position = 1

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            transcribe = r.recognize_google(audio)
            commandList = ['Stand', 'Sit', 'Walk', 'Run', 'Bark', 'Shake', 'stand', 'sit', 'walk', 'run', 'bark', 'shake', 'goodnight']

            if any(x in transcribe for x in commandList):
                if transcribe.find('Stand')!=-1 or transcribe.find('stand')!=-1:
                    print("Pupper will stand up")
                    action(1, position)
                    position = 1
                elif transcribe.find('Sit')!=-1 or transcribe.find('sit')!=-1:
                    print("Pupper will sit down")
                    action(2, position)
                    position = 2
                elif transcribe.find('Walk')!=-1 or transcribe.find('walk')!=-1:
                    print("Pupper will walk")
                    action(3, position)
                    position = 1
                elif transcribe.find('Run')!=-1 or transcribe.find('run')!=-1:
                    print("Pupper will run")
                    action(4, position)
                    position = 1
                elif transcribe.find('Bark')!=-1 or transcribe.find('bark')!=-1:
                    print("Pupper will bark")
                    action(5, position)
                elif transcribe.find('Shake')!=-1 or transcribe.find('shake')!=-1:
                    print("Pupper will shake")
                    action(6, position)
                    position = 1
                elif transcribe.find('goodnight')!=-1:
                    print("Pupper is going to sleep. Goodnight")
                    break
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said '{}'".format(transcribe).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said '{}'".format(transcribe))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass