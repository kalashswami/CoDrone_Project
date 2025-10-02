import CoDrone
import time

drone = CoDrone.CoDrone()
drone.pair(drone.Nearest, 'COM3')  # Change COM port

drone.takeoff()
time.sleep(5)  # Hover for 5 seconds
drone.land()

drone.close()
