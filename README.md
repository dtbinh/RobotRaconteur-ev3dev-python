# RobotRaconteur-ev3dev-python

A python client and service for controlling the Lego ev3 device.

## Setup

#### 1. Install ev3dev on your device

Follow the installation instructions on the ev3dev website to create the SD card:

http://www.ev3dev.org/docs/getting-started/

Note: the default sign in information is:

    Username: root
    Password: r00tme


#### 2. Connect ev3 to the network

The easiest way to connect is through a USB to Ethernet adapter.  The StarTech USB 2.0 to Gigabit Ethernet NIC Network Adapter (USB21000S2) has worked well on the test network.  After booting the ev3 device, look  in the upper left hand corner of the LCD screen to find the IP address of the ev3 device.  On the test network it has been assigned 192.168.1.125.  Replace all occurances of 192.168.1.125 with the value seen on the LCD screen. 

#### 3. Copy Robot Raconteur Python for armel to the device

Go to http://robotraconteur.com/download on your computer and download "RobotRaconteur-{version}-Python.linux-armel-py2.7-{date}.tar.gz". (Replace {version} and {date} with the current release.) Once downloaded, copy it to the device using the command line scp or a tool like WinSCP. The scp command is:

    scp RobotRaconteur-{version}-Python.linux-armel-py2.7-{date}.tar.gz root@192.168.1.125:~
    
   
#### 4. SSH into the ev3 device and install software

Now it is time to ssh into the ev3 device and install some software. This can be done using the command line ssh program or using a tool such as Putty.

    ssh root@192.168.1.125
    
Run on the device:

    cd ~
    tar xf RobotRaconteur-{version}-Python.linux-armel-py2.7-{date}.tar.gz -C /
    apt-get install git python-smbus
    git clone https://github.com/topikachu/python-ev3.git
    git clone https://github.com/johnwason/RobotRaconteur-ev3dev-python
    
#### 5. Run the service on the ev3 device

In an ssh connection to the ev3 device run:

    export PYTHONPATH=/root/python-ev3
    cd RobotRaconteur-ev3dev-python
    python RobotRaconteur_ev3_service.py
    
At this point you should see "Service running, press enter to quit".  You can now connect to the service.

#### 6. Connect to the Robot Raconteur service

You can now connect to the service using any Robot Raconteur client.  The example Python client is:

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

Using MATLAB the code is similar:

    c=RobotRaconteur.ConnectService('tcp://192.168.1.125:58653/{0}/ev3');
    print "Running motors..."
    c.RunMotor('A',50)
    c.RunMotor('B',-50)
    sleep(1)
    c.StopMotor('A')
    c.StopMotor('B')
    
    disp(c.ColorRGB)
    disp(c.Touch)
    disp(c.Proximity)

## License

MIT license.

## Contributions

This is intended to be a simple example to demontrate how to use Robot Raconteur.  Any improvements are welcome!
    