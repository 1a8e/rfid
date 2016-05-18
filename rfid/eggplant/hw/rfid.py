import serial
import webbrowser
from time import sleep
from subprocess import Popen, PIPE

ser = serial.Serial('/dev/ttyUSB0', 9600)
base = 'http://localhost:8000/scroll/'
url_last = None

control_W_sequence = b'''keydown Control_L
key W
keyup Control_L
'''

def keypress(sequence):
	p = Popen(['xte'], stdin=PIPE)
	p.communicate(input=sequence)

while True:
	rfid = ser.read(12)
	print (rfid)
	if int(rfid[0:2], 16) ^ int(rfid[2:4], 16) ^ int(rfid[4:6], 16) ^ int(rfid[6:8], 16) ^ int(rfid[8:10], 16) == int(rfid[10:12], 16):
		url = base + str(rfid)[2:-1]
		if url != url_last:
			keypress(control_W_sequence)
			webbrowser.open_new_tab(url)
		url_last = url
		sleep(1)
	else:
		print ('[ERR] Checksum failed!')