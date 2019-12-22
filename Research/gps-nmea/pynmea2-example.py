import serial
import pynmea2
import time

print("Process is starting...")

port = "COM4"

def parse_gps(dataByte):

    dataString = dataByte.decode("utf-8")

    if dataString.find("GGA") > 0:
        print("--> {}".format(dataByte))
        msg = pynmea2.parse(dataString)
        print("Timestamp: {} -- Lat: {} {} -- Lon: {} {} --Altitude: {} {} --Satellites: {}".format(msg.timestamp, msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, msg.altitude, msg.altitude_units, msg.num_sats))


serialPort = serial.Serial(port, baudrate=9600, timeout=0.5)

serialPort.write(b"AT+CGNSPWR=1\r\n")
time.sleep(1)
serialPort.write(b"AT+CGNSTST=1\r\n")

print("Reading serial...")

while True:
    str = serialPort.readline()
    parse_gps(str)