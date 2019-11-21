import serial
import pynmea2
import time
from utils.SerialHelper import SerialHelper

class GPSObject:
    def __init__(self):
        super().__init__()

        self.timeStamp: int = 0
        self.latitude: float = None
        self.latitudeDirection: str = None
        self.longitude: float = None
        self.longitudeDirection: str = None
        self.altitude: float = None
        self.altitudeUnits: str = None
        self.satelliteAmount: int = 0

    def checkDataValidity(self) -> bool:
        if (
            not self.timeStamp or
            not self.latitude or
            not self.latitudeDirection or
            not self.longitude or
            not self.longitudeDirection or
            not self.altitude or
            not self.altitudeUnits or
            not self.satelliteAmount
        ):
            return False
        return True




class GPSHelper:

    def __init__(self, serialObj: SerialHelper):
        super().__init__()

        self.serialObj = serialObj
        self.isOpen = False

    @staticmethod
    def parseGps(dataString: str) -> GPSObject:
        msg = pynmea2.parse(dataString)

        gpsObject = GPSObject()
        gpsObject.timeStamp = msg.timestamp
        gpsObject.latitude = msg.lat
        gpsObject.latitudeDirection = msg.lat_dir
        gpsObject.longitude = msg.lon
        gpsObject.longitudeDirection = msg.lon_dir
        gpsObject.altitude = msg.altitude
        gpsObject.altitudeUnits = msg.altitude_units
        gpsObject.satelliteAmount = msg.num_sats

        return gpsObject

    def getGPS(self, timeout=10000):

        startTime = time.time() * 1000

        if self.isOpen == True:
            return

        self.serialObj.sendLine("AT+CGNSPWR=1")

        self.serialObj.waitMessage("OK", errorMessage="[GPS] Unable to get OK response from device")

        self.serialObj.sendLine("AT+CGNSTST=1")

        while True:
            response = self.serialObj.readLine()

            if not response.find("GGA") > 0:
                continue

            gpsObject = self.parseGps(response)

            if gpsObject.checkDataValidity() == True:
                return gpsObject

            currentTime = time.time() * 1000
            if (currentTime - startTime) > timeout:
                raise Exception("[GPS] Timeout while getting GPS location")      