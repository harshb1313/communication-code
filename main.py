# coding: UTF-8

from usb_rs import Usb_rs

#Timeout(1sec)
Timeout_default = 1

def main():
    #Instantiation of the usb_rs communication class
    serial = Usb_rs()

    #Connect
    print("Port?")
    port = input()
    print("Speed?")
    speed = int(input())
    if not serial.open(port,speed):
        return
    
    #Send and receive commands
    while True:
        print("Please enter the command (Exit with no input)")
        command = input()
        #Exit if no input
        if command == "":
            break
        #If the command contains "?"
        if "?" in command :
            msgBuf = serial.SendQueryMsg(command, Timeout_default)
            print(msgBuf) 
        #Send only
        else:
            serial.sendMsg(command)
        
    serial.close()

if __name__ == '__main__':
  main()
