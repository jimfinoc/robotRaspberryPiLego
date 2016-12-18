import smbus
import time
bus = smbus.SMBus(1)
address = 0xE0

#SRF08 REQUIRES 5V

def write(value):
    bus.write_byte_data(address, 0, value)
    return -1

def lightlevel():
    light = bus.read_byte_data(address, 1)
    return light

def range():
    range1 = bus.read_byte_data(address, 2)
    range2 = bus.read_byte_data(address, 3)
    range3 = (range1 << 8) + range2
    return range3

#while True:
print "write 0x51"
write(0x50)
print ""
time.sleep(1)
lightlvl = lightlevel()
print "rng = range()"
rng = range()
print lightlvl
print "rng"
print rng

