from utils.GPSHelper import GPSObject, GPSHelper
from utils.SerialHelper import SerialHelper
from utils.TCPHelper import TCPHelper

serial = SerialHelper("COM4")
gpsHelper = GPSHelper(serial)
tcpHelper = TCPHelper(serial, "35.234.201.162", 8200, "celcom2g")

tcpHelper.initializeDevice()
tcpHelper.sendMessage("I'm skipping my class later!")
tcpHelper.sendMessage("WTHHHHHHHH")