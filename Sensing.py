import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port , 9600)
serialFromArduino.flushInput()

while True:
    serialFromArduino.write('2')
    obj = serialFromArduino.readline()
    str = obj[:-2].decode()
    print str
