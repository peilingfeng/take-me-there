#!/usr/bin/python3

import evdev
import time
from espeak import espeak
e={79:1,80:2,81:3,75:4,76:5,77:6,71:7,72:8,73:9,82:0,96:96}

dev = evdev.InputDevice('/dev/input/event0')
for event in dev.read_loop():
	if(event.value == 1):
		for key in sorted(e.keys()):
			if(event.code==key)and(event.code!=96):
				print(e[key])
				espeak.synth("%d"%e[key])
			elif(event.code==key)and(event.code==96):
				espeak.synth("Goodbye")
				time.sleep(1)
				exit()
			



