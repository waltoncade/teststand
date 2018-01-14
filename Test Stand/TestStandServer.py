import piplates.RELAYplate as RELAY
import paho.mqtt.client as mqtt

HOST = "192.168.1.132"
TOPIC_1 = "Valve_Commands"
TOPIC_2 = "Valve_Readings"

print ("\nTest Stand Server Ready.")
print (("Please connect client software to: %s at port: %d \n") % (HOST, 1883))
print ("Waiting to establish connection........ \n")

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(TOPIC_1)
	error = rc
	return error

def on_disconnect(client, userdata,rc=0):
	print("Connection Lost.")
	client.loop_stop()

def on_message(client, userdata, msg):
	calldata(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.connect(HOST, 1883, 60)

print ("Connection established.")
#print ('Connection address: ',addr)
#logger.debug("Connection established at {}".format(time.asctime())) #find what the ip is
print ("Awaiting commands... \n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Feedback Logging Setup
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#setting up the logging program
#all of the logging events will be put into a text file wherever the location is specified
#the location can be specified by setting the "filename" equal to "anyname.log"
#if the logging filname is kept the same, the logging events will be put in the same file, adding to past events.


#logname = time.strftime("LC_ServerLog(%H_%M_%S).log",time.localtime())
#logger = logging.getLogger("")                                                                 
#logging.basicConfig(filename=logname, level=logging.DEBUG)


def relay1_on():
	RELAY.relayON(0,1)
	print("Relay 1 ON")
	client.publish(TOPIC_2,b'R1ON')
	return

def relay2_on():
	RELAY.relayON(0,2)
	print("Relay 2 ON")
	client.publish(TOPIC_2,b'R2ON')
	return

def relay3_on():
	RELAY.relayON(0,3)
	print("Relay 3 ON")
	client.publish(TOPIC_2,b'R3ON')
	return

def relay4_on():
	RELAY.relayON(0,4)
	print("Relay 4 ON")
	client.publish(TOPIC_2,b'R4ON')
	return

def relay5_on():
	RELAY.relayON(0,5)
	print("Relay 5 ON")
	client.publish(TOPIC_2,b'R5ON')
	return

def relay6_on():
	RELAY.relayON(0,6)
	print("Relay 6 ON")
	client.publish(TOPIC_2,b'R6ON')
	return

def relay7_on():
	RELAY.relayON(0,7)
	print("Relay 7 ON")
	client.publish(TOPIC_2,b'R7ON')
	return

def relay8_on():
	RELAY.relayON(1,1)
	print("Relay 8 ON")
	client.publish(TOPIC_2,b'R8ON')
	return

def relay9_on():
	RELAY.relayON(1,2)
	print("Relay 9 ON")
	client.publish(TOPIC_2,b'R9ON')
	return

def relay1_off():
	RELAY.relayOFF(0,1)
	print("Relay 1 OFF")
	client.publish(TOPIC_2,b'R1OFF')
	return

def relay2_off():
	RELAY.relayOFF(0,2)
	print("Relay 2 OFF")
	client.publish(TOPIC_2,b'R2OFF')
	return

def relay3_off():
	RELAY.relayOFF(0,3)
	print("Relay 3 OFF")
	client.publish(TOPIC_2,b'R3OFF')
	return

def relay4_off():
	RELAY.relayOFF(0,4)
	print("Relay 4 OFF")
	client.publish(TOPIC_2,b'R4OFF')
	return

def relay5_off():
	RELAY.relayOFF(0,5)
	print("Relay 5 OFF")
	client.publish(TOPIC_2,b'R5OFF')
	return

def relay6_off():
	RELAY.relayOFF(0,6)
	print("Relay 6 OFF")
	client.publish(TOPIC_2,b'R6OFF')
	return

def relay7_off():
	RELAY.relayOFF(0,7)
	print("Relay 7 OFF")
	client.publish(TOPIC_2,b'R7OFF')
	return

def relay8_off():
	RELAY.relayOFF(1,1)
	print("Relay 8 OFF")
	client.publish(TOPIC_2,b'R8OFF')
	return

def relay9_off():
	RELAY.relayOFF(1,2)
	print("Relay 9 OFF")
	client.publish(TOPIC_2,b'R9OFF')
	return



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Main Loop
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Our main loop is the listener or the TCP connection. It listens for 'data' and 
# uses this data to analyze what is being requested on the Launch Control Client. Data
# that is receieved requesting valve or ignitor actuation simply jumps into the correct
# function listed above. If sensor information is requested, new threads are started that
# use the target function specified to send sensor information back to the client software.


def calldata(data):

	if 'relay1_open' in data:
		print ("Received data: ",data)
		relay1_on()

	elif 'relay2_open' in data:
		print ("Received data: ",data)
		relay2_on()

	elif 'relay3_open' in data:
		print ("Received data: ",data)
		relay3_on()

	elif 'relay4_open' in data:
		print ("Received data: ",data)
		relay4_on()

	elif 'relay5_open' in data:
		print ("Received data: ",data)
		relay5_on()

	elif 'relay6_open' in data:
		print ("Received data: ",data)
		relay6_on()

	elif 'relay7_open' in data:
		print ("Received data: ",data)
		relay7_on()

	elif 'relay8_open' in data:
		print ("Received data: ",data)
		relay8_on()

	elif 'relay9_open' in data:
		print ("Received data: ",data)
		relay9_on()

	elif 'relay1_close' in data:
		print ("Received data: ",data)
		relay1_off()

	elif 'relay2_close' in data:
		print ("Received data: ",data)
		relay2_off()

	elif 'relay3_close' in data:
		print ("Received data: ",data)
		relay3_off()

	elif 'relay4_close' in data:
		print ("Received data: ",data)
		relay4_off()

	elif 'relay5_close' in data:
		print ("Received data: ",data)
		relay5_off()

	elif 'relay6_close' in data:
		print ("Received data: ",data)
		relay6_off()

	elif 'relay7_close' in data:
		print ("Received data: ",data)
		relay7_off()

	elif 'relay8_close' in data:
		print ("Received data: ",data)
		relay8_off()

	elif 'relay9_close' in data:
		print ("Received data: ",data)
		relay9_off()

client.loop_forever()