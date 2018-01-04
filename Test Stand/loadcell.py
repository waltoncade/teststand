import sys
import time 
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
	ch = VoltageRatioInput()
except RuntimeError as e:
	print("Runtime Exception %s" % e.details)
	readin = sys.stdin.read(1)
	exit(1)

def VoltageRatioInputAttached(e):
    print("Attached!")

def VoltageRatioInputDetached(e):
    print("Detached") 

def VoltageRatioChangeHandler(e, voltageRatio):
    voltageRatio = (877420*voltageRatio)
    voltageZero.append(voltageRatio)
    print("VoltageRatio: %f" % voltageRatio)

def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

try:
	ch.setOnErrorHandler(ErrorEvent)
	ch.setOnAttachHandler(VoltageRatioInputAttached)
	ch.setOnVoltageRatioChangeHandler(VoltageRatioChangeHandler)
	ch.openWaitForAttachment(5000)
except PhidgetException as e:
	print("Phidget Exception %i: %s" % (e.code, e.details))
	readin = sys.stdin.read(1)
	exit(1)

ch.setBridgeEnabled(1)

voltageZero = []
voltlist = []

time.sleep(5)
voltavg = float(sum(voltageZero)) / float(len(voltageZero))

def VoltageRatioChangeHandler1(e, voltageRatio):
    voltageRatio = (877420*voltageRatio - voltavg)
    voltlist.append(voltageRatio)
    print("VoltageRatio: %f" % voltageRatio)

ch.setOnDetachHandler(VoltageRatioInputDetached)
ch.setOnVoltageRatioChangeHandler(VoltageRatioChangeHandler1)
time.sleep(10)
