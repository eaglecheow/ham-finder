import serial
import time
import datetime
import logging

class SerialHelper:

    def __init__(self, port: str, baudRate: int = 9600, doNotOpen: bool = False):
        super().__init__()

        self.port = port
        self.baudRate = baudRate
        self.serialObject = serial.Serial(port, baudRate, xonxoff=0, rtscts=0)

        if doNotOpen == False:
            self.openSerial()

    def openSerial(self):

        if self.serialObject.is_open == False:
            self.serialObject.open()

    def sendLine(self, text: str):
        if self.serialObject.is_open == False:
            raise Exception("[Serial] Trying to send data with closed serial")

        textInByte = text.encode() + b"\r\n"
        self.serialObject.write(textInByte)

    def readLine(self) -> str:
        if self.serialObject.is_open == False:
            raise Exception("[Serial] Trying to read data with closed serial")

        returnMessage = self.serialObject.readline().decode().strip("\r\n")
        print("[{}] {}".format(datetime.datetime.now().time(), returnMessage))

        return returnMessage

    def waitMessage(self, matchingString: str, timeout: int = 10000, errorMessage: str = None):
        startTime = time.time() * 1000

        while True:
            message = self.readLine()
            if message == matchingString:
                return

            currentTime = time.time() * 1000

            if (currentTime - startTime) > timeout:

                msg = errorMessage

                if msg == None:
                    msg = "[Serial] Timeout while waiting for expected message: {}".format(matchingString)

                raise Exception(msg)

