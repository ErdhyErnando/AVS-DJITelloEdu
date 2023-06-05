import pygame
from djitellopy import tello
from time import sleep

# Initialize Pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

# Check if a specific key is pressed
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

# Initialize Pygame
init()

# Create an instance of the Tello class
me = tello.Tello()
me.connect()
print(me.get_battery())

# Function to get keyboard input and control the drone
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    # Move left and right
    if getKey("LEFT"):
        lr = -speed
    elif getKey("RIGHT"):
        lr = speed

    # Move forward and backward
    if getKey("UP"):
        fb = speed
    elif getKey("DOWN"):
        fb = -speed

    # Move up and down
    if getKey("w"):
        ud = speed
    elif getKey("s"):
        ud = -speed

    # Yaw movement
    if getKey("a"):
        yv = speed
    elif getKey("d"):
        yv = -speed

    # For landing
    if getKey("q"):
        me.land()

    # For takeoff
    if getKey("e"):
        me.takeoff()

    return [lr, fb, ud, yv]

# Main loop for controlling the drone
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
