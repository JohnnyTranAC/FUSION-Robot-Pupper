from time import sleep
#from adafruit_servokit import ServoKit
import os, sys

### Set channels to the number of servo channels on your kit.
### 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
#kit = ServoKit(channels=8)

### Initialize standing
# 1-4: Hips,   5-8: Knees,   9-12: Sideways Hips
#kit.servo[2].angle = 0      # front left
#kit.servo[6].angle = 0
#kit.servo[1].angle = 40     # front right
#kit.servo[5].angle = 40
#kit.servo[4].angle = 0      # back left
#kit.servo[8].angle = 0
#kit.servo[3].angle = 40     # back right
#kit.servo[7].angle = 40
#time.sleep(1)

### Command Types
# 1 - standing    2 - sitting
# 3 - walk        4 - run
# 5 - bark        6 - shake

### Voice command input
def action(commandType, position):
    if commandType == 1 and position == 2:
        ### Sitting to standing
        #kit.servo[4].angle = 0
        #kit.servo[8].angle = 0
        #kit.servo[3].angle = 40
        #kit.servo[7].angle = 40
        print("Pupper is now standing up\n")
        sleep(3)
        
    elif commandType == 2 and position == 1:
        ### Standing to sitting
        #kit.servo[4].angle = 40
        #kit.servo[8].angle = 40
        #kit.servo[3].angle = 0
        #kit.servo[7].angle = 0
        print("Pupper is now sitting down\n")
        sleep(3)
        
    elif commandType == 3 and commandType == 4:
        print("Pupper has not yet learned to walk or run\n")
        sleep(3)
        
    elif commandType == 5:
        ### Barking
        os.system('omxplayer -o local /home/pi/speech_recognition/bark.wav')
        print("Pupper is now barking\n")
        sleep(3)
        
    elif commandType == 6 and position == 1:
        ### Shake paw
        #kit.servo[1].angle = 120
        #kit.servo[5].angle = 0
        print("Pupper is now shaking its paw\n")
        sleep(3)
        
    else:
        print("ERROR: Pupper does not understand or cannot that action\n")