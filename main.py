from pi import Pi
import os
import time
import traceback

p = Pi()
p.initialize()

run = True

while run:
    try:
        p.tick()

    except:
        run = False
        traceback.print_exc()
        time.sleep(1)

p.destruct()

