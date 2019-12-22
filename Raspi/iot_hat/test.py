from utils.GPSHelper import GPSObject, GPSHelper
from utils.SerialHelper import SerialHelper
from utils.TCPHelper import TCPHelper

serial = SerialHelper("COM6")
gpsHelper = GPSHelper(serial)
tcpHelper = TCPHelper(serial, "35.234.201.162", 8200, "celcom2g")

# location = gpsHelper.getGPSLocation()
# print("Coordinate: {}{}, {}{}".format(location.latitude, location.latitudeDirection, location.longitude, location.longitudeDirection))

tcpHelper.initializeDevice()
tcpHelper.sendMessage("This is a test message")
tcpHelper.sendMessage("Sending message from SIM7000E")