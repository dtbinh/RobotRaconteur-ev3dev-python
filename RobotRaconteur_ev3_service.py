#!/usr/bin/python

# RobotRaconteur_ev3_service.py

# The MIT License (MIT)
# 
# Copyright (c) 2015 John Wason
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# This is a minimal example of an Ev3 Service. It is intended
# to be expanded as needed to implement your project.

import RobotRaconteur as RR
RRN=RR.RobotRaconteurNode.s
from ev3 import *

ev3_interface="""
service com.wasontech.ev3

object ev3

    property uint16[3] ColorRGB
    property uint8 Touch
    property int32 Proximity

    function void RunMotor(string motor, int32 velocity)
    function void StopMotor(string motor)
    
end object

"""

class ev3_impl(object):
    
    def __init__(self):
        try:        
            self._MotorA=lego.Motor('A')
        except: pass
        try:
            self._MotorB=lego.Motor('B')
        except: pass
        try:
            self._MotorC=lego.Motor('C')
        except: pass
        try:
            self._MotorD=lego.Motor('D')
        except: pass
        
        self._ColorSensor=lego.ColorSensor()
        self._TouchSensor=lego.TouchSensor()
        self._InfraredSensor=lego.InfraredSensor()
    
    @property
    def ColorRGB(self):
        return self._ColorSensor.rgb
    
    @property
    def Touch(self):
        return self._TouchSensor.is_pushed
    
    @property
    def Proximity(self):
        return self._InfraredSensor.prox 
        
    def RunMotor(self, motor, velocity):
        m=getattr(self,"_Motor" + motor)
        m.run_forever(velocity)
    
    def StopMotor(self, motor):
        m=getattr(self, "_Motor" + motor)
        m.stop()
    
    
def main():
    
    t=RR.TcpTransport()
    t.StartServer(58653)
    RRN.RegisterTransport(t)
    
    RRN.RegisterServiceType(ev3_interface)
    
    obj=ev3_impl()

    RRN.RegisterService("ev3", "com.wasontech.ev3.ev3", obj)
    
    raw_input("Press enter to quit")
    
    RRN.Shutdown()


if __name__ == '__main__':
    main()
