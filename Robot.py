#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
Motor1 = mh.getMotor(1)
Motor2 = mh.getMotor(2)


print "Set conditions for stopped motors and moing forward! "
Motor1.setSpeed(0)
Motor2.setSpeed(0)
Motor1.run(Adafruit_MotorHAT.FORWARD)
Motor2.run(Adafruit_MotorHAT.FORWARD)

#print "\tSpeed up..."
#for i in range(255):
#    Motor1.setSpeed(i)
#    Motor2.setSpeed(i)
#    time.sleep(0.005)
#
#print "\tSlow down..."
#for i in reversed(range(255)):
#    Motor1.setSpeed(i)
#    Motor2.setSpeed(i)
#    time.sleep(0.005)
#
#print "Release"
#Motor1.run(Adafruit_MotorHAT.RELEASE)
#Motor2.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(2.0)
#
#
#Motor1.run(Adafruit_MotorHAT.FORWARD)
#Motor2.run(Adafruit_MotorHAT.BACKWARD)

#print "\tSpeed up..."
#for i in range(255):
#    Motor1.setSpeed(i)
#    Motor2.setSpeed(i)
#    time.sleep(0.002)
#
#print "Release"
#Motor1.run(Adafruit_MotorHAT.RELEASE)
#Motor2.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(2.0)
#
#Motor1.run(Adafruit_MotorHAT.FORWARD)
#Motor1.setSpeed(10)
#time.sleep(1.0)
#Motor1.run(Adafruit_MotorHAT.RELEASE)


#Motor1.setSpeed(0)
#Motor2.setSpeed(0)
#Motor2.run(Adafruit_MotorHAT.FORWARD)
#Motor1.run(Adafruit_MotorHAT.FORWARD)
#Motor1.setSpeed(25)
#Motor2.setSpeed(25)
#time.sleep(2)

def stop():
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)


def moveForward(timeSleeping=3):
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)
    Motor1.setSpeed(150)
    Motor2.setSpeed(150)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)

def moveBack(timeSleeping=3):
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)
    Motor1.setSpeed(75)
    Motor2.setSpeed(75)
    Motor2.run(Adafruit_MotorHAT.BACKWARD)
    Motor1.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)

def rotateLeft(timeSleeping=2):
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.BACKWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(50)
    Motor2.setSpeed(50)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def rotateRight(timeSleeping=2):
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.BACKWARD)
    Motor1.setSpeed(50)
    Motor2.setSpeed(50)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def turnRight(timeSleeping=2):
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(75)
    Motor2.setSpeed(150)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

def turnLeft(timeSleeping=1):
    Motor1.setSpeed(0)
    Motor2.setSpeed(0)
    Motor2.run(Adafruit_MotorHAT.FORWARD)
    Motor1.run(Adafruit_MotorHAT.FORWARD)
    Motor1.setSpeed(150)
    Motor2.setSpeed(75)
    time.sleep(timeSleeping)
    Motor1.run(Adafruit_MotorHAT.RELEASE)
    Motor2.run(Adafruit_MotorHAT.RELEASE)

#turnLeft(1)


#def program():
#    moveForward()
#    rotateRight()
#    moveForward()
#    rotateLeft()

def looping(inputValue="h"):
    while (inputValue!="q"):
#        print inputValue
        if str(inputValue)=="h":
            print "---------------------------------"
            print "press the key and enter to "
            print "h : to get this menu"
            print ""
            print "f : to go forward"
            print "b : to go backward"
            print ""
            print "r : to rotate right"
            print "t : to rotate left"
            print ""
            print "d : to turn left"
            print "g : to turn right"
            print ""
            print "q : to quit"
            print "---------------------------------"
        if inputValue=="f":
            moveForward()
        if inputValue=="b":
            moveBack()
        if inputValue=="t":
            rotateLeft()
        if inputValue=="r":
            rotateRight()
        if inputValue=="d":
            turnLeft()
        if inputValue=="g":
            turnRight()
        inputValue = raw_input('Enter your command: ')
        print inputValue


looping()