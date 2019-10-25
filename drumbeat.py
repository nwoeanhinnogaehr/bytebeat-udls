# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import time

# Start the system.
osc_startup()
tag='synbeat'

# Make client channels to send packets.
osc_udp_client("127.0.0.1", 8000, tag)

# Build a simple message and send it.
msg = oscbuildparse.OSCMessage("/renoise/song/bpm", ",i", [124])
osc_send(msg, tag)

# Periodically call osc4py3 processing method in your event loop.
finished = False
msgs = []
msgs.append(oscbuildparse.OSCMessage("/renoise/trigger/note_on", ",iiii", [1, 1, 48, 127]))
msgs.append(oscbuildparse.OSCMessage("/renoise/trigger/note_on", ",iiii", [2, 2, 48, 127]))
msgs.append(oscbuildparse.OSCMessage("/renoise/trigger/note_on", ",iiii", [3, 3, 48, 127]))
msgs.append(oscbuildparse.OSCMessage("/renoise/trigger/note_on", ",iiii", [4, 4, 48, 127]))
msgs.append(oscbuildparse.OSCMessage("/renoise/trigger/note_on", ",iiii", [5, 5, 48, 127]))
i = 0
while not finished:
    t = i%16 + i//64*16
    x = t^t>>1^t>>2
    y = x%(len(msgs)+1)
    if y != 0:
        osc_send(msgs[y-1], tag)
        time.sleep(1/8)
    osc_process()
    i += 1

# Properly close the system.
osc_terminate()
