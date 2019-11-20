from utils.SerialHelper import SerialHelper
import time

sh = SerialHelper("COM4")

sh.openSerial()
sh.sendLine("AT+CGNSPWR=1")
time.sleep(1)
sh.sendLine("AT+CGNSTST=1")
time.sleep(1)

while True:
    message = sh.readLine()
    print("Message: {}".format(message))