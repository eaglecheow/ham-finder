from utils.SerialHelper import SerialHelper
import time


class TCPHelper:
    def __init__(
        self,
        serialObj: SerialHelper,
        hostIP: str,
        portNumber: int,
        cellularNetworkAPN: str,
    ):
        super().__init__()

        self.serialObj = serialObj
        self.hostIP = hostIP
        self.portNumber = portNumber
        self.cellularNetworkAPN = cellularNetworkAPN

        self.isInitialized = False

    def initializeDevice(self):

        if self.isInitialized == True:
            return

        messagePair = [
            ["AT+CGATT?", "OK"],
            ['AT+CSTT="{}"'.format(self.cellularNetworkAPN), "OK"],
            ["AT+CIICR", "OK"],
            ["AT+CIFSR", r"[REGEX]\d+\.\d+\.\d+\.\d+"],
            [
                'AT+CIPSTART="TCP","{}","{}"'.format(self.hostIP, self.portNumber),
                "CONNECT OK",
            ],
            ["AT+CIPSPRT=0", "OK"],
        ]

        self.serialObj.communicate(messagePair)

        self.isInitialized = True

    def sendMessage(self, message: str):

        if self.isInitialized == False:
            raise Exception("[TCP] TCP connection not initialized")

        self.serialObj.sendLine("AT+CIPSEND")
        self.serialObj.sendLine(message)
        self.serialObj.sendCtrlZ()

        self.serialObj.communicate([["[EMPTY]", "SEND OK"]])


    # def sendImage(self, image):
        
