from utils.GPSHelper import GPSObject, GPSHelper
from utils.SerialHelper import SerialHelper

serial = SerialHelper("COM6")
gpsHelper = GPSHelper(serial)

gpsLoc = gpsHelper.getGPS(60000)

print("Latitude: {} {}".format(gpsLoc.latitude, gpsLoc.latitudeDirection))
print("Longitude: {} {}".format(gpsLoc.longitude, gpsLoc.longitudeDirection))