#!/usr/bin/python

# RobotRaconteur_ev3_example_client.py

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


# This is a minimal example of an Ev3 Client. It is intended
# to be expanded as needed to implement your project.

import time
import RobotRaconteur as RR
RRN=RR.RobotRaconteurNode.s

def main():
    t=RR.TcpTransport()
    RRN.RegisterTransport(t)
    
    #Change this URL to your ev3 device
    c=RRN.ConnectService('tcp://192.168.1.125:58653/{0}/ev3')
    
    #Run motors A and B for a second
    print "Running motors..."
    c.RunMotor('A',50)
    c.RunMotor('B',-50)
    time.sleep(1)
    c.StopMotor('A')
    c.StopMotor('B')
    
    print "ColorRGB: " + str(c.ColorRGB)
    print "Touch: " + str(c.Touch)
    print "Proximity: " + str(c.Proximity)

    RRN.Shutdown()

if __name__ == '__main__':
    main()