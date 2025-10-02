# CoDrone Project (CoDrone Pro + Python/Arduino)

Hands‑on drone programming with CoDrone Pro for TEOP workshops. This repo includes:
- A clear **setup guide** (Arduino + Python)
- **Example Python flight scripts** with an emergency landing key
- Links to official learning resources

> Safety first: Fly in an open space, use prop guards, and keep people/pets away from the drone while testing.

## Hardware
- CoDrone Pro quadcopter (Robolink)
- Smart Inventor Board + BLE module (controller)
- USB cable, Li‑Po battery

## Quick Start (Python)
1) **Install Python 3.9+** and **pip**.
2) **Install library**:
   ```bash
   pip install CoDrone keyboard
   ```
3) **Pair** your controller to the nearest drone once (use the Pairing example from Arduino library, or follow Robolink docs).
4) **Run** an example:
   ```bash
   python src/code1_emergency_flight.py
   ```
   Press `l` anytime to trigger **emergency landing**.

> The `keyboard` package on Windows may require running your terminal **as Administrator**. If that's an issue, try `code2_hover_only.py` which uses a simple timed hover and lands automatically.

## Quick Start (Arduino Controller)
- Install **Arduino IDE** → Boards: `Arduino Uno`
- Install the **CoDrone** library
- Set DIP switches: **upload mode** = switch 1 ON, 2 & 3 OFF; **run mode** = all OFF
- Upload an example like **Pairing** or **BasicControl**
- Use joystick/buttons for manual flight

## Repository Layout
```
CoDrone_Project/
├─ src/
│  ├─ code1_emergency_flight.py
│  └─ code2_hover_only.py
├─ docs/
│  └─ README_short.md
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Example: Emergency Flight (Python)
```python
# python src/code1_emergency_flight.py
import CoDrone
from CoDrone import Color
from CoDrone.protocol import Direction
import threading
import keyboard
import time

drone = CoDrone.CoDrone()
drone.pair(drone.Nearest, 'COM3')  # Change COM port if needed (Windows). Use '/dev/tty...' on macOS/Linux.
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
```

## Links & References
- Blockly course: https://learn.robolink.com/course/codrone-with-blockly/
- Python first program: https://learn.robolink.com/lesson/codrone-python-first-program/
- Python docs: https://docs.robolink.com/docs/CoDronePro_Lite/Python/Function-Documentation
- Pairing help: https://robolink.helpdocs.io/article/jiomh5z2d7-how-do-i-pair-in-python

## License
MIT — see `LICENSE`.

---
Prepared by **Kalash Chiragkumar Swami** (Department of Engineering Lab).
