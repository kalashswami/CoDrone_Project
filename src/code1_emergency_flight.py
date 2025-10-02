import CoDrone
from CoDrone import Color
from CoDrone.protocol import Direction
import threading
import keyboard
import time

drone = CoDrone.CoDrone()
drone.pair(drone.Nearest, 'COM3')  # Change to your COM port

emergency = False

def monitor():
    global emergency
    print("Press 'l' to land immediately.")
    while True:
        if keyboard.is_pressed('l'):
            emergency = True
            break

threading.Thread(target=monitor, daemon=True).start()

def do(action, *args):
    global emergency
    if not emergency:
        action(*args)
        time.sleep(0.1)
    else:
        print("Emergency landing activated.")
        drone.land()
        drone.close()
        raise SystemExit

do(drone.takeoff)
do(drone.eye_color, Color.Yellow, 100)
drone.hover(2)
do(drone.move, 1, 0, 0, 0, 10)
do(drone.go, Direction.FORWARD, 4, 25)
drone.hover(1.5)
drone.rotate180()
do(drone.eye_color, Color.Navy, 100)
do(drone.move, 1, 0, 0, 0, 10)
do(drone.go, Direction.FORWARD, 4, 25)
drone.hover(1)
drone.rotate180()
do(drone.land)
drone.close()
