from utils.GPSHelper import GPSObject, GPSHelper
from utils.SerialHelper import SerialHelper

serial = SerialHelper("COM4")
gpsHelper = GPSHelper(serial)

gpsLoc = gpsHelper.getGPS()