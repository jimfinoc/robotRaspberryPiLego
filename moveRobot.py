#!/usr/bin/python
mh = Adafruit_MotorHAT(addr=0x60)
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)



mh = Adafruit_MotorHAT(addr=0x60)

Motor1 = mh.getMotor(1)
Motor2 = mh.getMotor(2)

Motor1.setSpeed(200)
Motor2.setSpeed(200)


print "Forward! "
Motor1.setSpeed(0)
Motor2.setSpeed(0)
Motor1.run(Adafruit_MotorHAT.FORWARD)
Motor2.run(Adafruit_MotorHAT.FORWARD)

print "\tSpeed up..."
for i in range(255):
    Motor1.setSpeed(i)
    Motor2.setSpeed(i)
    time.sleep(0.005)

print "\tSlow down..."
for i in reversed(range(255)):
    Motor1.setSpeed(i)
    Motor2.setSpeed(i)
    time.sleep(0.005)

print "Release"
Motor1.run(Adafruit_MotorHAT.RELEASE)
Motor2.run(Adafruit_MotorHAT.RELEASE)
time.sleep(2.0)


Motor1.run(Adafruit_MotorHAT.FORWARD)
Motor2.run(Adafruit_MotorHAT.BACKWARD)



print "\tSpeed up..."
for i in range(255):
    Motor1.setSpeed(i)
    Motor2.setSpeed(i)
    time.sleep(0.002)

print "Release"
Motor1.run(Adafruit_MotorHAT.RELEASE)
Motor2.run(Adafruit_MotorHAT.RELEASE)
time.sleep(2.0)

Motor1.run(Adafruit_MotorHAT.FORWARD)
Motor1.setSpeed(10)
time.sleep(1.0)
Motor1.run(Adafruit_MotorHAT.RELEASE)


Motor1.setSpeed(0)
Motor2.setSpeed(0)
Motor2.run(Adafruit_MotorHAT.FORWARD)
Motor1.run(Adafruit_MotorHAT.FORWARD)
Motor1.setSpeed(25)
Motor2.setSpeed(25)
time.sleep(2)
Motor1.run(Adafruit_MotorHAT.RELEASE)
Motor2.run(Adafruit_MotorHAT.RELEASE)


def moveForward():
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(50)
    Motor2.setSpeed(50)
    time.sleep(2)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def rotateLeft():
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.BACKWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(50)
    Motor2.setSpeed(50)
    time.sleep(2)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def rotateRight():
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.BACKWARD)
    Motor1.setSpeed(50)
    Motor2.setSpeed(50)
    time.sleep(2)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def turnRight():
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(25)
    Motor2.setSpeed(75)
    time.sleep(2)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def turnLeft():
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(75)
    Motor2.setSpeed(25)
    time.sleep(2)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

