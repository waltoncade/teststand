import socket
import piplates.RELAYplate as RELAY

#TCP_IP = "192.168.1.127"
TCP_IP = "192.168.1.132" #Server IP, not client IP.
#TCP_IP = "10.240.232.136"
TCP_PORT = 5000
BUF = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

def relay1_toggle():
	RELAY.relayTOGGLE(0,1)
	print "Relay 1 Toggled"
	return

def relay2_toggle():
	RELAY.relayTOGGLE(0,2)
	print "Relay 2 Toggled"
	return

def relay3_toggle():
	RELAY.relayTOGGLE(0,3)
	print "Relay 3 Toggled"
	return


while True:
	 
	conn,addr = s.accept()
	print("Connected")

	while True:
		data = conn.recv(BUF)
		if not data: break
		print data

		if 'relay_1' in data:
			print "Received data: ",data
			relay1_toggle()

		elif 'relay_2' in data:
			print "Received data: ",data
			relay2_toggle()

		elif 'relay_3' in data:
			print "Received data: ",data
			relay3_toggle()

conn.close()