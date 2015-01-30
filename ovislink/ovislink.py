#  Copyright (c) 2013, captainblood13007
#
#  Ovislink.py is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

"""

@author: captainblood13007
@copyright: (C) 2013  captainblood13007
@license: GNU General Public License (GPL)
"""


class Ovislink(object):
    def __init__(self, ip, passw):


        self.ip = ip
        self.passw = passw

    def connect(self):                

        
        print "connecting... to the modem"
        try:
            self.tn = telnetlib.Telnet(self.ip, '23' , 5)
            self.tn.read_until("Login: ")
            print "enter radadmin."
            self.tn.write('radadmin\r\n')
            self.tn.read_until("Password: ")
            print "enter password."
            self.tn.write(self.passw+"\r\n")
            data = self.tn.read_until("> ")
            print "connected on the modem."
            print data
            self.tn.write("sysinfo\r")
            sysinfo = self.tn.read_until("> ")
            
            uptime = re.search('up(.+)' ,sysinfo)
            self.tn.write("adsl info\r\n")
            sync = self.tn.read_until("> ")
            print "you are connected"
            print  data, sync
            return " not available ", uptime.group(1)
            
        except IOError:
            try:
                self.tn = telnetlib.Telnet(self.ip, '2323' , timeout =5)
                self.tn.read_until("Login: ")
                self.tn.write('radadmin\r\n')
                self.tn.read_until("Password: ")
                self.tn.write(self.passw+"\r\n")
                data = self.tn.read_until("> ")
                print "you are connected"
                return data
                
            except IOError:                
                print "timing out please verify that the modem is connected"



    def sh_dsl(self):
        try:
            self.tn.write('adsl info --stats\r\n')
            data = self.tn.read_until("> ")
            #self.outputter(data, end='')
            return data
        except EOFError:
            print "the telnet session timed out. Please re-connect"
        
    def sh_arp(self):

        self.tn.write('arp show\r\n')
        data = self.tn.read_until(" > ")
        #self.outputter(data, end='')
        return data

    def sh_restart(self):
        self.tn.write('system reboot\r\n')
        #data = self.tn.read_until("{radadmin}=>")
        #print data,

    def sh_route(self):
        self.tn.write('route show\r\n')
        data = self.tn.read_until(" > ")
        #self.outputter(data, end='')
        return data

    def sh_log(self):
        self.tn.write('systemlog show\r\n')
        data = self.tn.read_until("{radadmin}=>")
        print data,

    def command(self, entry):


        self.tn.write(entry+'\r\n')
        data = self.tn.read_until(" > ")
        print data
    
        

    def disconnect(self):
    
        self.tn.close()
        #self.outputter("disconnect from the modem")
        print "disconnect from the modem"
        

import telnetlib
import re

