import serial
import pygame.midi

# Initialize serial
ser = serial.Serial(
        port='/dev/cu.usbmodem141301',
        baudrate=115200,
)

# Initialize midi
pygame.midi.init()
port = pygame.midi.get_default_output_id()
o = pygame.midi.Output(port)

while True:
    recvData = ser.read(3)
    recvData = int.from_bytes(recvData, byteorder='big', signed=False)
    print(bin(recvData))

    if recvData >> 20 == 0b1001:
        o.note_on((recvData >> 8) & 0b01111111, recvData & 0b01111111, (recvData >> 16) & 0b00001111)
    elif recvData >> 20 == 0b1000:
        o.note_off((recvData >> 8) & 0b01111111, recvData & 0b01111111, (recvData >> 16) & 0b00001111)
